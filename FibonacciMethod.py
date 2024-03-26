from Task import Task


class FibonacciMethod:
    def __init__(self, task: Task):
        self.function_access_counter = -1
        self.task = task
        self.fibonacci_num = [1, 1]
        self.k = 0
        self.__update_fibonacci()

    def __update_fibonacci(self) -> None:
        while len(self.fibonacci_num) <= self.task.n:
            self.fibonacci_num.append(self.fibonacci_num[-1] + self.fibonacci_num[-2])

    def __lambda_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return (a + self.fibonacci_num[self.task.n - (self.k + 1) - 1] * (b - a) /
                self.fibonacci_num[self.task.n - (self.k + 1) + 1])

    def __mu_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return (a + self.fibonacci_num[self.task.n - (self.k + 1)] * (b - a) /
                self.fibonacci_num[self.task.n - (self.k + 1) + 1])

    def solve_task(self) -> tuple[float, int]:
        lmbd = self.__lambda_calc()
        mu = self.__mu_calc()

        f_lambda = self.task.calc_func(lmbd)
        f_mu = self.task.calc_func(mu)
        a_rem = self.task.a
        b_rem = self.task.b
        while self.task.eps < self.task.b - self.task.a:
            print(f"\na = {self.task.a}, b = {self.task.b}")
            print(f"lambda = {lmbd}, mu = {mu}\n")

            if self.k == self.task.n - 2:
                a_rem = self.task.a
                b_rem = self.task.b

            if self.k == self.task.n - 1:
                self.k = 1
                self.task.a = a_rem
                self.task.b = b_rem

            if f_lambda > f_mu:
                self.task.a = lmbd
                lmbd = mu
                f_lambda = f_mu
                mu = self.__mu_calc()
                f_mu = self.task.calc_func(mu)
            else:
                self.task.b = mu
                mu = lmbd
                f_mu = f_lambda
                lmbd = self.__lambda_calc()
                f_lambda = self.task.calc_func(lmbd)

        answer = self.task.calc_func((self.task.a + self.task.b) / 2)
        x = (self.task.a + self.task.b) / 2
        return answer, self.function_access_counter, x
