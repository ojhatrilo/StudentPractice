# str = abbbcdddd
# Output: a1b3c1d4
def compress_string(s):
    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    compressed += s[-1] + str(count)
    return compressed

input_str = "abbbcdddd"
output_str = compress_string(input_str)
print(output_str)




    


