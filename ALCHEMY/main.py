from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import func

class Base(DeclarativeBase):
     pass

class client(Base):
     __tablename__ = "client"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     
class table(Base):
     __tablename__ = "table"

     id: Mapped[int] = mapped_column(primary_key=True)
     id_restaurant: Mapped[Optional [int]] = mapped_column(ForeignKey("rest.id"))
     id_client: Mapped[Optional [int]] = mapped_column(ForeignKey("client.id"))

class rest(Base):
     __tablename__ = "rest"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     adress: Mapped[str] = mapped_column(String)
     
class menu(Base):
     __tablename__ = "menu"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String)
     id_table: Mapped[Optional [int]] = mapped_column(ForeignKey("table.id"))
     foooood:Mapped["foooood"] = relationship(back_populates="menu")
     
class order(Base):
     __tablename__ = "order"

     id: Mapped[int] = mapped_column(primary_key=True)
     total_price: Mapped[int] = mapped_column()
     data:Mapped[int]= mapped_column()
     name: Mapped[str] = mapped_column(String)
     id_client: Mapped[Optional [int]] = mapped_column(ForeignKey("client.id")) 
     
class foooood(Base):
     __tablename__ = "food"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String)
     service_size: Mapped[int] = mapped_column()
     price: Mapped[int] = mapped_column()
     id_menu: Mapped [Optional [int]] = mapped_column(ForeignKey("menu.id"))
     menu:Mapped["menu"] = relationship(back_populates="foooood")
     id_order: Mapped[Optional [int]] = mapped_column(ForeignKey("order.id"))
              
              
class employee(Base):
     __tablename__ = "employee"

     id: Mapped[int] = mapped_column(primary_key=True)
     first_name: Mapped[str] = mapped_column(String)
     last_name: Mapped[str] = mapped_column(String)
     age: Mapped[int] = mapped_column()
     post: Mapped[str] = mapped_column(String)
    
     id_rest: Mapped[Optional [int]] = mapped_column(ForeignKey("rest.id"))
     id_order: Mapped[Optional [int]] = mapped_column(ForeignKey("order.id"))  
     
class post(Base):
     __tablename__ = "post"

     id: Mapped[int] = mapped_column(primary_key=True)
     title: Mapped[str] = mapped_column(String)
     payroll: Mapped[int] = mapped_column()
     function: Mapped[str] = mapped_column(String)
     id_employee: Mapped[Optional [int]] = mapped_column(ForeignKey("employee.id"))
                      
 ####################################
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:100100@localhost:5432/R",echo = True) 

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

####################################
from sqlalchemy.orm import Session
with Session(engine) as session:
     
    spongebob = rest(name="spongebob", adress="Arbat 98,24")
    sandy = rest(name="sandy",adress="Sosna 1,999")
    patrick = rest(name="patrick",adress="Meow 234534,22" )
    #
    Galkov = client(name="Galkov")
    Petykhov = client(name="Petykhov")
    Makedonskiy = client(name="Makedonskiy")
    Pavlov = client(name="Pavlov")
    #
    Tomato_cyp = foooood(name="Tomato_cyp",service_size="100",price="2000")
    Thezar = foooood(name='Thezar',service_size='300',price='4000')
    Borch = foooood(name='Borch',service_size='200',price='500')
    #
    
    
    session.add_all([spongebob, sandy, patrick,Galkov,Petykhov,Makedonskiy,Pavlov,Tomato_cyp,Thezar,Borch])
    session.commit()
    
    
    
    
    
from sqlalchemy import select
from sqlalchemy.orm import joinedload

st = select(client).options(joinedload(client.name))
print()
print(st)

st = select(rest).where(rest.id == 1)

result = session.execute(st).unique().fetchall()

print()
print("выполнение запроса")
#for i in result:
#print(i)
#print(client.name)


#stm = select(foooood.price,func.count(foooood.id)).join(order).group_by(order.total_price)


