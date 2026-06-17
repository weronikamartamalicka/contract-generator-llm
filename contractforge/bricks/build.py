from contractforge.bricks.pipeline import ContractPipeline
from contractforge.bricks.ingest import DocxParser
from contractforge.bricks.extract import OpenAIExtractor
from contractforge.bricks.enrich import RegonAdapter

PARSERS = {"docx" : DocxParser}
EXTRACTORS = {"openai" : OpenAIExtractor}
ENRICHERS = {"regon" : RegonAdapter}

class PipelineBuilder:

    def build_pipeline(self, config : dict) -> ContractPipeline:
        parser = PARSERS[config["parser"]]
        extractor = EXTRACTORS[config["llm"]["provider"]]
        enricher = ENRICHERS[config["registry"]]

        return ContractPipeline(
            parser=parser(),
            extractor=extractor(config["llm"]["model"]),
            enricher=enricher()
        )
