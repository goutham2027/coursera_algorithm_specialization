def print_normalized_average_runtime(run_times, normalized_const=1000000):
    time_calc = (sum(run_times)/len(run_times))
    print "Average time for 1000 run after normalizing by multiplying with %s is: %s" % (str(normalized_const), str(time_calc * normalized_const))
