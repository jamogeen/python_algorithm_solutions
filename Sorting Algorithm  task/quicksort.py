import time
import sys
sys.setrecursionlimit(10000)


def partition(pivot_position, end, sort_list):

    # Initializing pivot's index to start
    pivot_index = pivot_position
    pivot = sort_list[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while pivot_position < end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while pivot_position < len(sort_list) and sort_list[pivot_position] <= pivot:
            pivot_position += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while sort_list[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(pivot_position < end):
            sort_list[pivot_position], sort_list[end] = sort_list[end], sort_list[pivot_position]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    sort_list[end], sort_list[pivot_index] = sort_list[pivot_index], sort_list[end]

    # Returning end pointer to divide the list into 2
    return end

# The main function that implements QuickSort


def quick_sort(pivot_position, end, sort_list):
    start = time.perf_counter()
    if(pivot_position < end):
        p = partition(pivot_position, end, sort_list)

        # sorting the list element before the partition implemetation and after
        # partition

        quick_sort(pivot_position, p-1, sort_list)
        quick_sort(p + 1, end, sort_list)
    stop = time.perf_counter()
    time_taken = stop - start
    return sort_list, time_taken

# Driver code


def read_file(file):
    with open(file, "r") as file:
        content = file.read().splitlines()
        content = [int(item) for item in content]
        return content

files_arr=["arr20.txt","arr100.txt","arr1000.txt","arr4000.txt"]

for i in files_arr:

	sort_list = read_file(i)

	pivot_number = len(sort_list) - 1
	# quick_sort(0, pivot_number, sort_list)
	print(f"      {i}output:")
	print("SORTED LIST:", quick_sort(0, pivot_number, sort_list)[0])
	print("TIME TAKEN IN SECONDS: ", quick_sort(0, pivot_number, sort_list)[1])

# print("     arr20.txt output:")
# print("SORTED LIST: ", sortingalg(algorithm_20)[0])
# print("TIME TAKEN IN SECONDS: ", sortingalg(algorithm_20)[1])