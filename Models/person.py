from dataclasses import dataclass
#order = True enables sorting
@dataclass(order = True)
class Person():
    id: int
    first_name: str
    last_name: str
    born: str
    city: str
    gender: str

