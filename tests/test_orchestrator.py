import unittest
import os
from core.orchestrator import Orchestrator

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = Orchestrator()
        # Create a temporary test file if needed
        self.test_input_file = "test_input.txt"
        with open(self.test_input_file, "w") as f:
            f.write("Create a function hello that prints 'Hello, World!'")
    
    def tearDown(self):
        # Clean up temporary files
        if os.path.exists(self.test_input_file):
            os.remove(self.test_input_file)
        
        if os.path.exists("output.py"):
            os.remove("output.py")
    
    def test_process_string_input(self):
        """Test processing a direct string input."""
        input_text = "Create a function add that takes parameters a and b and returns their sum"
        result = self.orchestrator.process_string(input_text)
        
        self.assertIsNotNone(result)
        self.assertIn("def add(a, b):", result)
        self.assertIn("return a + b", result)
    
    def test_process_file_input(self):
        """Test processing input from a file."""
        result = self.orchestrator.process_file(self.test_input_file)
        
        self.assertIsNotNone(result)
        self.assertIn("def hello():", result)
        self.assertIn("print('Hello, World!')", result)
    
    def test_save_output(self):
        """Test saving output to a file."""
        input_text = "Create a variable x set to 10"
        self.orchestrator.process_and_save(input_text, "output.py")
        
        self.assertTrue(os.path.exists("output.py"))
        with open("output.py", "r") as f:
            content = f.read()
            self.assertIn("x = 10", content)
    
    def test_multiple_blocks(self):
        """Test processing multiple blocks."""
        input_text = """
        Create a variable count set to 0
        Create a function increment that increases count by 1
        Create a loop that calls increment 5 times
        """
        result = self.orchestrator.process_string(input_text)
        
        self.assertIn("count = 0", result)
        self.assertIn("def increment():", result)
        self.assertIn("for", result)
    
    def test_error_handling(self):
        """Test handling of errors in the pipeline."""
        input_text = "This is not a valid command"
        
        # The orchestrator should handle exceptions from its components
        with self.assertRaises(Exception):
            self.orchestrator.process_string(input_text)
    
    def test_end_to_end(self):
        """Test the full end-to-end process with a complex example."""
        input_text = """
        Create a function calculate_factorial that:
        - Takes a parameter n
        - Creates a variable result set to 1
        - Creates a loop from 1 to n
        - In the loop, multiplies result by the current index
        - Returns result
        """
        result = self.orchestrator.process_string(input_text)
        
        self.assertIn("def calculate_factorial(n):", result)
        self.assertIn("result = 1", result)
        self.assertIn("for", result)
        self.assertIn("range", result)
        self.assertIn("result *=", result)
        self.assertIn("return result", result)

if __name__ == "__main__":
    unittest.main()