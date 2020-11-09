from enum import Enum


class MoveStatus(Enum):
    ERR_COLLIDE = -6  # Move collides with a piece
    ERR_WAIT_TURN = -5  # Wait for your turn
    ERR_FF = -4  # Friendly fire
    ERR_MOVE_ILLEGAL = -3  # Not a legal move based on piece's special movement
    ERR_SELF_PWN = -2  # Are you trying to pwn yourself?
    ERR_OOB = -1  # You have unbounded yourself from the positive numbers!
    ERR_ENOENT = 0  # There's nobody in there! ZERO!
    OK_MOVE = 1  # Normal move
    OK_KILL = 2  # Move and kill
