def expand_string(input_str):
    output_str = ""
    i = 0

    while i < len(input_str):
        char = input_str[i]
        count = ""
        
        while i + 1 < len(input_str) and input_str[i + 1].isdigit():
            count += input_str[i + 1]
            i += 1       

        count = int(count) if count else 1        
        output_str += count * char
        i += 1

    return output_str
a=input("enter the string")
print(expand_string(a))  
  
