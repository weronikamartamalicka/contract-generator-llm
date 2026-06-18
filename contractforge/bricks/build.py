from contractforge.bricks.pipeline import ContractPipeline
from contractforge.bricks.ingest import DocxParser
from contractforge.bricks.extract import OpenAIExtractor
from contractforge.bricks.enrich import RegonAdapter
from contractforge.bricks.resolve import TermsResolver

import logging

PARSERS = {"docx" : DocxParser}
EXTRACTORS = {"openai" : OpenAIExtractor}
ENRICHERS = {"regon" : RegonAdapter}
RESOLVERS = {"termsresolver" : TermsResolver}

class PipelineBuilder:

    def build_pipeline(self, config : dict) -> ContractPipeline:
        self.logger = logging.getLogger(__name__)
        parser = PARSERS[config["parser"]]
        extractor = EXTRACTORS[config["llm"]["provider"]]
        enricher = ENRICHERS[config["registry"]]
        resolver = RESOLVERS[config["resolver"]]
        self.logger.info("Successfuly parsed bean configuration")

        return ContractPipeline(
            parser=parser(),
            extractor=extractor(config["llm"]["model"]),
            enricher=enricher(),
            resolver=resolver(config["partner"])
        )
