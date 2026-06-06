from openai import OpenAI
from contractforge.contracts import OfferData, RawDocument

class LLMExtractor:
    def __init__(self) -> None:
        self.client = OpenAI()
    
    def extract(self, raw : RawDocument) -> OfferData | None:
        response = self.client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "Extract the offer information"},
                {"role": "user", "content": raw.text},
            ],
            text_format=OfferData
            )
        return response.output_parsed
    