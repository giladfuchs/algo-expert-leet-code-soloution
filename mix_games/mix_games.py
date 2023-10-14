from pydantic import BaseModel, Extra, TypeAdapter
from pydantic.fields import FieldInfo
from typing import Annotated


class BaseResponse(BaseModel, extra='allow'):
    pass


class ErrorResponse(BaseResponse):
    error_code: int
    error_msg: str= 'some error'


error_response: ErrorResponse = ErrorResponse(error_code=1, extra_field="efee")
base_response: BaseResponse = BaseResponse(extra_field="abcde")

print("Calling model_dump:")
print(error_response.model_dump(mode="json"))
print(base_response.model_dump(mode="json"))

print()

field_info: FieldInfo = FieldInfo(annotation=BaseResponse)
type_adapter: TypeAdapter = TypeAdapter(Annotated[field_info.annotation, field_info])

print("Calling type_adapter.dump_python:")
print(type_adapter.dump_python(error_response, mode="json"))
print(type_adapter.dump_python(base_response, mode="json"))