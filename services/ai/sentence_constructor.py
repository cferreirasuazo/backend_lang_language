
from services.ai.llm_client import ChatGPTClient

class SentenceConstructor:
    def __init__(self, chatgpt_client: ChatGPTClient):
        self.client = chatgpt_client

    def construct_sentence(self, user_prompt: str) -> str:
        full_prompt = (
            f"Based on the following input, generate a complete, natural English sentence:\n"
            f"\"{user_prompt}\"\n"
            f"Make sure the sentence is grammatically correct."
        )
        return self.client.ask(full_prompt)