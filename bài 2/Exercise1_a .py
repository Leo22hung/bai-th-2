def count_chars(inp_string):
    result = {}
    for char in inp_string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

# Ví dụ sử dụng:
word = "Hello"
print("Dictionary đếm số lần các chữ xuất hiện trong từ:", count_chars(word))
