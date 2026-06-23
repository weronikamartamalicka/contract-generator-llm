from contractforge.contracts import CooperationType
from typing import Protocol
from pathlib import Path
import yaml
import logging

class Resolver(Protocol):
    def resolve(self, cooperation_type : CooperationType):...

class TermsResolver:
    def __init__(self, partner : str):
        self.logger = logging.getLogger(__name__)
        self.partner = partner

    def resolve(self, cooperation_type : CooperationType):
        self.logger.info("Starting to open partner terms configuration for: %s", self.partner)
        path = Path("tenants", self.partner, "configuration.yaml")
        try:
            with open(path, encoding="utf-8") as f:
                configuration = yaml.safe_load(f)
                resolved = configuration[cooperation_type.value]
            print(resolved)
        except Exception as e:
            self.logger.error("Error retrievening terms in configuration file %s: %s", path, e)
