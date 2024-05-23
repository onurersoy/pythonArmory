import time
from time import time as my_timer
# from time import perf_counter as my_timer
# from time import monotonic as my_timer
# from time import process_time as my_timer

# 'process_time' is not really appropriate for this little game, and that's because it returns the time that the CPU
# spends executing the current process rather than the actual elapsed time.

# If you want to measure actual elapsed time then use the 'perf_counter' function, that's really the best way or the
# best function. If you want to know how much time the CPU is spent on a particular task, then use 'process_time'.

# If you want to deal with real times rather than just measuring durations, use the 'time' function.
import random

# Reaction time game:
input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()  # 'my_timer' is actually 'time.time()' so it's our current epoch
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# 'strftime' is for formatting the time value. You can check it from the link below:
# Link: https://docs.python.org/3/library/time.html ('time' documentation link)

reaction_time = end_time - start_time
print(f"Your reaction time was {reaction_time}")
