from enum import Enum
from pydantic import BaseModel
from decimal import Decimal

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
    name : str
    nip : str | None = None
    email : str
    address : Address


class OfferData(BaseModel):
    cooperation_type : CooperationType
    amount : Amount
    company_details : CompanyDetails