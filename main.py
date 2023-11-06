# def outer():
#     x = "local"
#     def inner():
#         # nonlocal x  # Khai báo x là nonlocal
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
#
# outer()


def fn(*p, **kw):
    print(p)
    print(kw)

fn(1,2,3,4, a = 1, b = 2, c = 3)