def countWords(s):
    count = 1
    for i in s:
        if i == " ":
            count += 1
    return count

print(countWords("Hello world this is Me!"))