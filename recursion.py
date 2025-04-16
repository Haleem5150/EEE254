# Function to find all subsets of a set using recursion
def find_subsets(nums, index=0, current_subset=None):
    if current_subset is None:
        current_subset = []
    
    # Base case: if we've considered all elements, print the current subset
    if index == len(nums):
        print(current_subset)
        return
    
    # Recursive case 1: Include the current element
    find_subsets(nums, index + 1, current_subset + [nums[index]])

    # Recursive case 2: Exclude the current element
    find_subsets(nums, index + 1, current_subset)

# Example usage: Find all subsets of the set [1, 2, 3]
nums = [1, 2, 3]
find_subsets(nums)
