from .messages import Messages

class CodeExplanationMessages(Messages):
    def __init__(
            self,
            *,
            code: str,
            additional_context: str = "",
            additional_system_directives: str = "",
            stream: bool = True,
    ) -> None:
        default_system = "You are a helpful code explanation assistant. Explain the code clearly, including its purpose, logic, and any notable patterns or techniques. Always respond with markdown."
        if additional_system_directives:
            default_system += f"\n\n{additional_system_directives}"

        user_message = f"Please explain what this code does and why:\n\n```\n{code}\n```"
        if additional_context:
            user_message += f"\n\nAdditional context: {additional_context}"

        super().__init__(
            system = default_system,
            user = user_message,
            stream = stream
        )