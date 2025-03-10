import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

from communication.messages import Message

class OpenAIWrapper:
    client: OpenAI

    def __init__(
            self,
            *,
            api_key: str | None = None,
            url: str | None = None,
            model: str | None = None,
    ) -> None:
        if api_key is None:
            load_dotenv(override=True)
            api_key = os.getenv('OPENAI_API_KEY')

        self.model = model
        self.client = OpenAI(
            base_url=url,
            api_key=api_key
        )

    def chat(self, message: Message):
        return self.client.chat.completions.create(
            model=self.model,
            messages=message.to_messages(),
            stream=message.stream,
        )

    def display(self, message: Message):
        if message.stream:
            self.stream_markdown(self.chat(message))
        else:
            self.display_markdown(self.chat(message))

    def display_markdown(self, response):
        display(Markdown(response.choices[0].message.content))

    def stream_markdown(self, stream):
        response = ""
        display_handle = display(Markdown(""), display_id=True)
        for chunk in stream:
            response += chunk.choices[0].delta.content or ''
            response = response.replace("```", "").replace("markdown", "")
            update_display(Markdown(response), display_id=display_handle.display_id)