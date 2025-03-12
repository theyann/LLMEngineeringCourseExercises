from communication import Messages


class BrochureLinksMessages(Messages):
    url: str
    links: list

    def __init__(
            self,
            *,
            url: str,
            links: list,
    ) -> None:
        self.url = url
        self.links = links

        super().__init__(
            system=self._make_system_prompt(),
            user=self._make_user_prompt(),
            stream=False
        )

    def _make_system_prompt(self) -> str:
        return """
You are provided with a list of links found on a webpage.
            
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.

You must respond with **pure JSON only**—without any extra text, explanations, or formatting such as markdown.
     
You should respond in JSON as in this example:
{
  "links": [
    { "type": "about page", "url": "https://full.url/goes/here/about" },
    { "type": "careers page": "url": "https://another.full.url/careers" }
  ]
}

Do not include markdown (` ```json `) or any additional text before or after the JSON. Only return valid JSON.
        """

    def _make_user_prompt(self) -> str:
        user_prompt = f"""
Here is the list of links on the website of {self.url} - 
            
please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.
            
Links (some might be relative links):\n
        """
        user_prompt += "\n".join(self.links)
        return user_prompt
