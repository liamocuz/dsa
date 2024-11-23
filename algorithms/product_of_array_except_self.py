#pylint: disable=all

"""
Leetcode 238
"""

def pre_post_fix(nums: list[int]) -> list[int]:
    # Idea: Create two arrays
    #       1. The prefix array that contains the product of the values moving forward in the array
    #           Formula: prefix[i] = prefix[i - 1] * nums[i]
    #           Multiply the previous value with the current value
    #       2. The postfix array the contains the product of the values moving backward in the array
    #           Formula: postfix[j] = postfix[j + 1] * nums[j]
    #           Multiply the previous value with the current value

    #       The final formula is answer[k] = prefix[k - 1] + postfix[k + 1]
    #       k - 1 in the prefix will be the product of all values to the left in the original nums array
    #       k + 1 in the prostfix will be the product of all values to the right in the original nums array

    # Time: O(n)
        # Only pass over array 3 times
    # Space: O(n)
        # Create extra arrays

    if not nums:
        return nums
    
    length: int = len(nums)

    # The prefix will compute a running product for all indices before a given index
    # Initialize the first value to the first value of nums as we need to caluculate i - 1
    prefix: list[int] = [0] * length
    prefix[0] = nums[0]
    for i in range(1, length):
        prefix[i] = prefix[i - 1] * nums[i]

    # The postfix will compute a running product for all indices after a given index
    # Initialize the last value to the last value of nums as we need to caluculate j + 1
    postfix: list[int] = [0] * length
    postfix[-1] = nums[-1]
    for j in range(length - 2, -1, -1):
        postfix[j] = postfix[j + 1] * nums[j]

    # Create a final array to return the answer
    answer: list[int] = [0] * length
    for k in range(length):
        # The value at i will be pre[i-1] * post[i+1]
        # If we are at the ends of either pre or post, we use 1 instead
        prefix_value: int = prefix[k - 1] if k - 1 >= 0 else 1
        postfix_value: int = postfix[k + 1] if k + 1 < length else 1

        answer[k] = prefix_value * postfix_value

    print(answer)
    return answer

def two_passes(nums: list[int]) -> list[int]:
    # Idea: Instead of creating the two prefix and postfix arrays, we can instead just use a single answer array
    #       The forward pass computes the prefix values and stores them in the answer array
    #       The backward pass computes both the answer and the next postfix value for the next index
    #       For both passes, we start one off of each end since we know that at some point, i - 1 or j + 1 is out of bounds
    #       and also that we have already computed the final prefix going forward.

    # Time: O(n)
        # Two passes through the array
    # Space: O(1)
        # If we say the answer array is not aux space, then we don't use any extra space

    if not nums:
        return nums

    length: int = len(nums)
    answer: list[int] = [1] * length

    # Compute the prefix values and store them in the answer array
    L: int = nums[0]
    for i in range(1, length):
        answer[i] = L * answer[i - 1]
        # This is only = because we are only currently finding just the prefix values
        L = nums[i]

    # Compute the answer as well as the postfix value
    R: int = nums[-1]
    for j in range(length - 2, -1, -1):
        # answer[j] here is the prefix value, and R is the computed postfix at that index
        answer[j] = R * answer[j]
        # This *= is the real product of both parts, where it computes the postfix and also the answer
        R *= nums[j]

    print(answer)
    return answer


if __name__ == "__main__":
    arr: list[int] = [1, 2, 3, 4]

    pre_post_fix(arr)

    two_passes(arr)