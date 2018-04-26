def read_dataset_info(dataset_key):
    import json
    # from pprint import pprint
    import os

    data = json.load(open(os.path.join('dataset', 'dt_infos.json')))
    data = data[dataset_key]

    if data['data_source'] == "":
        data['data_source'] = None
    if data['train_data_source'] == "":
        data['train_data_source'] = None
    if data['test_data_source'] == "":
        data['test_data_source'] = None

    features_columns_indexes = data['features_columns_indexes']

    if features_columns_indexes == 'all':
        if data['data_source'] is not None:
            source_file = data['data_source']
        elif data['test_data_source'] is not None:
            source_file = data['test_data_source']
        else:
            source_file = data['train_data_source']

        df = _read_data_frame(source_file, nrows=1)
        number_of_columns = df.shape[1]

        features_columns_indexes = set(list(range(0, number_of_columns))) - set([data['classes_column_index']])

    data['features_columns_indexes'] = list(set(features_columns_indexes) - set(data['features_columns_indexes_to_ignore']))
    # pprint(data)
    return data


def read_classification_dataset(dataset_key=None):
    if dataset_key is None:
        from config import DATASET_INFO
    else:
        DATASET_INFO = read_dataset_info(dataset_key)

    return _read_classification_dataset(source_file=DATASET_INFO['data_source'],
                                        train_source_file=DATASET_INFO['train_data_source'],
                                        test_source_file=DATASET_INFO['test_data_source'],
                                        features_columns=DATASET_INFO['features_columns_indexes'],
                                        classes_column=DATASET_INFO['classes_column_index'])


def _get_path_raw_data(file_name):
    import os
    return os.path.join('dataset', 'raw_data', file_name)


def _read_data_frame(file_source, **kargs):
    from pandas import read_csv
    return read_csv(open(_get_path_raw_data(file_source), 'rUb'), sep=',', index_col=None, header=None, compression='bz2', **kargs)


def _read_files(source_file=None, train_source_file=None, test_source_file=None):
    if source_file is None and (train_source_file is None or test_source_file is None):
        raise ValueError('Source files names are missing. {}, {}, {}'.format(source_file, train_source_file, test_source_file))

    elif source_file is not None:
        df = _read_data_frame(source_file)

    else:
        from pandas import concat
        df_train = _read_data_frame(train_source_file)
        df_test = _read_data_frame(test_source_file)
        dfs = [df_train, df_test]
        df = concat(dfs)
    # from pprint import pprint
    # pprint(df_train)
    # pprint(df_test)
    # pprint(df)
    return df


def _read_classification_dataset(source_file=None, train_source_file=None, test_source_file=None, features_columns=None, classes_column=None):
    from numpy import array

    df = _read_files(source_file=source_file, train_source_file=train_source_file, test_source_file=test_source_file)

    number_of_columns = df.shape[1]

    if classes_column is None:
        classes_column = number_of_columns - 1
    elif not isinstance(classes_column, int):
        raise ValueError('Wrong type for columns of classes.')
    else:
        classes_column = list(range(0, number_of_columns))[classes_column]

    if features_columns is None:
        features_columns = list(set(range(0, number_of_columns)) - set([classes_column]))
    elif not isinstance(features_columns, list):
        raise ValueError('Wrong type for columns of features.')
    elif len(set(features_columns).intersection(set([classes_column]))) != 0:
        raise ValueError('Wrong input for columns of features. features_columns={}, classes_column={}'.format(features_columns, classes_column))

    # print(features_columns)
    # print(classes_column)

    # from pprint import pprint
    # pprint(df.iloc[:, features_columns])
    # pprint(df.iloc[:, classes_column])

    X = array(df.iloc[:, features_columns])
    y = array(df.iloc[:, classes_column])

    return dict(X=X, y=y, y_one_hot_enconded=_one_hot_enconde_y(y))


def _one_hot_enconde_y(y):
    from keras.utils import np_utils
    from sklearn.preprocessing import LabelEncoder

    # encode class values as integers
    encoder = LabelEncoder()
    encoder.fit(y)
    encoded_y = encoder.transform(y)
    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_y)

    # from pprint import pprint
    # pprint(y)
    # pprint(dummy_y)

    return dummy_y
