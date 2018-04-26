def _get_optimizer_instance(name, hp):
    from keras.optimizers import SGD, Adam

    if name.lower() == 'adam':
        optimizer = SGD(lr=hp['learn_rate'], momentum=hp['momentum'])
    elif name.lower() == 'sgd':
        optimizer = Adam(lr=hp['learn_rate'])
    else:
        raise ValueError('Optimizer {} not supported.'.format(name))

    return optimizer


def mutually_exclusive_classes_dense_model_builder(n_hidden_layers=1,
                                            n_neurons_hidden_layers=8,
                                            init_mode='normal',
                                            activation='relu',
                                            optimizer='adam',
                                            learn_rate=0.001,
                                            momentum=0.,

                                            DATASET_INFO=None,
                                            compute_custom_metrics=False):

    from keras.models import Sequential
    from keras.layers import Dense
    from .custom_metrics import f1_score, auc, precision, recall

    number_of_classes = DATASET_INFO['number_of_classes']
    number_of_features = len(DATASET_INFO['features_columns_indexes'])

    model = Sequential()

    # Add the input layer
    model.add(Dense(number_of_features, kernel_initializer=init_mode, input_dim=number_of_features, activation=activation))

    # Add hidden layers
    for n in range(0, n_hidden_layers):
        model.add(Dense(n_neurons_hidden_layers, kernel_initializer=init_mode, activation=activation))

    # Add the ouput layer
    model.add(Dense(number_of_classes, kernel_initializer=init_mode, activation='softmax'))

    optimizer = _get_optimizer_instance(name=optimizer, hp=dict(learn_rate=learn_rate,
                                                            momentum=momentum))

    if compute_custom_metrics:
        metrics = ["acc", f1_score, precision, recall, auc]
    else:
        metrics = None

    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=metrics)
    return model
