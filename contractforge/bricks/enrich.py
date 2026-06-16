from typing import Protocol
from RegonAPI import RegonAPI
from contractforge.contracts import CompanyDetails,Address,OfferData
import logging

TEST_API_KEY = "abcde12345abcde12345"

class RegistryAdapter(Protocol):
    def enrich(self, offer_data : OfferData):...

class RegonAdapter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api = RegonAPI(bir_version="bir1.1", is_production=False)
        self.api.authenticate(key=TEST_API_KEY)

    def enrich(self, offer_data : OfferData):
        nip = offer_data.company_details.nip
        try:
            results = self.api.searchData(nip=nip)
        except Exception as e:
            self.logger.error("Error querying CompanyDetails for %s: %s", nip, e)
        else:
            if results:
                self.logger.info("Found %s results for nip number: %s in Regon API", len(results), nip)
                result = results[0]
                enriched = CompanyDetails(
                    name=result["Nazwa"],
                    nip=nip,
                    address=Address(
                        city=result["Miejscowosc"],
                        postcode=result["KodPocztowy"],
                        street=self._parse_street(result=result)
                        )
                    )
                self._enrich(offer_data=offer_data, enriched=enriched)
            else:
                self.logger.info("Found 0 results for nip number: %s in Regon API", nip)
    
    def _enrich(self, offer_data : OfferData, enriched : CompanyDetails):
        offer_data.company_details = offer_data.company_details.model_copy(update={
            "name":enriched.name,
            "address":enriched.address
        })

    def _parse_street(self, result : dict) -> str:
        street = result["Ulica"]
        if result["NrNieruchomosci"]:
            street += " " + result["NrNieruchomosci"]
        if result["NrLokalu"]:
            street += "/" + result["NrLokalu"]
        
        return street