import unittest
from unittest.mock import MagicMock
from luxserver import data_process, show_dialog
import filters_obj
from table import Table

class TestShowDialog(unittest.TestCase):
    def test_filters_obj(self):
        
        actual_output = data_process(Table(['table'],[['1,2,3']], is_object = True))
        expected_output = (
            [['1,2,3']]
        )
        self.assertEqual(actual_output, expected_output)

    def test_show_dialog(self):
        actual_output = show_dialog([1,2,3,4])
        expected_output = (
            "         Object Information\n\n-------------------------------\n\n"+
            "1\n\n"+
            "         Produced By\n\n-------------------------------\n\n"+
            "2\n\n"+
            "3\n\n"+
            "         Information: \n\n-------------------------------\n\n"+
            "4\n\n"
        )
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()