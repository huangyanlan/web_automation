from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError

class  schemaDemo:

  def schema_check(self, result):
    schema = {
    "title": "test demo",
    "description": "validate result information",
    "type": "object",
    "properties": {
        "code": {
            "description": "error code",
            "type": "integer"
        },
        "msg": {
            "description": "error msg ",
            "type": "string"
        },
        "token":
        {
            "description": "login success return token",
            "maxLength": 40,
            "pattern": "^[a-f0-9]{40}$",  # 正则校验a-f0-9的16进制，总长度40
            "type": "string"
        }
    },
    "required": [
        "code", "msg", "token"
    ] }

    try:
        validate(instance=result, schema=schema, format_checker=draft7_format_checker)
    except SchemaError as e:
        return 1, "验证模式schema出错，出错位置：{}，提示信息：{}".format(" --> ".join([i for i in e.path if i]), e.message)
    except ValidationError as e:
        return 1, "不符合schema规定，出错字段：{}，提示信息：{}".format(" --> ".join([i for i in e.path if i]), e.message)
    else:
        return 0, 'success'


 # result = {
 #    "code": 0,
 #    "msg": "login success!",
 #    "token": "000038efc7edc7438d781b0775eeaa009cb64865",
 #    "username": "test"}

 # validate(instance=result, schema=schema)


