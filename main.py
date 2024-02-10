from util_array import pillam, charactors

def to_sinhala_unicode(input_text):
    output_array = []

    for i, char in enumerate(input_text[:-1]):
        e_char = charactors.get(char)
        p_char = pillam.get(char)

        if e_char:
            # Preserve spaces
            output_array.append(char if char == ' ' else e_char)

            # Check for pillam and append 'a'
            next_char = input_text[i + 1]
            output_array.append(pillam.get(next_char) or 'a' if e_char and char != ' ' else '')
        
        elif not e_char and not p_char:
            # Character not found in mapping, keep the original character
            output_array.append(char)
            
        if char == '්':
            output_array.pop()

    # Add the last character to the output
    output_array.append(charactors.get(input_text[-1], input_text[-1]))

    return "".join(output_array)

input_text = "පහත සඳහන් දෑ සතුන්, ශාක සහ ඛනිජ ලෙස වර්ග කරන්න "
output_text = to_sinhala_unicode(input_text)
print(output_text)
