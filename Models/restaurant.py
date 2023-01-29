from dataclasses import dataclass

@dataclass
class Restaurant():
    id: int
    name: str
    city: str
    street: str
    postalcode: str