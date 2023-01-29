from dataclasses import dataclass
#order = True enables sorting
@dataclass(order = True)
class Restaurant():
    id: int
    name: str
    city: str
    street: str
    postalcode: str