from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User, Order
from schemas import OrderModel
from database import Session, engine
from fastapi.encoders import jsonable_encoder

order_router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

session = Session(bind=engine)
@order_router.get("/")
async def hello(Authorize: AuthJWT = Depends()):
    
    try:
        Authorize.jwt_required() #Json Web Token Authentication
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    return {"message": "Hello World"}


@order_router.post("/order", status_code=201)
async def place_an_order(order: OrderModel, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required() #Json Web Token Authentication
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    #Defining current user based on the JWT
    current_user = Authorize.get_jwt_subject() 
    
    #Querying the user from the database
    user = session.query(User).filter(User.username == current_user).first()
    
    new_order = Order(
        quantity = order.quantity,
        pizza_size = order.pizza_size,
    )
    
    new_order.user = user
    
    session.add(new_order)
    
    session.commit()
    
    response= {
        "pizza_sizze": new_order.pizza_size,
        "quantity": new_order.quantity,
        "id": new_order.id,
        "order_status": new_order.order_status
        
    }
    
    return jsonable_encoder(response)
    
    
@order_router.get("/orders")
async def get_orders(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required() #Json Web Token Authentication
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    current_user = Authorize.get_jwt_subject() 
    
    user = session.query(User).filter(User.username == current_user).first()
    
    if user.is_staff:
        
        orders = session.query(Order).all()
        
        return jsonable_encoder(orders)
    
    raise HTTPException(status_code=401, detail="You are not authorized")


@order_router.get("/orders/{order_id}")
async def get_order(order_id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required() #Json Web Token Authentication
        
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
    current_user = Authorize.get_jwt_subject() 
    
    user = session.query(User).filter(User.username == current_user).first()
    
    if user.is_staff:
        
        order = session.query(Order).filter(Order.id == order_id).first()
        
        return jsonable_encoder(order)
    
    raise HTTPException(status_code=401, detail="You are not authorized")
    