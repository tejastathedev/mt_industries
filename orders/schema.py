from pydantic import BaseModel
from datetime import datetime





class Constants:
    # 'ordered', 'delivered', 'cancelled', 'returned'
    ordered = 'ordered'
    delivered = 'delivered'
    cancelled = 'cancelled'
    returned = 'returned'
    pending = 'pending'
    sucessfull = 'completed'
    failed = 'failed'




    # scheams for payment status 

    class CreatePaymentStatus(BaseModel):
        payment_id: int
        payment_status: str
        payment_status_date: datetime
        

    class PaymentStatusResponse(BaseModel):
        id: int
        payment_id: int
        timestamp: datetime

        class Config:
            orm_mode = True

    



