import time
import sys
h=3
m=40
s=0
while true:
    sys.stdout.write("\r{:0.2d}: {:0.2d} : {0.2d}".format)
    sys.stdout.flush()
    time.sleep(1)
    s=s+1
    if s==60:
       s=0
       m=m+1
    if m==60:
       m=0
       h=h+1
