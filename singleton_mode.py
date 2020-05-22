# 绑定类变量
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class SingleClass(Singleton):
#     a = 1
#
#
# one = SingleClass()
# two = SingleClass()
#
# print(id(one))
# print(id(two))
# print(one is two)
# one.a = 2
# print(two.a)


# 共享属性
# class Singleton(object):
#     _state = {}
#
#     def __new__(cls, *args, **kwargs):
#         obj = super().__new__(cls, *args, **kwargs)
#         obj.__dict__ = cls._state
#         return obj
#
#
# class SingleClass(Singleton):
#     a = 1
#
#
# one = SingleClass()
# two = SingleClass()
#
# print(id(one))
# print(id(two))
# one.a = 2
# print(two.a)
# print(id(one.__dict__))
# print(id(two.__dict__))


# 装饰器
def singleton(cls, *args, **kwargs):
    instance = {}

    def getinstance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getinstance


@singleton
class SingleClass(object):
    def __init__(self):
        self.a = 1


one = SingleClass()
two = SingleClass()

print(id(one))
print(id(two))
print(one is two)
one.a = 2
print(two.a)
