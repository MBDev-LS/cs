import string


class EquationComponent():
    def __init__(self):
        pass


class Equation():
    def __init__(self, equation: str, var: str):

        self.eq = equation
        self.var = var

    def verify(self):
        chars = []
        for c in self.eq:
            if not c.isdigit() and c in string.ascii_lowercase:
                chars.append(c)
        if len(list(set(chars))) > 1:
            print(
                'This program currently only supports equations with one unknown variable')
            return False

        if self.eq.count('=') < 1:
            print("The equation must have one = sign.")
            return False
        elif self.eq.count('=') > 1:
            print("The equation must have only one = sign.")
            return False

        if len(self.eq.split('=')[0]) == 0 or len(self.eq.split('=')[0]) == 0:
        return True

    def decompose(self):
        self.left = self.eq.split('=')[0]
        self.right = self.eq.split('=')[1]
        
        if len(self.left) == 1
        for i, char in self.left()

    def __str__(self):
        return self.eq


Eq = Equation("x=1+1", 'x')
Eq.verify()
Eq.decompose()
