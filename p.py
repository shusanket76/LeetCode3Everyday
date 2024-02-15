def subsets(nums):
    stack = [(0, [])]  # (pointer, current_subset)
    res = []

    while stack:
        pointer, current_subset = stack.pop()

        if pointer == len(nums):
            res.append(current_subset)
        elif pointer < len(nums):
            for next_pointer in range(pointer, len(nums)):
                new_subset = current_subset + [nums[next_pointer]]
                stack.append((next_pointer + 1, new_subset))

    return res

# Example usage:
nums = [1, 2, 3]
print(subsets([1,2,3]))
