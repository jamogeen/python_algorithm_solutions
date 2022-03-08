
import time
def read_file(file):
    with open(file,"r") as file:  
        content = file.read().splitlines()
        content = [int(item) for item in content]
        return content

 
def mergeSort(sort_list):
    start = time.perf_counter()
    if len(sort_list)>1:
        middle = len(sort_list)//2
        lefthalf = sort_list[:middle]
        righthalf = sort_list[middle:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        x=y=z=0       
        while x < len(lefthalf) and y < len(righthalf):
            if lefthalf[x] < righthalf[y]:
                sort_list[z]=lefthalf[x]
                x=x+1
            else:
                sort_list[z]=righthalf[y]
                y=y+1
            z=z+1
        while x < len(lefthalf):
            sort_list[z]=lefthalf[x]
            x=x+1
            z=z+1   

        while y < len(righthalf):
            sort_list[z]=righthalf[y]
            y=y+1
            z=z+1
    stop = time.perf_counter() 
    time_taken=stop-start
    return sort_list,time_taken 





print("     arr20.txt output:")
print("SORTED LIST: ",mergeSort(read_file("arr20.txt"))[0])
print("TIME TAKEN IN SECONDS: ",mergeSort(read_file("arr20.txt"))[1])

print("     arr100.txt output:")
print("SORTED LIST: ",mergeSort(read_file("arr100.txt"))[0])
print("TIME TAKEN IN SECONDS: ",mergeSort(read_file("arr100.txt"))[1])

print("     arr1000.txt output:")
print("SORTED LIST: ",mergeSort(read_file("arr1000.txt"))[0])
print("TIME TAKEN IN SECONDS: ",mergeSort(read_file("arr1000.txt"))[1])

print("      arr4000.txt output:")
print("SORTED LIST: ",mergeSort(read_file("arr4000.txt"))[0])
print("TIME TAKEN IN SECONDS: ",mergeSort(read_file("arr4000.txt"))[1])

