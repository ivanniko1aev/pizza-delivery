from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship("Order", back_populates="user") #allows us to user order.user
    
    def __repr__(self):
        return f"< User {self.username}>"
    
class Order(Base):
    
    ORDER_STATUSES = [
        ('PENDING', 'Pending'),
        ('IN-TRANSIT', 'in-transit'),
        ('DELIVERED', 'Delivered'),
    ]
    
    PIZZA_SIZES = [
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('EXTRA-LARGE', 'Extra Large'),
    ]
    #Using the ChoiceType from sqlalchemy_utils, we created a 
    #custom column with choices or attributes
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices = ORDER_STATUSES), default='PENDING') 
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="orders") #mirror of user relationship
    
    def __repr__(self):
        return f"<Order {self.id}>"
    
    
    