from FibonacciMethod import FibonacciMethod
from GoldenSectionMethod import GoldenSectionMethod
from Task import Task

if __name__ == '__main__':
    task = Task("task.txt")
    task.show()

    fib_method = FibonacciMethod(task)
    fib_answer, func_access_count, x = fib_method.solve_task()
    print("Ответ, полученный методом Фибоначчи:", fib_answer)
    print("Точка минимума:", x)
    print("Число обращений к функции:", func_access_count)

    task = Task("task.txt")
    gld_method = GoldenSectionMethod(task)
    gld_answer, func_access_count, x = gld_method.solve_task()
    print("Ответ, полученный методом золотого сечения:", gld_answer)
    print("Точка минимума:", x)
    print("Число обращений к функции:", func_access_count)







