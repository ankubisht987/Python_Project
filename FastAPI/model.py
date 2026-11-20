from pydantic import BaseModel

class ProductItem(BaseModel):
    id: int
    name:str
    category:str
    description:str
    available:bool

class ProductRespone(BaseModel):
    status:str ="Success"
    count :int
    items:list[ProductItem]