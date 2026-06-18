import logging
from contractforge.bricks.ingest import Parser
from contractforge.bricks.extract import LLMExtractor
from contractforge.bricks.enrich import RegistryAdapter
from contractforge.bricks.resolve import Resolver

class ContractPipeline:

    def __init__(self, parser : Parser, extractor : LLMExtractor, enricher : RegistryAdapter, resolver : Resolver):
        self.logger = logging.getLogger(__name__)
        self.parser = parser
        self.extractor = extractor
        self.enricher = enricher
        self.resolver = resolver

    def run(self, path : str):
        raw = self.parser.parse(path=path)
        if raw:
            offer_data = self.extractor.extract(raw=raw)
            if(offer_data and offer_data.company_details and offer_data.company_details.nip):
                self.enricher.enrich(offer_data=offer_data)
                print(offer_data)
            if(offer_data and offer_data.cooperation_type):
                self.resolver.resolve(cooperation_type=offer_data.cooperation_type)