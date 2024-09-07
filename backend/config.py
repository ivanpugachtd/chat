from pydantic import BaseModel
from typing import TypeVar, Type
from dotenv import load_dotenv
from src.utils.env import value_or_error

load_dotenv()


class Config(BaseModel):
    STAGE: str
    PORT: int

T = TypeVar("T", bound=BaseModel)


def parse_env(env_class: Type[T]) -> T:
    values = {}
    for field_name, field_type in env_class.__annotations__.items():
        value = value_or_error(field_name)
        values[field_name] = value

    return env_class.model_validate(values)
