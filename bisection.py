class Bisection:
    def __init__(self, a, b, df) -> None:
        self.a = a
        self.b = b
        self.df = df
    
    def iterate(self, itr):
        a = self.a
        b = self.b
        func = self.df
        for i in range(itr):
            c = (a + b) / 2
            if func(c) == 0:
                return c
            if func(a) * func(c) < 0:
                b = c
            elif func(b) * func(c) < 0:
                a = c
        return (a + b) / 2

class test_functions:
    def x_squared(x):
        return x * x
    
    def two_x(x):
        return 2 * x

    def two(x):
        return 2
    
if __name__ == '__main__':
    bi = Bisection(-5, 15, test_functions.two_x)
    print(bi.iterate(10))