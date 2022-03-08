import random
import time
from tracemalloc import stop


# Function to generate the random numbers
def random_number():
    ran_list_20 = random.sample(range(0, 6000), 20)
    ran_list_100 = random.sample(range(0, 6000), 100)
    ran_list_1000 = random.sample(range(0, 6000), 1000)
    ran_list_4000 = random.sample(range(0, 6000), 4000)

    # function to write the random number list into a txt file
    def write_number(file, random_number):
        with open(file, "w") as file:
            for item in random_number:
                file.write(str(item))
                file.write("\n")
    # calling the write funcction to write each file with different list
    write_number("arr20.txt", ran_list_20)
    write_number("arr100.txt", ran_list_100)
    write_number("arr1000.txt", ran_list_1000)
    write_number("arr4000.txt", ran_list_4000)


random_number()

# function to read the numbers from the file into a list


def read_file(file):
    with open(file, "r") as file:
        content = file.read().splitlines()
        content = [int(item) for item in content]
        return content


algorithm_20 = read_file("arr20.txt")
algorithm_100 = read_file("arr100.txt")
algorithm_1000 = read_file("arr1000.txt")
algorithm_4000 = read_file("arr4000.txt")


# start of the sorting algorithm
def sortingalg(input_arr):
    # start of the time counter to measure the algorithm runtime
    start = time.perf_counter()\

    # start of the insertion sort
    for number in range(1, len(input_arr)):
        current_number = input_arr[number]
        current_position = number

        while current_position > 0 and input_arr[current_position - 1] > current_number:
            input_arr[current_position] = input_arr[current_position - 1]
            current_position = current_position - 1

        input_arr[current_position] = current_number

        #stoping the timer and calculating the algorithm runtime
    stop = time.perf_counter()
    time_taken = stop-start
    #return the sorted algorithm and the algorithm runtime as an array
    return input_arr, time_taken

#printing the output for each file-sorted list
print("     arr20.txt output:")
print("SORTED LIST: ", sortingalg(algorithm_20)[0])
print("TIME TAKEN IN SECONDS: ", sortingalg(algorithm_20)[1])

print("     arr100.txt output:")
print("SORTED LIST: ", sortingalg(algorithm_100)[0])
print("TIME TAKEN IN SECONDS: ", sortingalg(algorithm_100)[1])

print("     arr1000.txt output:")
print("SORTED LIST: ", sortingalg(algorithm_1000)[0])
print("TIME TAKEN IN SECONDS: ", sortingalg(algorithm_1000)[1])

print("      arr4000.txt output:")
print("SORTED LIST: ", sortingalg(algorithm_4000)[0])
print("TIME TAKEN IN SECONDS: ", sortingalg(algorithm_4000)[1])
