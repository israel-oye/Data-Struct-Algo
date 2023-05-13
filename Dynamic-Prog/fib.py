from timeit import default_timer as timer


def ordinary_fibonacci_sum(n: int):
    if n <= 1:
        return 1
    else:
        return ordinary_fibonacci_sum(n-1) + ordinary_fibonacci_sum(n-2)


def memoised_fibonacci_sum(n: int, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        memo[n] = 1
    else:
        memo[n] = memoised_fibonacci_sum(n-1, memo) + memoised_fibonacci_sum(n-2, memo)

    return memo[n]

start_1 = timer()
print(ordinary_fibonacci_sum(20))
end_1 = timer()

start_2 = timer()
print(memoised_fibonacci_sum(20))
end_2 = timer()


print(f"\nOrdinary fib run time: {end_1 - start_1}s")
print(f"Memoised fib run time: {end_2 - start_2}s")
