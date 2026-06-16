import dotenv
import logging
from RegonAPI import RegonAPI
from contractforge.bricks.ingest import DocxParser
from contractforge.bricks.extract import LLMExtractor
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

    extractor = LLMExtractor()
    enricher = RegonAdapter()
    
    raw = DocxParser().parse("test.docx")
    if raw is None:
        logging.error("Failed to parse docx file")
        return
    
    offer_data = extractor.extract(raw)
    if offer_data is None:
        logging.error("There is no offer data parsed from document")
        return
    
    if(offer_data.company_details.nip):
        enricher.enrich(offer_data=offer_data)
    else:
       logging.error("There is no nip")
       
    print(offer_data)
   
if __name__ == "__main__":
    main()