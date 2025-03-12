from communication import Messages, MultiAssistantTypes


class BrochureGenerationMessages(Messages):
    company_name: str
    details: str

    def __init__(
            self,
            *,
            company_name: str,
            details: str,
            types: MultiAssistantTypes,
    ) -> None:
        self.company_name = company_name
        self.details = details

        super().__init__(
            system=self._make_system_prompt(),
            user=self._make_user_prompt(),
            stream=False,
            assistant_types=types
        )

    def _make_system_prompt(self) -> str:
        return """
           You are an assistant that analyzes the contents of several relevant pages from a company website
            and creates a short brochure about the company for prospective customers, investors and recruits. 
            Respond in markdown.
            Include details of company culture, customers and careers/jobs if you have the information.
        """

    def _make_user_prompt(self) -> str:
        user_prompt = f"""
            You are looking at a company called: {self.company_name}
            Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.
            
            {self.details}
        """
        return user_prompt[:5_000]  # Truncate if more than 5,000 characters
