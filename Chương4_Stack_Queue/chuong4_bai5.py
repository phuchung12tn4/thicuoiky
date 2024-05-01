def sliding_max(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i+k]))
    return result

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
output = sliding_max(num_list, k)
print(output)