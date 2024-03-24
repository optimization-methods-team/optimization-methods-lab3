from Task import Task


class FibonacciMethod:
    def __init__(self, task: Task):
        self.function_access_counter = 0
        self.task = task
        self.fibonacci_num = [1, 1, 2]

    def __update_fibonacci(self) -> None:
        self.fibonacci_num.append(self.fibonacci_num[1] + self.fibonacci_num[2])
        del self.fibonacci_num[0]

    def __lambda_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return a + self.fibonacci_num[0] * (b - a) / self.fibonacci_num[2]

    def __mu_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return a + self.fibonacci_num[1] * (b - a) / self.fibonacci_num[2]

    def __calc_func(self, x: float) -> float:
        func = 0
        st = len(self.task.function) - 1
        for k in self.task.function:
            func += x ** st * k
            st -= 1
        return func

    def solve_task(self) -> tuple[float, int]:
        lmbd = self.__lambda_calc()
        mu = self.__mu_calc()

        f_lambda = self.__calc_func(lmbd)
        f_mu = self.__calc_func(mu)

        while self.task.eps < self.task.b - self.task.a:
            print(f"\na = {self.task.a}, b = {self.task.b}")
            print(f"lambda = {lmbd}, mu = {mu}\n")

            if f_lambda > f_mu:
                self.task.a = lmbd
                lmbd = mu
                f_lambda = f_mu
                mu = self.__mu_calc()
                f_mu = self.__calc_func(mu)
            else:
                self.task.b = mu
                mu = lmbd
                f_mu = f_lambda
                lmbd = self.__lambda_calc()
                f_lambda = self.__calc_func(lmbd)

            self.__update_fibonacci()

        answer = self.__calc_func((self.task.a + self.task.b) / 2)
        return answer, self.function_access_counter
