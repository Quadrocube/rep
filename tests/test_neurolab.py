# Copyright 2014-2015 Yandex LLC and contributors <https://yandex.com/>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import division, print_function, absolute_import
from rep.test.test_estimators import check_classifier, check_regression
from sklearn.ensemble import BaggingClassifier
from rep.estimators.sklearn import SklearnClassifier
from rep.estimators.neurolab import NeurolabClassifier, NeurolabRegressor
import neurolab as nl

__author__ = 'Sterzhanov Vladislav'


N_EPOCHS2 = 100
N_EPOCHS4 = 800
N_EPOCHS_REGR = 950


def test_neurolab_single_classification():
    check_classifier(NeurolabClassifier(show=0, layers=[], epochs=N_EPOCHS2, trainf=nl.train.train_rprop),
                     supports_weight=False, has_staged_pp=False, has_importances=False)
    check_classifier(NeurolabClassifier(net_type='single-layer', cn='auto', show=0, epochs=N_EPOCHS2, trainf=nl.train.train_delta),
                     supports_weight=False, has_staged_pp=False, has_importances=False)


def test_neurolab_multiple_classification():
    check_classifier(NeurolabClassifier(show=0, layers=[], epochs=N_EPOCHS4, trainf=nl.train.train_rprop),
                     supports_weight=False, has_staged_pp=False, has_importances=False, n_classes=4)
    check_classifier(NeurolabClassifier(net_type='single-layer', cn='auto', show=0, epochs=N_EPOCHS4, trainf=nl.train.train_delta),
                     supports_weight=False, has_staged_pp=False, has_importances=False, n_classes=4)


def test_neurolab_regression():
    check_regression(NeurolabRegressor(layers=[], show=0, epochs=N_EPOCHS_REGR, trainf=nl.train.train_rprop),
                     supports_weight=False, has_importances=False, has_staged_predictions=False)
    check_regression(NeurolabRegressor(net_type='single-layer', cn='auto', show=0, epochs=N_EPOCHS_REGR, trainf=nl.train.train_delta),
                     supports_weight=False, has_importances=False, has_staged_predictions=False)


def test_neurolab_stacking():
    base_nlab = NeurolabClassifier(show=0, layers=[], epochs=N_EPOCHS2, trainf=nl.train.train_rprop)
    check_classifier(SklearnClassifier(clf=BaggingClassifier(base_estimator=base_nlab, n_estimators=3)),
                     supports_weight=False, has_staged_pp=False, has_importances=False)
