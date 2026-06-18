from enum import Enum
from pydantic import BaseModel
from dataclasses import dataclass

class CooperationType(str, Enum):
    INFLUENCER_COLLABORATION = "INFLUENCER_COLLABORATION"
    LICENSING = "LICENSING"

class NetOrGross(str, Enum):
    NET = "NET"
    GROSS = "GROSS"

class Currency(str, Enum):
    PLN = "PLN"
    EU = "EU"

class Amount(BaseModel):
    amount : str
    currency : Currency
    net_or_gross : NetOrGross

class Address(BaseModel):
    street : str
    postcode : str
    city : str

class CompanyDetails(BaseModel):
    name : str | None = None
    nip : str | None = None
    email : str | None = None
    address : Address | None = None

class OfferData(BaseModel):
    cooperation_type : CooperationType | None = None
    amount : Amount | None = None
    company_details : CompanyDetails | None = None

@dataclass
class RawDocument():
    source_format : str
    text : str
    source_name : str