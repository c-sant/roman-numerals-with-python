from .utils import roman_to_int, int_to_roman
from typing import Type, Union

class Roman:
    """
    Roman representation of an integer.
    """

    def __init__(self, value: Union[int, str]):
        if type(value) in (int, float):
            value = int(value)
        
        if type(value) == int and value > 0:
            self._int_value = value
            self._roman_value = int_to_roman(value)

        elif type(value) == int and value <= 0:
            raise ValueError("there's no Roman equivalent to 0 or negative numbers")

        elif type(value) == str:
            self._roman_value = value
            self._int_value = roman_to_int(value)

        else:
            raise TypeError("value must be int or a Roman numeral ('str')")      

    def __int__(self):
        return self._int_value

    def __str__(self):
        return self._roman_value

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        return int(self) == int(other)

    def __lt__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"'<' not supported between instances of 'Roman' and '{type(other).__name__}'")
        
        return int(self) < int(other)

    def __le__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"'<=' not supported between instances of 'Roman' and '{type(other).__name__}'")
        
        return int(self) <= int(other)

    def __add__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"unsupported operand type(s) for +: 'Roman' and '{type(other).__name__}'")

        return Roman(int(self) + int(other))

    def __sub__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"unsupported operand type(s) for -: 'Roman' and '{type(other).__name__}'")

        return Roman(int(self) - int(other))
    
    def __mul__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"unsupported operand type(s) for *: 'Roman' and '{type(other).__name__}'")

        return Roman(int(self) * int(other))
    
    def __truediv__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"unsupported operand type(s) for /: 'Roman' and '{type(other).__name__}'")

        return Roman(int(self) / int(other))
    
    def __floordiv__(self, other):
        if type(other) not in [int, Roman]:
            raise TypeError(f"unsupported operand type(s) for /: 'Roman' and '{type(other).__name__}'")

        return Roman(int(self) / int(other))