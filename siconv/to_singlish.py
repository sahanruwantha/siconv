charactors = {
    'අ': 'a', 'ආ': 'aa', 'ඇ': 'A', 'ඉ': 'i', 'ඊ': 'ii', 'උ': 'u', 'ඍ': 'Ru', 'එ': 'e', 'ඔ': 'o', 'ක': 'k', 'ග': 'g', 'ච': 'ch',
    'ජ': 'j', 'ට': 't', 'ඩ': 'd', 'න': 'n', 'ප': 'p', 'බ': 'b', 'ල': 'l', 'ද': 'd', 'ව': 'w', 'ශ': 'sh',
    'භ': 'bh', 'ස': 's', 'හ': 'h', 'ය': 'y', 'ර': 'r', 'ම': 'm', 'ත': 'th', 'ඛ': 'kh', ' ': ' ', 'ඳ': 'dn',
    'උ': 'u', 'ඌ': 'uu', 'ඕ': 'oo', 'ඔ': 'o', 'ඖ': 'au', 'ඞ': 'ng', 'ඟ': 'gn', 'ඡ': 'chh', 'ඣ': 'jh',
    'ඍ': 'R', 'ඎ': 'Ru', 'ඏ': 'A', 'ඐ': 'aa', 'ෆ': 'fa',
    'ච': 'ch', 'ජ': 'j', 'ඩ': 'd', 'ළ': 'L', 'ණ': 'N', 'ධ': 'dhh', 'ඤ': 'zk', 'ඥ': 'zh',
    'ෂ': 'S', 'හෝ': 'Sh', 'ෆ': 'a', 'ඹ': 'B', 'ළු': 'L', 'ඟ': 'zg', 'ඦ': 'zja', 'ඬ': 'zd', 'හෝ': 'q',
    'ඥ': 'zh', 'ය': 'y', 'හෝ': 'A', 'හෝ': 'o', 'හෝ': 'v', 'හෝ': 'f', 'හෝ': 'Sh',
    'ඈ': 'Aa', 'ඌ': 'uu','ඎ': 'Ruu','ඒ': 'ee', 'ඓ': 'Ee', 'ඕ': 'O', 'ඖ': 'Ou'
}


pillam = {
    'ා': 'aa', 'ැ': 'A', 'ෑ': 'Aa', 'ි': 'i', 'ී': 'ii', 'ු': 'u', 'ූ': 'uu', 'ෘ': 'ru', 'ෙ': 'e', 'ේ': 'ee', 'ෛ': 'ai',
    'ො': 'o', 'ෝ': 'oo', 'ෞ': 'au',
    '්‍ය': 'ya', '්‍ර': 'ra' , '්': ' '
}

vowels = ['අ', 'ආ', 'ඇ', 'ඈ', 'ඉ', 'ඊ', 'උ', 'ඌ', 'ඍ', 'ඎ', 'ඏ', 'ඐ', 'එ', 'ඒ', 'ඓ', 'ඔ', 'ඕ', 'ඖ']

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
            
            if is_vowel or char == '්':
                if output_array:
                    output_array.pop()

        # Add the last character to the output
        output_array.append(charactors.get(input_text[-1], input_text[-1]))

    except Exception as e:
        # Handle exceptions and print an error message
        print(f"An error occurred: {e}")

    return "".join(output_array)
