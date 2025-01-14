# ngebuktiin kalo bytecode lebih cepet running code
import time
start_time = time.time ()
print("Hello World")
a=10
print(a)
for i in range(1,1000):
    a=10
print(time.time() - start_time, "detik")
