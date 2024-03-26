import numpy as np
import matplotlib.pyplot as plt


def isnum(string: str) -> bool:
    try:
        float(string)
        return True
    except Exception:
        return False


class Task:
    def __init__(self, filename: str):
        self.operations = None
        self.nums = None

        with open(filename, "r") as file:
            lines = file.readlines()

            for line in lines:
                ln = line.rstrip().split(' ')
                command = ln[0]
                if command == "func":
                    self.__load_func(ln)
                elif command == "eps":
                    self.__load_eps(ln)
                elif command == "interval":
                    self.__load_interval(ln)
                elif command == "n":
                    self.__load_fib_count(ln)

        self.operation_priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}

    def __load_func(self, line):
        func = line
        del func[0]
        func = "".join(func)
        self.function = []
        operation = ''
        for i in func:
            if i in '()+-*/':
                if operation != '':
                    self.function.append(operation)
                self.function.append(i)
                operation = ''
            elif i == 'x':
                if operation != '':
                    self.function.append(operation)
                self.function.append(i)
                operation = ''
            else:
                operation += i
        if operation != '':
            self.function.append(operation)

    def calc_func(self, x: float):
        self.nums = []
        self.operations = []

        for i in self.function:
            if i == 'x':
                self.nums.append(x)
            elif isnum(i):
                self.nums.append(float(i))
            elif i == ')':
                while self.operations[-1] != '(':
                    self.__calc_operation()
                self.operations.pop()
            elif i not in '+-*/^':
                self.operations.append(i)  # sin, cos и тд
            else:
                while (len(self.operations) > 0 and (self.operations[-1] not in '(+-*/^'
                       or self.operation_priority[self.operations[-1]] > self.operation_priority[i])):
                    self.__calc_operation()
                self.operations.append(i)

        while len(self.operations) > 0:
            self.__calc_operation()

        return self.nums[0]

    def __calc_operation(self):
        operation = self.operations[-1]
        self.operations.pop()
        if operation in '+-*/^':
            a = self.nums[-1]
            b = self.nums[-2]
            self.nums.pop()
            self.nums.pop()
            if operation == '+':
                self.nums.append(a + b)
            elif operation == '-':
                self.nums.append(b - a)
            elif operation == '*':
                self.nums.append(a * b)
            elif operation == '/':
                self.nums.append(b / a)
            elif operation == '^':
                self.nums.append(b ** a)
        else:
            a = self.nums[-1]
            self.nums.pop()
            if operation == 'sin':
                self.nums.append(np.sin(a))
            elif operation == 'cos':
                self.nums.append(np.cos(a))
            elif operation == 'tg':
                self.nums.append(np.tan(a))
            elif operation == 'ctg':
                self.nums.append(1 / np.tan(a))
            elif operation == 'sqrt':
                self.nums.append(a ** 0.5)

    def __load_eps(self, line):
        self.eps = float(line[1])

    def __load_interval(self, line):
        self.a = float(line[1])
        self.b = float(line[2])

    def show(self):
        x = np.linspace(self.a, self.b, 100)
        y = [self.calc_func(i) for i in x]
        plt.plot(x, y)
        plt.show()

    def __load_fib_count(self, ln):
        self.n = int(ln[1])
