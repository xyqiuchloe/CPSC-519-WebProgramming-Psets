
import unittest
from unittest.mock import patch
import filters_obj
import lux

class TestLux(unittest.TestCase):

    def test_main(self):
        # Test that the main function correctly calls filters_obj.filter_term2
        # and filters_obj.get_filtered_objects with the right arguments
        with patch.object(filters_obj, 'get_filtered_objects') as mock_get_filtered_obj:
            args_list = ["-a", "duchamp", "-l", "tu"]
            args = [['agt', 'duchamp'],['label' ,'tu']]
            with patch('sys.argv', ['lux.py'] + args_list):
                lux.main()
                mock_my_filter = filters_obj.filter_term2(*args)
                mock_get_filtered_obj.assert_called_once_with(mock_my_filter)


if __name__ == '__main__':
    unittest.main()
