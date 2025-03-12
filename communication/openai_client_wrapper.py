import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display, update_display

from .messages import Messages

class OpenAIWrapper:
    client: OpenAI
    model: str
    response_as_json: bool

    def __init__(
            self,
            *,
            api_key: str | None = None,
            url: str | None = None,
            model: str | None = None,
            response_as_json: bool = False,
    ) -> None:
        if api_key is None:
            load_dotenv(override=True)
            api_key = os.getenv('OPENAI_API_KEY')

        self.model = model
        self.response_as_json = response_as_json
        self.client = OpenAI(
            base_url=url,
            api_key=api_key
        )

    def chat(self, messages: Messages):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages.to_messages(),
            stream=messages.stream,
            response_format={"type": "json_object"} if self.response_as_json else None
        )

    def display(self, message: Messages):
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