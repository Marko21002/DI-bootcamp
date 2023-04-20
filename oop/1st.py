class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return '{} {}'.format(self.amount, self.currency)

    def __int__(self):
        return self.amount

    def __repr__(self):
        return '{} {}'.format(self.amount, self.currency)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError('Cannot add between Currency type <{}> and <{}>'.format(
                    self.currency, other.currency))
        else:
            raise TypeError(
                'Unsupported operand type(s) for +: {} and {}'.format(type(self), type(other)))

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError('Cannot add between Currency type <{}> and <{}>'.format(
                    self.currency, other.currency))
        else:
            raise TypeError(
                'Unsupported operand type(s) for +=: {} and {}'.format(type(self), type(other)))
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1)  # '5 dollars'
print(int(c1))  # 5
print(repr(c1))  # '5 dollars'
print(int(c1 + 5))  # 10
print(int(c1 + c2))  # 15
print(c1)  # '5 dollars'
c1 += 5
print(c1)  # '10 dollars'
c1 += c2
print(c1)  # '20 dollars'
try:
    c1 + c3
except TypeError as e:
    print(e)  # 'Cannot add between Currency type <dollar> and <shekel>'
