# Python default lib imports
import sys, os, random

# External imports to handle LLM models
from llama_cpp import Llama

# Store the path of the desired LLM model. This mechanism is used as a 
# fallback when the user does not specify a propper one in the class
# constructor. If you want to take advantage of this feature, change the
# value of this variable to the path of your desired model.
LLM_MODEL_PATH = "~/workspace/local-models/llm/Lexi-Llama-3-8B-Uncensored_Q4_K_M.gguf"


class ChatHandler:
    """Class to handle local chat with LLM models."""
    
    def __init__(self, 
        model_path: str = LLM_MODEL_PATH,
        streaming: bool = False,
        temperature: float = 0.7,
        repeat_penalty: float = 1.1,
        top_p: float = 0.9,
        top_k: int = 50,
        context_limit: int = 8192,
        ):
        """
        Initialize the LLM model with the specified parameters.
        
        Args:
            model_path (str): Path to the LLM model file. Use the default fallback one if there is none specified.
            streaming (bool): Whether the response of the model should be streamed or not. If not streamed, the response will be returned as a simple string object once the model has finished generating it.
            temperature (float): How randon the model's responses are. From 0 to 2, standard is around 0.7 or 0.8. Higher the value, more random the responses.
            repeat_penalty (float): Try to penalize the model when it repeat itself too much. From 1 to 2, standard is around 1.1.
            top_k (int): Limits the model choice of words for the top k choices. Standard is around 50.
            top_p (float): Also limit the model choice of words, but based on cumulative probability to use a word (Also know as nucleus sampling). From 0 to 1, standard is around 0.9.
                - Example: If the model is 80% sure the next word is "cat" and 10% sure it is "dog", it stops there. It won't even consider "elephant"
            context_limit (int): The maximum s
        
        Summary of what you're doing:
        - When the model needs to pick a word, it applies them in this order:
            - Top_K: "Throw away everything except the top 50 words."
            - Top_P: "Of those 50, keep only the ones that make up the top 90% probability."
            - Repeat Penalty: "Lower the score of any word we just used."
            - Temperature: "Now, shuffle the remaining probabilities. If temp is high, boost the underdogs. If temp is low, boost the favorite."
            - Selection: Pick the winner.
        """

        # Set the attibutes to the class instance
        self.model_path = model_path
        self.streaming = streaming
        self.temperature = temperature
        self.repeat_penalty = repeat_penalty
        self.top_p = top_p
        self.top_k = top_k
        self.context_limit = context_limit

        # Instance the model
        self._load_model()


    def _load_model(self):
        """
        Load the LLM model into memory
        """

        # Load the model from the specified path
        self.model = Llama(
            model_path=self.model_path,
            n_ctx=self.context_limit,
            repeat_penalty=self.repeat_penalty,
            top_p=self.top_p,
            top_k=self.top_k,
            temperature=self.temperature,

            n_threads=4,
            verbose=False,
        )
        
    def _save_context(self, messages: list):
        """
        Save the context of the conversation
        """

        print("In development")
        

    def _load_context(self, file_path: str):
        """
        Load the context of the conversation
        """

        print("In development")


    def _clean_context(self, file_path: str):
        """
        Clean the context of the conversation
        """

        print("In development")


    def chat(self, messages: list):
        """
        Chat with the LLM model
        """

        print("In development")


    def chat_no_context(self, messages: list):
        """
        Chat with the LLM model without context
        """

        print("In development")







