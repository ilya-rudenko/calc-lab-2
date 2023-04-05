def f(x):
    return x ** 3 - 3.78 * x ** 2 + 1.25 * x + 3.49


def df(x):
    return 3 * x ** 2 - 7.56 * x + 1.25


flag = "right"

if flag == "left":
    def xk_next(x):
        return x - f(x) / df(x)


    xk = -0.750

    print("xk: ", xk)
    print("f(x): ", f(xk))
    print("df(x): ", df(xk))
    print("xk_next: ", xk_next(xk))
    print("delta: ", abs(xk_next(xk) - xk))

if flag == "center":
    a = 1.569
    b = 1.577

    x = (a + b) / 2

    print("a: ", a)
    print("b: ", b)
    print("x: ", x)
    print("f(a): ", f(a))
    print("f(b): ", f(b))
    print("f(x): ", f(x))
    print("delta: ", abs(a - b))

if flag == "right":

    lyambda = -1/11.54

    def fi(x):
        return x + lyambda*f(x)
    def dfi(x):
        return 1 + lyambda*df(x)


    xk = 2.939

    print("xk: ", xk)
    print("xk_next: ", fi(xk))
    print("fi(xk_next): ", fi(fi(xk)))
    print("f(xk_next): ", f(fi(xk)))
    print("delta: ", abs(fi(xk) - xk))
