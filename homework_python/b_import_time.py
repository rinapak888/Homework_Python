#for i in range(10):
    #print(i)

#for hours in range(24):
    #for minutes in range(60):
        #for seconds in range(60):
            #print(hours, ':', minutes, ':', seconds)

#for i in range(1, 4):
    #for j in range(3, 5):
        #print(i + j, end='')

#counter = 0
#for i in range(99, 102):
    #temp = i
    #while temp > 0:
        #counter += 1
        #temp //= 10
#print(counter)

import time 

time_start = time.time()
i = 0
while i < 1000000000:
    i += 1
    
t_f = time.time()
t_s = t_f - time_start
print(t_s, 'seconds')



