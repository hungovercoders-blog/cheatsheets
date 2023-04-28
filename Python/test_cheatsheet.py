import unittest
from cheatsheet import CheatSheet

## create tests for cheatsheet class
class TestCheatSheet(unittest.TestCase):
    
    def setUp(self):
        self.my_cheat = CheatSheet("dataGriff")
    
    def test_name(self):
        self.assertEqual(self.my_cheat.my_name, "dataGriff")
        
    def test_list_length(self):
        self.assertEqual(self.my_cheat.list_length, 4)
        
    def test_beer_list(self):
        self.assertEqual(self.my_cheat.beer_list, ["crafty devil","flowerhorn","mad dog","pipes"])
        
    def test_reverse_list(self):
        self.assertEqual(self.my_cheat.reverse_beer_list, ["pipes","mad dog","flowerhorn","crafty devil"])
        
    def test_first_list(self):
        self.assertEqual(self.my_cheat.first_list, "crafty devil")
    
    def test_last_list(self):
        self.assertEqual(self.my_cheat.last_list, "pipes")
        
    def test_second_third_slice(self):
        self.assertEqual(self.my_cheat.second_third_slice, ["flowerhorn","mad dog"])
        
    def test_last_two_slice(self):
        self.assertEqual(self.my_cheat.last_two_slice, ["mad dog","pipes"])
        
    def test_dict(self):
        self.assertEqual(self.my_cheat.beer_dict, {"tiny rebel":"clwb tropicana","crafty devil":"mike rayer","flowerhorn":"sprinkles"})
    
    def test_tuple(self):
        self.assertEqual(self.my_cheat.beer_tuple, ("tiny rebel","clwb tropicana"))
        
    def test_hello_coder(self):
        self.assertEqual(self.my_cheat.hello_coder(), "Hello dataGriff, you are now a hungovercoder")  
        
    def test_tiny_rebel_removed(self):
        self.assertNotIn("tiny rebel",self.my_cheat.beer_list)

if __name__ == '__main__':
    unittest.main()