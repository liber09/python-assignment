from dataclasses import dataclass

#order = True enables sorting
@dataclass(order = True)
class Review():
    id: int
    person_id: int
    restaurant_id: int
    rating: int
    review_text: str