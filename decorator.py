# This Python file uses the following encoding: utf-8


# what is a decorator ?

def log(func):
    '''

    :param func:
    :return:
     注意这里的*args代表没有名字的参数
     **kwargs代表有名字的参数
    '''
    def wrapper(*args, **kwargs):
        print "begin calling " + func.__name__
        func(*args, **kwargs)
        print '*args', args, '**kwargs', kwargs

        print "end calling " + func.__name__
    return wrapper



@log
def hello():
    print "Hello"

@log
def whoareyou(name, age):
    print "name", name
    print "age", age





if __name__ == '__main__':
    hello()
    whoareyou(name = 'Leo', age = 21)


