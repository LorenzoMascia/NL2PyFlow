import unittest
import os
from core.code_generator import generate_code_for_block
from dotenv import load_dotenv

class TestCodeGenerator(unittest.TestCase):
    
    def test_generate_code_for_block_with_real_api(self):
        """
        Test generation of Python code from a block description using the real OpenAI API.
        """
        # Carica le variabili d'ambiente dal file .env
        load_dotenv()

        # Prepariamo il blocco di input (un esempio di descrizione di un blocco)
        block = {
            "name": "block_1",
            "description": "Create a function add that takes two arguments a and b and returns their sum"
        }

        # Directory di output per il file generato
        output_dir = "real_output"
        
        # Chiamata alla funzione per generare il codice
        file_path = generate_code_for_block(block, output_dir)
        
        # Verifica che il file sia stato creato
        self.assertTrue(os.path.exists(file_path))
        self.assertIn("block_1.py", file_path)
        
        # Verifica che il contenuto generato contenga la struttura della funzione
        with open(file_path, "r") as file:
            generated_code = file.read()
            self.assertIn("def add(context: dict) -> dict:", generated_code)
            self.assertIn("context[\"sum\"] = a + b", generated_code)

        # Pulizia (rimuovere il file creato durante il test)
        os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
