import openai
import os

class ChatGPTClient:
    def __init__(self, api_key=None, model="gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required.")
        openai.api_key = self.api_key
        self.model = model

    def ask(self, prompt, temperature=0.7, max_tokens=150):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    client = ChatGPTClient(api_key="your-openai-api-key")
    prompt = "Explain the difference between a list and a tuple in Python."
    response = client.ask(prompt)
    print("ChatGPT:", response)
