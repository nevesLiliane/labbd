import collections

hyperparameters_values_list_dict1 = collections.OrderedDict(
    optimizer=['Adam', 'Adamax'],
    init_mode=['uniform'],
    batch_size=[10],
    epochs=[10],
    learn_rate=[0.1, 0.2, 0.3],
    momentum=[0.1, 0.2, 0.3],
    activation=['sigmoid'],
    n_hidden_layers=[1],
    n_neurons_hidden_layers=[8],
)


hyperparameters_values_list_dict2 = collections.OrderedDict(
    optimizer=['SGD'],
    init_mode=['uniform'],
    batch_size=[10],
    epochs=[10],
    learn_rate=[0.1, 0.2, 0.3],
    momentum=[0.1],
    activation=['sigmoid'],
    n_hidden_layers=[1],
    n_neurons_hidden_layers=[8],
)


hyperparameters_values_list_dict3 = collections.OrderedDict(
    optimizer=['Adam'],
    init_mode=['uniform'],
    batch_size=[20],
    epochs=[10],
    learn_rate=[0.01],
    momentum=[0.],
    activation=['sigmoid'],
    n_hidden_layers=[0],
    n_neurons_hidden_layers=[8],
)


hyper_hyper_parameters_values_dict_list = [
    dict(
        optimizer=['SGD'],
        init_mode=['normal'],
        batch_size=[100],
        epochs=[10],
        learn_rate=(0.001, 0.9, 0.001),
        momentum=[0.005],
        activation=['sigmoid'],
        n_hidden_layers=[1],
        n_neurons_hidden_layers=[8],
    ),
    dict(
        optimizer=['SGD'],
        init_mode=['normal'],
        batch_size=[100],
        epochs=[10],
        learn_rate=(0.1, 0.3, 0.1),
        momentum=[0.005],
        activation=['sigmoid'],
        n_hidden_layers=[1],
        n_neurons_hidden_layers=[8],
    ),
    dict(
        optimizer=['SGD'],
        init_mode=['normal'],
        batch_size=[100],
        epochs=[10],
        learn_rate=(0.1, 0.8, 0.1),
        momentum=[0.005],
        activation=['sigmoid'],
        n_hidden_layers=[1],
        n_neurons_hidden_layers=[8],
    ),
    dict(
        optimizer=['SGD'],
        init_mode=['normal'],
        batch_size=[100],
        epochs=[10],
        learn_rate=(0.1, 0.6, 0.2),
        momentum=[0.005],
        activation=['sigmoid'],
        n_hidden_layers=[1],
        n_neurons_hidden_layers=[8],
    ),
]

blocksData = [{
    'block_id': 10,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 13,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 23,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 33,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 43,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 53,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 63,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 73,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 83,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 93,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 433,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 343,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 3,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 235,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.456, 0.98],
    'status': 1,
  }, {
    'block_id': 3,
    'labels': ['epocas: 5, bath:30, ...', 'epocas: 98, bath: bla, ...'],
    'accuracy': [0.766, 0.65],
    'status': 1,
  }, {
    'block_id': 2,
    'status': 0,
  }, {
    'block_id': 0,
    'status': -1,
  }]


block = dict(
    block_id=0,
    hyperparameters=[
        collections.OrderedDict(
            optimizer='Adam',
            init_mode='uniform',
            batch_size=10,
            epochs=10,
            learn_rate=0.1,
            momentum=0.1),
        collections.OrderedDict(
            optimizer='Adam',
            init_mode='uniform',
            batch_size=10,
            epochs=10,
            learn_rate=0.1,
            momentum=0.1)
            ],
    results=[0.6, 1.3],
    status=1
)

block_final = dict(
        block_id=0,
        hyperparameters=0,
        results=dict(
            hyperparameters=[
                collections.OrderedDict(
                    optimizer='Adam',
                    init_mode='uniform',
                    batch_size=10,
                    epochs=10,
                    learn_rate=0.1,
                    momentum=0.1),
                collections.OrderedDict(
                    optimizer='Adam',
                    init_mode='uniform',
                    batch_size=10,
                    epochs=10,
                    learn_rate=0.1,
                    momentum=0.1)
                ],
            score=[0.6, 1.3])
)

block_final = dict(
        block_id=0,
        hyperparameters=0,
        results=dict(
            hyperparameters=[
                collections.OrderedDict(
                    optimizer='Adam',
                    init_mode='uniform',
                    batch_size=10,
                    epochs=10,
                    learn_rate=0.1,
                    momentum=0.1),
                collections.OrderedDict(
                    optimizer='Adam',
                    init_mode='uniform',
                    batch_size=10,
                    epochs=10,
                    learn_rate=0.1,
                    momentum=0.1)
                ],
            score=[0.6, 1.3])
)
