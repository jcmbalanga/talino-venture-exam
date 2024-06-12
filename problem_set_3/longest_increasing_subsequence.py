def longest_increasing_subsequence(data):
    scoring = [1] * len(data)
    for i in range(1, len(data)):
        for j in range(i):
            if data[i] > data[j]:
                print(f"{i}: {scoring[i]}", f"{j}: {scoring[j]}")
                scoring[i] = max(scoring[i], scoring[j] + 1)
    return max(scoring)

print(longest_increasing_subsequence([1, 2, 3, 4, 5]))
print(longest_increasing_subsequence([1, 2, 5, 4, 6]))
print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18, 20, 0, 21]))
