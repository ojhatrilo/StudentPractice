def expand_string(input_str):
    output = ""
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char.isalpha():
            count = ""
            i += 1
            while i < len(input_str) and input_str[i].isdigit():
                count += input_str[i]
                i += 1
            count = int(count)
            output += char * count
        else:
            output += char
            i += 1
    return output

# Test the function
input_str = "a11b12c13"
output_str = expand_string(input_str)
print(output_str)
