from .assistant_type import MultiAssistantTypes

class Messages:
    system: str
    user: str
    stream: bool
    assistant_types: MultiAssistantTypes

    def __init__(
            self,
            *,
            system: str | None = None,
            user: str,
            stream: bool = True,
            assistant_types: MultiAssistantTypes | None = None
    ) -> None:
        self.system = system
        self.user = user
        self.stream = stream
        self.assistant_types = assistant_types

    def to_messages(self) -> list:
        system_prompt = self.system
        if self.assistant_types is not None:
            system_prompt = f"{system_prompt} {self.assistant_types}"

        return [
            { "role": "system", "content": system_prompt },
            { "role": "user", "content": self.user },
        ]
