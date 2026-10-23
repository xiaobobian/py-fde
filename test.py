import time

start=time.perf_counter()
num=0
for i in range(10000):
    # try:
        num=num+1
    # except:
        # pass
    # num+=1
end=time.perf_counter()
print(end-start)