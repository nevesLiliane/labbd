# from pyspark import SQLContext
# from pprint import pprint


def init_spark():
    from pyspark import SparkContext

    spark_context = SparkContext.getOrCreate()
    spark_context.setLogLevel('OFF')

    return spark_context


def train_model(X, y, param_grid, use_spark=False, spark_context=None, sklearn_parallel_jobs=False):
    if param_grid is None:
        raise ValueError('Param grid is None')

    if use_spark:
        if spark_context is None:
            raise ValueError('Spark context is None')

        return train_model_with_spark(X, y, param_grid=param_grid, spark_context=spark_context)
    else:
        return train_model_sklearn_only(X, y, param_grid=param_grid, sklearn_parallel_jobs=sklearn_parallel_jobs)


def train_model_with_spark(X, y, param_grid, spark_context):
    from keras.wrappers.scikit_learn import KerasClassifier
    from spark_sklearn import GridSearchCV
    from .custom_model_builders import mutually_exclusive_classes_dense_model_builder

    model = KerasClassifier(build_fn=mutually_exclusive_classes_dense_model_builder, verbose=0)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, sc=spark_context, scoring="accuracy")
    grid_result = grid.fit(X, y)
    return grid_result


def train_model_sklearn_only(X, y, param_grid, sklearn_parallel_jobs=False):
    from keras.wrappers.scikit_learn import KerasClassifier
    from sklearn.model_selection import GridSearchCV
    from .custom_model_builders import mutually_exclusive_classes_dense_model_builder

    if sklearn_parallel_jobs:
        n_jobs = -1
    else:
        n_jobs = 1

    model = KerasClassifier(build_fn=mutually_exclusive_classes_dense_model_builder, verbose=0)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=n_jobs, scoring="accuracy")
    grid_result = grid.fit(X, y)
    return grid_result
