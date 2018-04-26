from util.decorators import async_process
from engine import coordinator
from util.json import json_to_dict
from numpy import arange
import collections

from engine.defs import WAITING, EXECUTING, DONE
from engine.defs import OPTIMIZER, INIT_MODE, BATCH_SIZE, EPOCHS, LEARN_RATE, MOMENTUM, ACTIVATION, N_HIDDEN_LAYERS, N_NEURONS_HIDDEN_LAYERS

from config import DEFAULT_SPLIT_SIZE

from logger import experiment_logger

# -------------------------------------------------------------------------------


def hyperparameters_as_list_of_values(parameter_tuple_or_list_or_value):

    if isinstance(parameter_tuple_or_list_or_value, list):
        return parameter_tuple_or_list_or_value
    elif isinstance(parameter_tuple_or_list_or_value, tuple):

        start = parameter_tuple_or_list_or_value[0]
        stop = parameter_tuple_or_list_or_value[1]
        step = parameter_tuple_or_list_or_value[2]

        return arange(start, stop, step).tolist()
    else:
        return [parameter_tuple_or_list_or_value]


@async_process  # isso executa o método em um processo novo
def start_experiment():
    '''
    atualiza o controle interno de multiplos experimentos e inicia a execução
    '''
    from config import FORCE_CPU_ONLY
    if FORCE_CPU_ONLY:
        import os
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
        os.environ["CUDA_VISIBLE_DEVICES"] = ""

    coordinator.create_experiment()

    experiment_logger.info("Experiment ended.")


def finalize_or_abort_experiment():
    '''
    atualiza o controle interno de multiplos experimentos e indica que a execução foi concluída normalmente ou interrompe forçadamente a execução
    '''
    coordinator.finalize_or_abort_experiment()


def is_experiment_active():
    if coordinator.get_experiment_status() == 0:
        return True
    else:
        return False

# -------------------------------------------------------------------------------


def remove_block(block_id):
    coordinator.remove_block_from_queue(block_id)


def move_block_up(block_id):
    coordinator.move_task_up(block_id)


def move_block_down(block_id):
    coordinator.move_task_down(block_id)


def convert_hyper_hyper_to_hyper(hyper_hyper_parameters_data_dict):
    hyperparameters_values_list_dict = dict(
        n_hidden_layers=hyper_hyper_parameters_data_dict[N_HIDDEN_LAYERS],
        n_neurons_hidden_layers=hyper_hyper_parameters_data_dict[N_NEURONS_HIDDEN_LAYERS],
        init_mode=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[INIT_MODE]),
        activation=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[ACTIVATION]),

        optimizer=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[OPTIMIZER]),
        learn_rate=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[LEARN_RATE]),
        momentum=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[MOMENTUM]),

        batch_size=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[BATCH_SIZE]),
        epochs=hyperparameters_as_list_of_values(hyper_hyper_parameters_data_dict[EPOCHS]),
    )
    return hyperparameters_values_list_dict


def add_blocks_to_queue(hyper_hyper_parameters_data_dict, split_size=None, batchMode=True):
    '''
    recebe um hyper_hyper_parameters_data_dict e o utiliza para criar um ÚNICO bloco, caso batchMode=False
    ou multiplos blocos de tamanho médio (numero de combinações distintas dentro dele) igual ao valor informado em "mean size", caso batchMode=True
    '''

    hyperparameters_values_list_dict = convert_hyper_hyper_to_hyper(hyper_hyper_parameters_data_dict)

    if split_size is not None and batchMode:
        coordinator.add_blocks_to_queue(hyperparameters_values_list_dict, split_size=split_size)
    else:
        coordinator.add_block_to_queue(hyperparameters_values_list_dict)


def load_hyper_hyper(hyper_hyper_parameters_data_dict):
    coordinator.clear_waiting_queue()
    # from pprint import pprint
    # pprint(hyper_hyper_parameters_values_dict)
    hyperparameters_values_list_dict = convert_hyper_hyper_to_hyper(hyper_hyper_parameters_data_dict)
    coordinator.add_blocks_to_queue(hyperparameters_values_list_dict, split_size=DEFAULT_SPLIT_SIZE)


def clear_waiting_queue():
    coordinator.clear_waiting_queue()


def get_blocks(task_id=None):
    '''
    retorna um array de objetos com os detalhes de cada block, em qualquer ordem, para a task_id passada
    ou para mais recente se nenhuma for passado
    '''
    pass


def get_queue(task_id=None):
    '''
    retorna um array de objetos com os detalhes de cada block incluindo o status de execução (executando, a executar, já executado),
    na ordem em que serão executados, para a task_id passada ou para mais recente se nenhuma for passado
    '''

    queue_list = []

    for block in coordinator.get_task_queue():
        block_dict = json_to_dict(block)
        block_view = dict(
            block_id=block_dict['block_id'],
            status=WAITING,
            block_size=block_dict['block_size']
        )
        queue_list.append(block_view)

    for block in coordinator.get_experiment_queue():
        block_dict = json_to_dict(block)
        block_view = dict(
            block_id=block_dict['block_id'],
            status=EXECUTING,
            block_size=block_dict['block_size']
        )
        queue_list.append(block_view)

    for block in coordinator.get_done_queue():
        block_dict = json_to_dict(block)
        block_view = get_block_view(block_dict)
        queue_list.append(block_view)

    queue_list.reverse()

    return queue_list


def get_legend(hyperparameters_list):

    legend_list = []

    for hyperparameters_dict in hyperparameters_list:

        item_list = []

        for label, value in hyperparameters_dict.items():
            # print(key)
            item = str(label)+': '+str(value)
            item_list.append(item)

        legend = ', '.join(item_list)
        legend_list.append(legend)

    return legend_list


def get_block_view(block_dict):
    results_dict = block_dict['results']
    block_view = collections.OrderedDict(
        block_id=block_dict['block_id'],
        labels=get_legend(results_dict['hyperparameters']),
        accuracy=results_dict['score'],
        status=DONE,
        block_size=block_dict['block_size']
        )
    return block_view


def get_blocks_results(task_id=None):
    '''
    retorna um array de objetos com os detalhes de cada block já executado com o resultado, na ordem em que foram executados, para a task_id passada
    ou para mais recente se nenhuma for passado
    '''

    experiment_id = coordinator.get_experiment_id()
    block_data = list()

    for block in coordinator.get_done_queue():
        block_dict = json_to_dict(block)
        block_view = get_block_view(block_dict)
        block_data.append(block_view)

    block_data.reverse()

    result_dict = dict(
        experiment_id=experiment_id,
        block_data=block_data
    )

    return result_dict

# -------------------------------------------------------------------------------


def get_queue_data_as_table():
    blocksData = get_queue()

    # import mock_data
    # blocksData = mock_data.blocksData

    queueData = list()

    i = 1

    for blockData in blocksData:
        blockQueueData = list()

        blockQueueData.append(i)
        i += 1

        blockQueueData.append(blockData['block_id'])
        blockQueueData.append(blockData['block_size'])

        if 'accuracy' in blockData:
            idx = blockData['accuracy'].index(max(blockData['accuracy']))
            blockQueueData.append(blockData['accuracy'][idx])
        else:
            blockQueueData.append(' - ')

        if blockData['status'] == EXECUTING:
            blockQueueData.append(' Running ')
        elif blockData['status'] == DONE:
            blockQueueData.append(' Ready ')
        else:
            blockQueueData.append(' Waiting ')

        blockQueueData.append('')

        queueData.append(blockQueueData)

    result_dict = dict(
        experiment_id=coordinator.get_experiment_id(),
        data=queueData
    )

    return result_dict


def get_from_directory():
   ''' userSchema = StructType().add("name", "string").add("age", "integer") StructType([StructField("f1", StringType, True)])
    val
    csvDF = spark
    .readStream
    .option("sep", ";")
    .schema(userSchema) // Specify
    schema
    of
    the
    csv
    files
    .csv("/path/to/directory") // Equivalent
    to
    format("csv").load("/path/to/directory")


csvDf.writeStream.format("console").option("truncate", "false").start()'''
