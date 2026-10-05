from pydantic import BaseModel

class PlayerCreate(BaseModel): 
    first_name: str
    last_name: str
    phone_number: str
    password: str

class SessionCreate(BaseModel): 
    date: str
    time: str 
    location: str 
    pitch_cost: float

class RSVPCreate(BaseModel): 
    player_id: int
    session_id: int
    is_coming: bool

class PaymentCreate(BaseModel): 
    player_id: int
    session_id: int

class LoginRequest(BaseModel): 
    phone_number: str
    password: str