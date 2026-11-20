from fastapi import FastAPI
from contextlib import asynccontextmanager
from exceptions import (
    PinCodeNotFoundError,
    InvalidPincodeError,
    pincode_is_Invalid,
    pincode_not_found_handler
)
from model import(
    LocationResponse, 
    BulkResponse,
    BulkRequest
)
from data import understand_query

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting the Application")
    yield
    print("Ending the Application")


app = FastAPI(
    title="Pincode lookUp API",
    description="Auto fill city and State From Indian Pincode during checkout",
    lifespan=lifespan
)

# Register our Own Custom Exception Handler
app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPincodeError, pincode_is_Invalid)


@app.get("/")
def home():
    return {
        "message" :"pin Code Lookup API",
    }

@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup_pincode(code:str):
    if len(code) !=6 or not code.isdigit():
        raise InvalidPincodeError(code, "Must be exactly 6 Digit!!!")

    result = understand_query(f"Find the city, state and district for Pin Code: {code}")
    return result

# @app.post("/pincode/bulk" , response_model=BulkResponse)
# def bulk_lookup(request: BulkRequest):
#     result = []
#     missing= []
#     # invalid= []
#     # for code in request.pincodes:
#     #     # if len(code) !=6 or not code.isdigit():
#     #     #     invalid.append(code)
#     #     #     continue

#     #     if code in pincode_db:
#     #         result.append(pincode_db[code])
#     #     else:
#     #         missing.append(code)

#     return BulkResponse(
#         found= len(result),
#         not_found=len(missing),
#         result=result,
#         missing=missing,
#     )
