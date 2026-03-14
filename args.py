def get_sum(a: int, b: int, c: int = 3, *args) -> int:
    
    print(a, b)
    print(c)
    print(args)

    return 0


nums = [1, 2, 3]

result = get_sum(4, 3, 5, *nums)

print(result)
