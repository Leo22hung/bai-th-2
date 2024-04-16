def max_sliding_window(num_list, k):
    if not num_list or k <= 0:
        return []

    n = len(num_list)
    max_list = []

    for i in range(n - k + 1):
        max_in_window = max(num_list[i:i+k])
        max_list.append(max_in_window)

    return max_list

# Ví dụ sử dụng:
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print("Số lớn nhất trong sliding window:", max_sliding_window(num_list, k))
