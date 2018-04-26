#!flask/bin/python
import sys
import mock_data
from pprint import pprint

from engine import interface as engine_interface

from dataset.dt_handler import read_classification_dataset


if __name__ == '__main__':

    if len(sys.argv) == 1:
        read_classification_dataset()

    elif sys.argv[1] == 'start_experiment' or sys.argv[1] == 'se':
        engine_interface.start_experiment()

    elif sys.argv[1] == 'finalize_or_abort_experiment' or sys.argv[1] == 'fae':
        engine_interface.finalize_or_abort_experiment()

    elif sys.argv[1] == 'add_block' or sys.argv[1] == 'ab':
        engine_interface.add_blocks_to_queue(mock_data.hyperparameters_values_list_dict3)

    elif sys.argv[1] == 'load_hyper_hyper' or sys.argv[1] == 'lhh':
        engine_interface.load_hyper_hyper(mock_data.hyper_hyper_parameters_values_dict_list[0])

    elif sys.argv[1] == 'clear_waiting_queue' or sys.argv[1] == 'cwq':
        engine_interface.clear_waiting_queue()

    elif sys.argv[1] == 'block_results' or sys.argv[1] == 'br':
        results = engine_interface.get_blocks_results()

        if results is not None:
            pprint(results)

    elif sys.argv[1] == 'get_queue' or sys.argv[1] == 'gq':
        queue = engine_interface.get_queue()

        if queue is not None:
            pprint(queue)

    elif sys.argv[1] == 'get_queue_table' or sys.argv[1] == 'gqt':
        queue = engine_interface.get_queue_data_as_table()

        if queue is not None:
            pprint(queue)

    else:
        print("Inexistent option.")

    # from tensorflow.python.client import device_lib
    # print(device_lib.list_local_devices())
