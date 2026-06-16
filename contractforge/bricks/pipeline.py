import logging
from contractforge.bricks.ingest import Parser
from contractforge.bricks.extract import LLMExtractor
from contractforge.bricks.enrich import RegistryAdapter

class ContractPipeline:

    def __init__(self, parser : Parser, extractor : LLMExtractor, enricher : RegistryAdapter):
        self.logger = logging.getLogger(__name__)
        self.parser = parser
        self.extractor = extractor
        self.enricher = enricher

    def run(self, path : str):
        raw = self.parser.parse(path=path)
        if raw:
            offer_data = self.extractor.extract(raw=raw)
            if(offer_data and offer_data.company_details.nip):
                self.enricher.enrich(offer_data=offer_data)