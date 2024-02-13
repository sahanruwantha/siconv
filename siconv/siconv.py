from .util_array import pillam, charactors, vowels

def sinhala_to_singlish(input_text):
    output_array = []
    input_text = list(input_text + ' ')
    try:
        for i, char in enumerate(input_text[:-1]):
            e_char = charactors.get(char)
            p_char = pillam.get(char)

            is_vowel = char in vowels

            if e_char:
                # Preserve spaces
                output_array.append(char if char == ' ' else e_char)

                # Check for pillam and append 'a'
                next_char = input_text[i + 1]
                output_array.append(pillam.get(next_char) or 'a' if e_char and char != ' ' else '')

            elif not e_char and not p_char:
                # Character not found in mapping, keep the original character
                output_array.append(char)

            if is_vowel:
                if output_array:
                    output_array.pop()

        # Add the last character to the output
        output_array.append(charactors.get(input_text[-1], input_text[-1]))

    except Exception as e:
        # Handle exceptions and print an error message
        print(f"An error occurred: {e}")
        # You can choose to log the exception or handle it in a different way

    return "".join(output_array)

