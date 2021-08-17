if __name__ == '__main__':
    n = int(raw_input())
    
    #First Sloution
    arr = map(int, raw_input().split())
    print (sorted(set(arr))[-2])
    
    #Second Solution
#     max_value=max(arr)
#     runner_up_score=min(arr)
#     n =len(arr)
#     for i in range(1,n):
#         if arr[i]>max_value:
#             runner_up_score=max_value
#             max_value=arr[i]
#         elif arr[i]>runner_up_score and max_value != arr[i]:
#             runner_up_score=arr[i]
 
# print(runner_up_score)
