from dataclasses import dataclass

@dataclass
class Person():
    id: int
    first_name: str
    last_name: str
    born: str
    city: str
    gender: str

