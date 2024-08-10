from openai import OpenAI

class ChatGPT:
    def __init__(self, api_key):
        """
        Initializes the ChatGPT class with an API key.
        
        :param api_key: Your OpenAI API key.
        """
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, prompt, user_text, model="gpt-3.5-turbo", temperature=0.5):
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_text}
        ]
        )

        return completion.choices[0].message

