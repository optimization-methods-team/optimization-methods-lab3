import numpy as np
import matplotlib.pyplot as plt


class Task:
    def __init__(self, filename: str):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                ln = line.split(' ')
                command = ln[0]
                if command == "func":
                    self.__load_func(ln)
                elif command == "eps":
                    self.__load_eps(ln)
                elif command == "interval":
                    self.__load_interval(ln)

    def __load_func(self, line):
        self.function = []
        for i in range(1, len(line)):
            self.function.append(float(line[i]))

    def __load_eps(self, line):
        self.eps = float(line[1])

    def __load_interval(self, line):
        self.a = float(line[1])
        self.b = float(line[2])

    def show(self):
        curve = np.array(self.function)
        x = np.linspace(self.a, self.b, 100)
        y = [np.polyval(curve, i) for i in x]
        plt.plot(x, y)
        plt.show()
