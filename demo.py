import dotenv
from contractforge.contracts import RawDocument
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
    raw = RawDocument(
        source_format = "docx",
        text = "Przedstawiamy ofertę stałej, comiesięsznej współpracy influencerskiej na kwotę 14 250 zł netto. Klientem jest Alior Bank SP. z O.O. ulica Olesińska 7/15 02-594 Warszawa. W razie potrzby kontaktu, adres mailwy to alior@bank.com",
        source_name = "offer.docx")
    
    offer_data = LLMExtractor().extract(raw)
    print(offer_data)

if __name__ == "__main__":
    main()