from dataclasses import dataclass
from typing import List


@dataclass
class ModelBase:
    id: int
    name: str

class QueryBase(object):
    def __init__(self, models: List[ModelBase]):
        self.models = models

    class NotFoundError(Exception):
        pass

    def all(self) -> List[ModelBase]:
        return self.models

    def get(self, id: int) -> ModelBase:
        for model in self.models:
            if model.id == id:
                return model

        raise self.NotFoundError()
