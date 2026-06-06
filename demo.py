import dotenv
from contractforge.bricks.ingest import DocxParser
from contractforge.bricks.extract import LLMExtractor
import logging

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
    raw = DocxParser().parse("test.docx")
    if raw is None:
        logging.error("Failed to parse docx file")
        return
    offer_data = LLMExtractor().extract(raw)
    print(offer_data)

if __name__ == "__main__":
    main()