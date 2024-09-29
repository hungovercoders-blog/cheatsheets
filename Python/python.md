---
key: value
---

<header class="site-header">
  <a href="https://blog.hungovercoders.com"><img alt="hungovercoders" src="../assets/logo3.ico"
    width=50px align="left"></a>
</header>

# Python

- [Python](#python)
  - [Class](#class)
  - [Test Class](#test-class)
 
## Tools

- [Streamlit Cheatsheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Streamlit Cheatsheet App](https://cheat-sheet.streamlit.app/)

## Class

```python
class CheatSheet:

    def __init__(self, my_name):
        """Creates a cheatsheet class that creates a numbers of properties and a list to act upon 

        Args:
            my_name (_type_): Your name
        """
        self.my_name = my_name
        self.beer_list = ["tiny rebel","garabage","crafty deval","flowerhorn","mad dog"]
        self.reverse_beer_list = []
        self.working_brewer = ""
        self.process_beer_list()
        self.first_list = self.beer_list[0]
        self.last_list = self.beer_list[-1]
        self.second_third_slice = self.beer_list[1:3]
        self.last_two_slice = self.beer_list[-2:]
        self.list_length = len(self.beer_list)
        
        self.beer_dict = {"tiny rebel":"clwb tropicana","crafty devil":"mike rayer","flowerhorn":"sprinkles"}
        self.beer_tuple = ("tiny rebel","clwb tropicana")
        
    def hello_coder(self,coder_type='hungovercoder'):
        """Prints a message saying hello to the coder

        Args:
            coder_type (str, optional): _description_. Defaults to 'hungovercoder'.

        Returns:
            string: A message saying hello
        """
        message = f"Hello {self.my_name}, you are now a {coder_type}"
        print(message)
        return message
    
    def process_beer_list(self):
        """Applies various example list type commands against the beer list
        """
        self.beer_list.append("pipes")
        self.beer_list.append("mistake")
        self.beer_list.remove("mistake")
        self.beer_list[2]= "crafty devil"
        del self.beer_list[1]
        self.beer_list.sort()
        self.working_brewer = self.beer_list.pop(-1)
        self.reverse_beer_list  = self.beer_list[:]
        self.reverse_beer_list.reverse()
```

## Test Class

```py
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
```
