import time

def timer(base_fun):
    def counted(*args,**kwargs):
        start_time=time.time()
        base_fun(*args,**kwargs)
        end_time=time.time()
        took_time= end_time - start_time
        print(f"Taken time: {took_time}")
    return counted

@timer
def count():
    for i in range(1,1000001):
        count_times=i
    print(f"counted {count_times} times")

count()