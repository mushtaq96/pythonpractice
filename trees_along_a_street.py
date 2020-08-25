#There are N trees growing along a street. For safety reasons , one of the trees needs to be cut down. The local council wants the street to look ordered, so all the remaining trees should be sorted in non-decreasing order of height. Your goal is to count the number of ways this can be done.

def solution(in_arr):
    count=0
    check = 0
    new_arr=[]
    for i in range(len(in_arr)-1):
            if(in_arr[i] < in_arr[i+1] or in_arr[i]==in_arr[i+1]):
                #do nothin
                new_arr.append(in_arr[i])
            
            if(in_arr[i] > in_arr[i+1]):
                #
                count+=1   
            i+=1
    new_arr.append(in_arr[-1])#last            
    print(new_arr)
            



solution([3,4,5,4])#give 2 ie 5 and 4 can be cut