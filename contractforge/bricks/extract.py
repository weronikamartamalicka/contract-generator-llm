from openai import OpenAI
from contractforge.contracts import OfferData, RawDocument
import logging

class LLMExtractor:
    def __init__(self):
        self.client = OpenAI()
        self.logger = logging.getLogger(__name__)
    
    def extract(self, raw : RawDocument) -> OfferData | None:
        self.logger.info("Extracting offer data from raw document %s", raw.source_name)
        try:
            response = self.client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {"role": "system", "content": "Extract the offer information"},
                {"role": "user", "content": raw.text},
            ],
            text_format=OfferData
            )
        except Exception as e:
            self.logger.error("Error extracting offer data %s: %s", raw.source_name, e)
            return None
        else:
            return response.output_parsed