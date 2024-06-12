def palindrome_checker(data):
    palindrome_indices = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][::-1] == data[j]:
                palindrome_indices.append([i, j])
                palindrome_indices.append([j, i])
    return palindrome_indices

print(palindrome_checker(["bat", "tab", "cat"]))
print(palindrome_checker(["olleh", "bat", "tab", "cat", "tac", "hello"]))
print(palindrome_checker(["race", "bat", "cat", "ecar"]))
