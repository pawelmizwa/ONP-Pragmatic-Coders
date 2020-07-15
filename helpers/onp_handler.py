from helpers.logger import log
import logging
from typing import List

logger = logging.getLogger("example")


class ONP_PHRASE_ERROR(Exception):
    pass


class ONPHandler:
    def __init__(self, digits: tuple, operations: dict):
        self.digits = digits
        self.operations = operations

    @log()
    def operation_handler(self, x: List[str], operation: str) -> float:
        result = float(x[0])
        op = self.operations.get(operation, None)
        for i in x[1:]:
            result = op(result, float(i))

        return result

    @log()
    def onp(self, phrase: str):
        result = list()
        for i in phrase.split(' '):
            if i in self.digits:
                result.append(i)
            elif i in self.operations.keys():
                result = [self.operation_handler(x=result, operation=i)]
            elif i == "~":
                result[-1] = float(result[-1]) * -1

        return result[0]

    @log()
    def validate_onp(self, phrase: str) -> bool:
        result = True
        prev_val = ""
        for i in phrase.split(' '):
            if not (i in self.digits or i in self.operations.keys()):
                raise ONP_PHRASE_ERROR("Please make sure you are providing digits and operators only")
            if i in self.operations.keys() and prev_val in self.operations.keys():
                raise ONP_PHRASE_ERROR("There is more than 1 operator in a row")

        return result
