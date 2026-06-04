import dotenv
from openai import OpenAI
from contractforge.contracts import OfferData

def main() :
    dotenv.load_dotenv()
    client = OpenAI()
    response = client.responses.parse(
    model="gpt-4o-mini",
    input=[
        {"role":"system", "content":"Extract the offer information"},
        {"role":"user", "content":"Przedstawiamy ofertę stałej, comiesięsznej współpracy influencerskiej na kwotę 14 250 zł netto. Klientem jest Alior Bank SP. z O.O. ulica Olesińska 7/15 02-594 Warszawa. W razie potrzby kontaktu, adres mailwy to alior@bank.com"},
        ],
    text_format=OfferData
    )
    print(response.output_parsed)
    print(response.usage)

if __name__ == "__main__":
    main()