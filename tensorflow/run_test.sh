#!/usr/bin/env bash
# TODO: Precisei excluir o .meta do path
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/berhu/2018-06-29_17-59-58/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/berhu/2018-07-11_13-16-54/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/berhu/2018-07-22_22-22-01/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/berhu/2018-08-06_20-15-06/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/berhu/2018-08-07_19-48-23/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/mse/2018-06-29_13-52-58/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/all_px/mse/2018-08-02_00-51-48/restore/model.fcrn
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/berhu/2018-07-27_20-32-56/restore/model.fcrn # FIXME: Deu erro! Esse modelo é do tipo 1x1conv?
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/berhu/2018-08-06_09-25-11_1x1conv/restore/model.fcrn*
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/berhu/2018-08-06_11-30-47_1x1conv/restore/model.fcrn*
#python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/berhu/2018-08-06_20-08-50_1x1conv/restore/model.fcrn*
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/eigen/2018-07-30_01-30-18/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/eigen_grads/2018-07-30_10-49-02/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/eigen_grads/2018-07-31_09-30-16/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/mse/2018-08-03_13-44-09/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous/valid_px/mse/2018-08-03_22-14-03/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous_city/all_px/berhu/2018-08-03_22-14-10/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kitticontinuous_city/all_px/eigen/2018-08-02_19-54-56/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/all_px/berhu/2018-07-18_15-16-56/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/all_px/berhu/2018-07-19_13-38-29/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/all_px/berhu/2018-07-24_12-48-33/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/valid_px/berhu/2018-07-06_18-07-11/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/valid_px/berhu/2018-07-10_14-01-13/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/valid_px/berhu/2018-07-12_10-58-40/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidepth/valid_px/berhu/2018-07-13_15-06-16/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidiscrete/all_px/berhu/2018-07-19_10-18-17/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidiscrete/all_px/eigen_grads/2018-07-06_18-32-27/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidiscrete/all_px/eigen_grads/2018-07-17_10-51-47/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidiscrete/valid_px/berhu/2018-07-12_18-33-06/restore/model.fcrn
python3 predict_nick.py -m test -s kittidepth --test_split eigen_continuous -r output/fcrn/kittidiscrete/valid_px/berhu/2018-07-16_15-53-40/restore/model.fcrn

# *São do tipo 1x1conv