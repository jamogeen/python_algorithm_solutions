
import time

#Function to read the unsorted numbers from the file and converting them into a list
def read_file(file):
    with open(file, "r") as file:
        content = file.read().splitlines()
        content = [int(item) for item in content]
        return content


def mergeSort(sort_list):
    #start of the time timer
    start = time.perf_counter()
    if len(sort_list) > 1:
        # splitting the list into two
        middle = len(sort_list)//2
        lefthalf = sort_list[:middle]
        righthalf = sort_list[middle:]
        #impossing a recursion to the function until all the entire list is all splitted
        mergeSort(lefthalf)
        mergeSort(righthalf)

        #Sorting and swapping
        x = y = z = 0
        while x < len(lefthalf) and y < len(righthalf):
            if lefthalf[x] < righthalf[y]:
                sort_list[z] = lefthalf[x]
                x = x+1
            else:
                sort_list[z] = righthalf[y]
                y = y+1
            z = z+1
        while x < len(lefthalf):
            sort_list[z] = lefthalf[x]
            x = x+1
            z = z+1

        while y < len(righthalf):
            sort_list[z] = righthalf[y]
            y = y+1
            z = z+1
      # stoping the timer and calculating the algorithm runtime
    stop = time.perf_counter()
    time_taken = stop-start
    # return the sorted algorithm and the algorithm runtime as an array
    return sort_list, time_taken


# printing the output for each file-sorted list
print("     arr20.txt output:")
print("SORTED LIST: ", mergeSort(read_file("arr20.txt"))[0])
print("TIME TAKEN IN SECONDS: ", mergeSort(read_file("arr20.txt"))[1])

print("     arr100.txt output:")
print("SORTED LIST: ", mergeSort(read_file("arr100.txt"))[0])
print("TIME TAKEN IN SECONDS: ", mergeSort(read_file("arr100.txt"))[1])

print("     arr1000.txt output:")
print("SORTED LIST: ", mergeSort(read_file("arr1000.txt"))[0])
print("TIME TAKEN IN SECONDS: ", mergeSort(read_file("arr1000.txt"))[1])

print("      arr4000.txt output:")
print("SORTED LIST: ", mergeSort(read_file("arr4000.txt"))[0])
print("TIME TAKEN IN SECONDS: ", mergeSort(read_file("arr4000.txt"))[1])
