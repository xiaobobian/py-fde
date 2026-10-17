def squares_of_evens(nums: list) -> list:
    return [n * n for n in nums if n % 2 == 0]


def squares_of_evens_long(nums: list) -> list:
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n*n)
    return result


nums = [1, 2, 3, 4, 5, 6]
print(squares_of_evens_long(nums))
print(squares_of_evens(nums) == squares_of_evens_long(nums))