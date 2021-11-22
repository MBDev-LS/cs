import string

OPERATORS = "+-"

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
            print("The must be at least one character on each side of the '=' sign.")
            return False

        return True

    def decompose(self):
        self.left = self.eq.split('=')[0]
        self.left_decomposed = []
        self.right = self.eq.split('=')[1]
        self.right_decomposed = []

        actual_count = 0

        for i, char in enumerate(self.left): # Repeated code is a product of early testing, real version will store 'left' and 'right' in a list and iterate through it.
            if not i < actual_count:
                
                if char in OPERATORS:
                    self.left_decomposed.append(char)
                elif char.isdigit():
                    num = char
                    c = 1
                    if len(self.left)-1 >= i+c:
                        while True and len(self.left)-1 >= i+c:
                            # print(i+c, self.left)
                            if self.left[i+c].isdigit() or self.left[i+c] == self.var:
                                num += self.left[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.left_decomposed.append(num)
                elif char == self.var:
                    num = char
                    c = 1
                    if len(self.left)-1 >= i+c:
                        while True and len(self.left)-1 >= i+c:
                            # print(i+c, self.left)
                            if self.left[i+c].isdigit() or self.left[i+c] == self.var:
                                num += self.left[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.left_decomposed.append(num)

                
                actual_count += 1


        actual_count = 0
        for i, char in enumerate(self.right):
            if not i < actual_count:
                
                if char in OPERATORS:
                    self.right_decomposed.append(char)
                elif char.isdigit():
                    num = char
                    c = 1
                    if len(self.left)-1 >= i+c:
                        while True and len(self.right)-1 >= i+c:
                            # print(i+c, self.right)
                            if self.right[i+c].isdigit() or self.right[i+c] == self.var:
                                num += self.right[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.right_decomposed.append(num)
                elif char == self.var:
                    num = char
                    c = 1
                    if len(self.right)-1 >= i+c:
                        while True and len(self.right)-1 >= i+c:
                            # print(i+c, self.right)
                            if self.right[i+c].isdigit() or self.right[i+c] == self.var:
                                num += self.right[i+c]
                            else:
                                break
                            c += 1
                        actual_count = i + (c - 1)
                    self.right_decomposed.append(num)

                
                actual_count += 1
        
        print(self.left_decomposed, self.right_decomposed)


    def __str__(self):
        return self.eq


Eq = Equation("x=1+-11", 'x')
Eq.verify()
Eq.decompose()
