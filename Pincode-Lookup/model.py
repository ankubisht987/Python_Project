from pydantic import BaseModel, field_validator

class PincodeRequest(BaseModel):
    pincode : str

    # pincode must be Exactly 6 Digit
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode Must Be exacty 6 Digit")
        return value

class LocationResponse(BaseModel):
    pincode:str
    city: str | None =None
    state: str |None =None
    district:str | None =None

class BulkRequest(BaseModel):
    pincodes : list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincode(cls, values):
        if len(values) == 0:
            raise ValueError("At Least one pincode is Required")
        
        if len(values) >20:
            raise ValueError("Maximum 20 pincode are allowed per request")
        for data in values:
            if len(data) != 6 or not data.isdigit():
                raise ValueError("Pincode Must Be exacty 6 Digit")
        return values

class BulkResponse(BaseModel):
    status:str = "Success"
    found : int
    not_found:int
    result: list[LocationResponse]
    missing:list[str]
    # invalid:list[str]
