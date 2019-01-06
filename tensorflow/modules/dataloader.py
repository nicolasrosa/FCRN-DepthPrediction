# ===========
#  Libraries
# ===========
import sys

import tensorflow as tf

from modules.datasets.apolloscape import Apolloscape
from modules.datasets.kitti_continuous import KittiContinuous
from modules.datasets.kitti_depth import KittiDepth
from modules.datasets.kitti_discrete import KittiDiscrete
from modules.datasets.nyudepth import NyuDepth
from modules.datasets.lrmjose import LRMJose
from modules.datasets.idrid_xande import idridXande


# ==================
#  Global Variables
# ==================


# ===========
#  Functions
# ===========
def getFilenamesTensors(image_filenames, depth_filenames):
    tf_image_filenames = tf.convert_to_tensor(image_filenames)
    tf_depth_filenames = tf.convert_to_tensor(depth_filenames)

    return tf_image_filenames, tf_depth_filenames


# ===================
#  Class Declaration
# ===================
class Dataloader:
    def __init__(self, args):
        # Defines dataset_root path depending on which machine is used.
        dataset_root = None

        if args.machine == 'nicolas':
            if args.dataset == 'lrmjose':
                dataset_root = "/home/nicolas/Downloads/" #TODO: Mudar de Folder
            elif args.dataset == 'idrid_xande':
                dataset_root = "/home/nicolas/Downloads/" #TODO: Mudar de Folder
            else:
                dataset_root = "/media/nicolas/nicolas_seagate/datasets/"
        elif args.machine == 'olorin':
            dataset_root = "/media/olorin/Documentos/datasets/"

        # Detects which dataset was selected and creates the 'dataset'.
        # print(args.dataset)

        if args.dataset == 'apolloscape':
            dataset_path = dataset_root + "apolloscape/data/"
            self.dataset = Apolloscape(dataset_path=dataset_path, name=args.dataset, height=2710, width=3384, max_depth=None)

        elif args.dataset == 'kitti_depth':
            dataset_path = dataset_root + "kitti/"
            self.dataset = KittiDepth(dataset_path=dataset_path, name=args.dataset, height=375, width=1242, max_depth=80.0)

        elif '_'.join(args.dataset.split('_')[:2]) == 'kitti_discrete':
            dataset_path = dataset_root + "kitti/raw_data/"
            self.dataset = KittiDiscrete(dataset_path=dataset_path, name=args.dataset, height=375, width=1242, max_depth=None)

        elif '_'.join(args.dataset.split('_')[:2]) == 'kitti_continuous':
            dataset_path = dataset_root + "kitti/raw_data/"
            self.dataset = KittiContinuous(dataset_path=dataset_path, name=args.dataset, height=375, width=1242, max_depth=85.0)

        elif args.dataset == 'nyudepth':
            dataset_path = dataset_root + "nyu-depth-v2/data/images/"
            self.dataset = NyuDepth(dataset_path=dataset_path, name=args.dataset, height=480, width=640, max_depth=None)

        elif args.dataset == 'lrmjose':
            dataset_path = dataset_root + "lrmjose/"
            self.dataset = LRMJose(dataset_path=dataset_path, name=args.dataset, height=256, width=455, max_depth=None)
        elif args.dataset == 'idrid_xande':
            dataset_path = dataset_root + "idrid_xande/"
            self.dataset = idridXande(dataset_path=dataset_path, name=args.dataset, height=256, width=455, max_depth=None)
        else:
            print("[Dataloader] The typed dataset '%s' is invalid. "
                  "Check the list of supported datasets." % args.dataset)
            sys.exit()

        # Searches dataset image/depth filenames lists
        self.train_image_filenames, self.train_depth_filenames, self.numTrainSamples = None, None, -1
        self.tf_train_image_filenames, self.tf_train_depth_filenames = None, None

        self.test_image_filenames, self.test_depth_filenames, self.numTestSamples = None, None, -1
        self.tf_test_image_filenames, self.tf_test_depth_filenames = None, None

        if args.mode == 'train':
            _ = self.getTrainData()
            _ = self.getTestData()

            self.tf_train_image_key = None
            self.tf_train_image = None

            self.tf_train_depth_key = None
            self.tf_train_depth = None

        elif args.mode == 'test':
            self.tf_test_image_key = None
            self.tf_test_image = None

            self.tf_test_depth_key = None
            self.tf_test_depth = None

        print("\n[Dataloader] dataloader object created.")

    def getTrainData(self, mode='train'):
        image_filenames, depth_filenames, _ = self.dataset.getFilenamesLists(mode)
        tf_image_filenames, tf_depth_filenames = getFilenamesTensors(image_filenames, depth_filenames)

        try:
            print("Summary - TrainData")
            print("image_filenames: ", len(image_filenames))
            print("depth_filenames: ", len(depth_filenames))

            self.numTrainSamples = len(image_filenames)

        except TypeError:
            print("[TypeError] 'image_filenames' and 'depth_filenames' are None.")

        self.train_image_filenames = image_filenames
        self.train_depth_filenames = depth_filenames
        self.tf_train_image_filenames = tf_image_filenames
        self.tf_train_depth_filenames = tf_depth_filenames

        return image_filenames, depth_filenames, tf_image_filenames, tf_depth_filenames, self.numTrainSamples

    def getTestData(self, mode='test', test_split='', test_file_path=''):
        image_filenames, depth_filenames, file = self.dataset.getFilenamesLists(mode, test_split, test_file_path)
        tf_image_filenames, tf_depth_filenames = getFilenamesTensors(image_filenames, depth_filenames)

        try:
            print("Summary - TestData (Validation Set)")
            print("image_filenames: ", len(image_filenames))
            print("depth_filenames: ", len(depth_filenames))

            self.numTestSamples = len(image_filenames)

        except TypeError:
            print("[TypeError] 'image_filenames' and 'depth_filenames' are None.")

        self.test_image_filenames = image_filenames
        self.test_depth_filenames = depth_filenames
        self.tf_test_image_filenames = tf_image_filenames
        self.tf_test_depth_filenames = tf_depth_filenames

        return image_filenames, depth_filenames, tf_image_filenames, tf_depth_filenames, self.numTestSamples, file

    @staticmethod
    def rawdepth2meters(tf_depth, dataset_name):
        """True Depth Value Calculation. May vary from dataset to dataset."""
        if dataset_name == 'apolloscape':
            # Changes the invalid pixel value (65353) to 0.
            tf_depth = tf.cast(tf_depth, tf.float32)
            tf_imask = tf.where(tf_depth < 65535, tf.ones_like(tf_depth), tf.zeros_like(tf_depth))
            tf_depth = tf_depth * tf_imask

            tf_depth = tf_depth / 200.0
        elif dataset_name == 'kitti_depth':
            tf_depth = (tf.cast(tf_depth, tf.float32)) / 256.0
        elif '_'.join(dataset_name.split('_')[:2]) == 'kitti_discrete' or \
             '_'.join(dataset_name.split('_')[:2]) == 'kitti_continuous':
            tf_depth = (tf.cast(tf_depth, tf.float32)) / 3.0
        elif dataset_name == 'nyudepth':
            tf_depth = (tf.cast(tf_depth, tf.float32)) / 1000.0
        elif dataset_name == 'lrmjose':
            tf_depth = (tf.cast(tf_depth, tf.float32)) / 1.0 # TODO: Correto?
        elif dataset_name == 'idrid_xande':
            tf_depth = (tf.cast(tf_depth, tf.float32)) / 1.0 # TODO: Correto?
        return tf_depth

    @staticmethod
    def removeSky(tf_image, tf_depth, dataset_name):
        """Crops Input and Depth Images (Removes Sky)"""
        if dataset_name[0:5] == 'kitti':
            tf_image_shape = tf.shape(tf_image)
            tf_depth_shape = tf.shape(tf_depth)

            crop_height_perc = tf.constant(0.3, tf.float32)
            tf_image_new_height = tf.cast(crop_height_perc * tf.cast(tf_image_shape[0], tf.float32), tf.int32)
            tf_depth_new_height = tf.cast(crop_height_perc * tf.cast(tf_depth_shape[0], tf.float32), tf.int32)

            tf_image = tf_image[tf_image_new_height:, :]
            tf_depth = tf_depth[tf_depth_new_height:, :]

        return tf_image, tf_depth

    @staticmethod
    def decodeImages(tf_image_key, tf_depth_key, dataset_name):
        tf_image_file = tf.read_file(tf_image_key)
        tf_depth_file = tf.read_file(tf_depth_key)

        if dataset_name == 'apolloscape':
            tf_image = tf.image.decode_jpeg(tf_image_file, channels=3)
        else:
            tf_image = tf.image.decode_png(tf_image_file, channels=3, dtype=tf.uint8)

        if '_'.join(dataset_name.split('_')[:2]) == 'kitti_discrete' or \
           '_'.join(dataset_name.split('_')[:2]) == 'kitti_continuous' or \
           dataset_name == 'lrmjose' or \
           dataset_name == 'idrid_xande':
            tf_depth = tf.image.decode_png(tf_depth_file, channels=1, dtype=tf.uint8)
        else:
            tf_depth = tf.image.decode_png(tf_depth_file, channels=1, dtype=tf.uint16)

        # Print Tensors
        print("tf_image_file: \t", tf_image_file)
        print("tf_depth_file: \t", tf_depth_file)

        return tf_image, tf_depth
