from dataclasses import dataclass

@dataclass
class Review():
    id: int
    person_id: int
    restaurant_id: int
    rating: int
    review_text: str