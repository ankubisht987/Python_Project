from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFoundError(Exception):
    def __init__(self, pin_code:str):
        self.pin_code = pin_code

class InvalidPincodeError(Exception):
    def __init__(self, pin_code:str, reason="Invalid Format"):
        self.pin_code = pin_code
        self.reason = reason

# Custom Handler

async def pincode_not_found_handler(request: Request, exc:PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Pin Code Not Found",
            "message": f"No Loaction for Pin Code: '{exc.pin_code}' ",
            "pincode": exc.pin_code
        }
    )
async def pincode_is_Invalid(request: Request, exc:InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Pin Code is Invalid",
            "message": f"Please Enter the Correct pin Code this Pin Code '{exc.pin_code}' is not Valid!!!",
            "pincode": exc.pin_code
        }
    )
