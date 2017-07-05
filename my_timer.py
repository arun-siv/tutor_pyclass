import time



from functools import  wraps
def my_timer(func):

    @wraps(func)
    def cal_time(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()

        print("Total time taken is {}ms: ".format(end - start))
        return val
    return cal_time



