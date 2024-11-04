def log_execution(fun):
    def wrapper():
        print("Function running")
        fun()
        print("Function Completed")
    return wrapper

@log_execution
def say_hello():
    print("hello!")

say_hello()
