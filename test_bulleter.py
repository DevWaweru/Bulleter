import unittest
import bulleter
new_list = []

class TestMyFile(unittest.TestCase):
    
    def test_reading(self):
        with open("test.txt","r") as bullet:
            data = bullet.readlines()
            return data
        self.assertEqual(data,bulleter.read_file("test.txt"))  

    def test_not_found(self):
        self.assertEqual(None,bulleter.read_file("text.txt"))
    
    def test_process_document(self):
        for i in bulleter.read_file("test.txt"):
            cap_lines = i.capitalize()
            new_sentence = ("*"+cap_lines[0:])
            new_list.append(new_sentence)
        
        self.assertEqual(new_list,bulleter.process_document())
        
if __name__ == "__main__":
    unittest.main()