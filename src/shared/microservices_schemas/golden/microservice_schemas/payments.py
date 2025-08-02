from pydantic import BaseModel

class PaymentsModel(BaseModel):
    user: str
    amount: str
