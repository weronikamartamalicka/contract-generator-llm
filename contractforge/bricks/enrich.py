from typing import Protocol
from RegonAPI import RegonAPI
from contractforge.contracts import CompanyDetails,Address
from contractforge.bricks.extract import OfferData
import logging

TEST_API_KEY = "abcde12345abcde12345"

class RegistryAdapter(Protocol):
    def enrich(self, nip : str) -> CompanyDetails | None:...

class RegonAdapter:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api = RegonAPI(bir_version="bir1.1", is_production=False)
        self.api.authenticate(key=TEST_API_KEY)

    def enrich(self, nip : str) -> CompanyDetails | None:
        try:
            results = self.api.searchData(nip=nip)
        except Exception as e:
            self.logger.error("Error querying CompanyDetails for %s: %s", nip, e)
            return None
        else:
            if results:
                self.logger.info("Found %s results for nip number: %s in Regon API", len(results), nip)
                result = results[0]
                return CompanyDetails(
                    name=result["Nazwa"],
                    nip=nip,
                    address=Address(
                        city=result["Miejscowosc"],
                        postcode=result["KodPocztowy"],
                        street=self._parse_street(result=result)
                        )
                    )
            else:
                self.logger.info("Found 0 results for nip number: %s in Regon API", nip)
                return None
            
    def _parse_street(self, result : dict) -> str:
        street = result["Ulica"]
        if result["NrNieruchomosci"]:
            street += " " + result["NrNieruchomosci"]
        if result["NrLokalu"]:
            street += "/" + result["NrLokalu"]
        
        return street