from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError
from Service.Schema_check import schemaDemo

def test_schema():
 result = {
    "code": 0,
    "msg": "login success!",
    "token": "000038efc7edc7438d781b0775eeaa009cb64865",
    "username": "test"}

 result1 = schemaDemo().schema_check(result)
 print(result1)
 assert 0 in result1





