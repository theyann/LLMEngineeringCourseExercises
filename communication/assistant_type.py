from enum import Enum

class AssistantType(Enum):
    """
    Assistant personality types that can be combined using the | operator.
    """
    NEUTRAL = "You are neutral."
    FRIENDLY = "You are friendly and kind."
    SNARKY = "You are snarky and sarcastic."
    COURTEOUS = "You are courteous and kind."
    COMEDIAN = "You try to turn everything into a joke."
    SAD = "You are sad and try to make people feel sad."
    EXCITED = "You are excited and try to make people feel excited."
    ANGRY = "You are angry all the time."

class MultiAssistantTypes:
    types: list[AssistantType]

    def __init__(
            self,
            types: list[AssistantType]
    ) -> None:
        self.types = types

    def __str__(self) -> str:
        return " ".join(t.value for t in self.types)
