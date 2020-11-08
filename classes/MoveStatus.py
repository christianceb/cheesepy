from enum import Enum


class MoveStatus(Enum):
    ERR_MOVE_ILLEGAL = -3  # Not a legal move based on piece's special movement
    ERR_SELF_PWN = -2  # Are you trying to pwn yourself?
    ERR_OOB = -1  # You have unbounded yourself from the positive numbers!
    ERR_ENOENT = 0  # There's nobody in there! ZERO!
    OK_MOVE = 1  # Very normal move, cool
    OK_KILL = 2  # Move and kill
