import json
import unittest
from abc import ABCMeta

from repository.mongo_mock_repository import MongoMockRepository


class MongoBaseTest(unittest.TestCase):
    # __metaclass__ = ABCMeta
    """Class with setup and tearsdown for all others tests"""


    def setUp(self):
        mock = MongoMockRepository()
        self.data_source = mock.get_data_source()

        files_names = ['clientes-test.json', 'produtos-test.json', 'faturamento-test.json']

        for file_name in files_names:
            collection_name = file_name.split('-')[0]
            with open('data\\' + file_name, 'r') as file:
                for line in file:
                    document = json.loads(line)
                    del document['_id']
                    self.data_source[collection_name].save(document)