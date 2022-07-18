def solution(y):
    y=str(y)
    j=0
    k=2
    empty_list = []
    for i in range(len(y)-1):

        x= int(y[j:k])
        empty_list.append(x)

        j=j+1
        k=k+1
    return max(empty_list)
print(solution('16749'))
