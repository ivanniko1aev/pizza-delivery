from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]
    
    
    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                'username': 'Johndoe',
                'email': 'johndoe@me.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
            
        }
        
class Settings(BaseModel):
    authjwt_secret_key: str = '207c63ad6f9a1e5325e4ba057235af677eaa06a96e271aea66eb18e339bb7460'
    
class LoginModel(BaseModel):
    username: str
    password: str
    
""" class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = 'PENDING'
    pizza_size: Optional[str] = 'SMALL'
    user_id: Optional[int]
    
    class Config:
        orm_mode = True
        schema_extra = {
            'examples':{
                'quantity': 1,
                'pizza_size': 'SMALL', 
            }
            
        } """
        
class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = 'PENDING'
    pizza_size: Optional[str] = 'SMALL'
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            'examples': [
                {
                    'quantity': 1,
                    'order_status': 'PENDING',
                    'pizza_size': 'SMALL',
                    'user_id': 1
                }
            ]
        }