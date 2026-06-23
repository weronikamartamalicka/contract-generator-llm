import dotenv
import logging
import yaml

from contractforge.bricks.build import PipelineBuilder

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("log_file.log"),
            logging.StreamHandler(),
        ],
        force=True
    )

def main() :
    dotenv.load_dotenv()
    setup_logging()
    try:
        with open("contractforge/configuration/configuration.yaml", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        contract_pipeline = PipelineBuilder().build_pipeline(config=config)
        contract_pipeline.run("test.docx")
    except Exception as e:
        return
    

if __name__ == "__main__":
    main()