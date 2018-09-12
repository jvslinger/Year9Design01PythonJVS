import time
import sys

print "Next Program is Loading"
animation = "|/-\\"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print "Success!"

import poopee