import httpx
import re
from openai import OpenAI
from typing import List, Dict, Optional


class OpenAIClient:
    def __init__(self, api_key: str, api_base: str, model: str = "gpt-4"):
        """
        Initializza il client OpenAI con API key e model.

        Args:
            api_key (str): La tua chiave API OpenAI.
            api_base (str): L'URL base del servizio compatibile con OpenAI.
            model (str): Il modello OpenAI da utilizzare (default 'gpt-4').
        """
        custom_http_client = httpx.Client(verify=False)
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=api_base,
            http_client=custom_http_client  # Usa il client HTTP custom
        )
        self.model = model

    def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7, max_tokens: int = 1024) -> str:
        """
        Invia un messaggio all'API chat di OpenAI e restituisce la risposta.

        Args:
            messages (List[Dict[str, str]]): Lista di messaggi in formato [{"role": "user", "content": "Hello"}]
            temperature (float): Temperatura di sampling.
            max_tokens (int): Numero massimo di token nell'output.

        Returns:
            str: La risposta dal modello.
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

    def complete(self, prompt: str, temperature: float = 0.3, max_tokens: int = 4096, model: Optional[str] = None) -> str:
        """
        Invia un prompt all'API completion di OpenAI e restituisce la risposta.

        Args:
            prompt (str): La stringa di input.
            temperature (float): Temperatura di sampling.
            max_tokens (int): Numero massimo di token nell'output.
            model (str, optional): Modello di completamento (es. 'text-davinci-003').

        Returns:
            str: La risposta dal modello.
        """
        # Nota: alcuni servizi compatibili potrebbero non supportare l'API di completamento legacy
        # ma solo l'API di chat.completions
        response = self.client.completions.create(
            model=model or self.model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
    
    def get_python(self, prompt: str, temperature: float = 0.7, max_tokens: int = 4096, model: Optional[str] = None) -> str:
        """
        Invia un prompt all'API completion di OpenAI e restituisce la risposta.

        Args:
            prompt (str): La stringa di input.
            temperature (float): Temperatura di sampling.
            max_tokens (int): Numero massimo di token nell'output.
            model (str, optional): Modello di completamento (es. 'text-davinci-003').

        Returns:
            str: La risposta dal modello.
        """
        # Nota: alcuni servizi compatibili potrebbero non supportare l'API di completamento legacy
        # ma solo l'API di chat.completions
        response = self.client.completions.create(
            model=model or self.model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None
        )
        txtresponse = response.choices[0].text.strip()
        return self.extract_python_code(txtresponse)

    def extract_python_code(self,input_string: str) -> str:
        pattern = r'```python(.*?)```'
        match = re.search(pattern, input_string, re.DOTALL)
        
        return match.group(1).strip() if match else input_string  