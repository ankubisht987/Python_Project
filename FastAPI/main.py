import uvicorn

from fastapi import FastAPI,  Query, HTTPException

from model import ProductItem , ProductRespone
from data import product_item

app = FastAPI(
    title="PATO API",
    description="Read Only Menu API for Web and Mobile App"
)

@app.get("/")
def read_root():
    return {"message":"Welcome To Pato.com" , "Health" : "Good"}

@app.get("/product" , response_model=ProductRespone)
def get_product(category :str | None =  Query(None, description="Filter by Pato.com, for Web and Mobile")):

    if category:
        filter = [item for item in product_item  if item["category"] == category.capitalize()]
        if not filter:
            raise HTTPException(status_code=404 , detail=f"Category which is {category} is not found in product")

        return ProductRespone(count = len(filter) , items=filter)

    return ProductRespone(count=len(product_item) , items=product_item)

@app.get("/product/{id}", response_model=ProductItem)
def get_product_id(id : int):

    left =0
    right = len(product_item) -1

    while left <= right:
        mid = left + (right - left)//2
        if product_item[mid]["id"] == id:
            return product_item[mid]
        elif product_item[mid]["id"] < id:
            left = mid + 1
        else:
            right = mid - 1
    # for item in product_item:
    #     if item["id"] == id:
    #         return item

    raise HTTPException(status_code=404 , detail=f"Id which is {id} is not found in product")


if __name__ == "__main__":
    uvicorn.run("main:app" , port=9000 , reload=True)