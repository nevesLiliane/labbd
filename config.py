# -*- coding: utf8 -*-
from logger import experiment_logger
from dataset.dt_handler import read_dataset_info, read_classification_dataset
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# Redis setup
RDB_RESULTS_HOST = 'localhost'
RDB_RESULTS_PORT = 6379
RDB_RESULTS_NO = 1

# MonetDB setup

MONEDB_USERNAME = "admin"
MONETDB_PASSWORD = "monetdb"
MONETDB_HOST = "localhost"
MONEDB_PROV_DB = "prov"

# email server
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# available languages
LANGUAGES = {
    'en': 'English',
}

# administrator list
ADMINS = ['you@example.com']

# DATASET_INFO_KEY = 'pima-indians-diabetes'
DATASET_INFO_KEY = 'MNIST'

DATASET_INFO = read_dataset_info(DATASET_INFO_KEY)
DATASET_DATA = None


def get_data_set_data():
    global DATASET_DATA
    if DATASET_DATA is None:
        experiment_logger.info("Reading dataset data.")
        DATASET_DATA = read_classification_dataset(DATASET_INFO_KEY)
    return DATASET_DATA


isProvOn = False

DEFAULT_SPLIT_SIZE = 10

USE_SPARK = True

PARALLEL_WITHOUT_SPARK = False

FORCE_CPU_ONLY = True
