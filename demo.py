import dotenv
import logging
from contractforge.configuration.config import AppConfig
from contractforge.bricks.ingest import DocxParser
from contractforge.bricks.extract import OpenAIExtractor
from contractforge.bricks.enrich import RegonAdapter

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("log_file.log"),
            logging.StreamHandler(),
        ],
    )

def main() :
    dotenv.load_dotenv()
    setup_logging()
    config = AppConfig()

   
if __name__ == "__main__":
    main()