import unittest
from unittest.mock import patch
import luxdetails
# import filters_detail

class TestLuxDetails(unittest.TestCase):
    
    @patch('luxdetails.filters_detail.object_details')
    def test_main(self, mock_object_details):
        args_list = ['50128']
        with patch('sys.argv', ['luxdetails.py'] + args_list):
            luxdetails.main()
            mock_object_details.assert_called_once_with(50128)
        
if __name__ == '__main__':
    unittest.main()
