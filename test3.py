import time
def partition():
    print("Hello world")
def quick_sort(pivot_position,end,sort_array):
    start = time.perf_counter
    if(pivot_position<end):
        p = partition(pivot_position,end,sort_array)

        # sorting the list element before the partition implemetation and after 
        # partition

        quick_sort(pivot_position ,p-1,sort_array)
        quick_sort(p + 1,end,sort_array)
    stop = time.perf_counter
    time_taken = stop -start
    return sort_array,time
