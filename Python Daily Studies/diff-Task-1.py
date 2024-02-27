def generate_substrings(input_str):
    substrings = []
    for i in range(len(input_str)):
        for j in range(i, len(input_str)):
            substrings.append(input_str[i:j+1])
    return substrings

def expand_string(input_str):
    substrings = generate_substrings(input_str)
    output = ' '.join(substrings)
    return output

# Test the function
input_str = "abc"
output_str = expand_string(input_str)
print(output_str)
