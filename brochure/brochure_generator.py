import json

from communication import Messages, OpenAIWrapper, AssistantType, MultiAssistantTypes
from web.website import Website

from .brochure_links_messages import BrochureLinksMessages
from .brochure_generation_messages import BrochureGenerationMessages


class BrochureGenerator:
    company_name: str
    website: Website
    client: OpenAIWrapper
    types: MultiAssistantTypes

    def __init__(
            self,
            *,
            company_name: str,
            url: str,
            client: OpenAIWrapper,
            types: MultiAssistantTypes,
    ) -> None:
        self.company_name = company_name
        self.website = Website(url)
        self.client = client
        self.types = types

    def _make_link_ai_messages(self) -> Messages:
        return BrochureLinksMessages(
            links=self.website.links,
            url=self.website.url
        )

    def _make_generation_ai_messages(self) -> Messages:
        return BrochureGenerationMessages(
            company_name=self.company_name,
            details=self._get_all_details(),
            types=self.types
        )

    def _get_links(self):
        link_response = self.client.chat(self._make_link_ai_messages()).choices[0].message.content
        return json.loads(link_response)

    def _get_all_details(self):
        result = f"Landing page:\n{self.website.get_contents()}"
        links = self._get_links()

        for link in links["links"]:
            result += f"\n\n{link['type']}\n{Website(link["url"]).get_contents()}"

        return result

    def generate(self) -> str:
        return self.client.chat(self._make_generation_ai_messages()).choices[0].message.content
