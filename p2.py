def find_starting_point(arr):
    total_sum = 0
    current_sum = 0
    start_index = 0

    for i in range(len(arr)):
        total_sum += arr[i]
        current_sum += arr[i]

        if current_sum < 0:
            start_index = i + 1
            current_sum = 0

    # If total_sum is negative, there's no valid start point
    if total_sum < 0:
        return -1
    else:
        return start_index % len(arr)

arr = [-1, 3, -4, 2]
start_index = find_starting_point(arr)

if start_index != -1:
    print(f"Starting point index: {start_index}, value: {arr[start_index]}")
else:
    print("No valid starting point found.")