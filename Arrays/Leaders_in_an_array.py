# Python Function to print leaders in array

def LeadersArray(arr,size):
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]<arr[j]:
                break
            if j == size-1:
                print(arr[i],end=' ')

arr = [12,3,4,55,6,2,1]
LeadersArray(arr,len(arr))