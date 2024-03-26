from Task import Task


class GoldenSectionMethod:
    def __init__(self, task: Task):
        self.function_access_counter = -1
        self.task = task

    def __lambda_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return a + (3 - 5 ** 0.5) * (b - a) / 2

    def __mu_calc(self) -> float:
        self.function_access_counter += 1
        a = self.task.a
        b = self.task.b
        return b - (3 - 5 ** 0.5) * (b - a) / 2

    def solve_task(self) -> tuple[float, int]:
        lmbd = self.__lambda_calc()
        mu = self.__mu_calc()

        f_lambda = self.task.calc_func(lmbd)
        f_mu = self.task.calc_func(mu)

        while self.task.eps < self.task.b - self.task.a:
            #
            # print(f"\na = {self.task.a}, b = {self.task.b}")
            # print(f"lambda = {lmbd}, mu = {mu}\n")
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
