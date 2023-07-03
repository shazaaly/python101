class Calc:
    """
    A simple calc class
    >>> c = Calc()
    >>> c.add(3, 5)
    8
    >>> c.div(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    """
    def add(self, a, b):
        """Returns sum of 2 nums"""
        return a + b

    def div(self, a, b):
        """
        Returns div of 2 nums.
        Raises:
            ZeroDivisionError: if b is zero
        """
        if b == 0:
            raise ZeroDivisionError("division by zero")
        else:
            return a / b

    if __name__ == "__main__":
        import doctest
        doctest.testmod()
