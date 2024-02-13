import re
from .util_array import pillam, charactors, vowels

text = ""
nVowels = 0
consonants = []
consonantsUni = []
vowels = []
vowelsUni = []
vowelModifiersUni = []
specialConsonants = []
specialConsonantsUni = []
specialCharUni = []
specialChar = []

vowelsUni.append('ඌ')
vowels.append('oo')
vowelModifiersUni.append('ූ')
vowelsUni.append('ඕ')
vowels.append('o\\)')
vowelModifiersUni.append('ෝ')
vowelsUni.append('ඕ')
vowels.append('oe')
vowelModifiersUni.append('ෝ')
vowelsUni.append('ආ')
vowels.append('aa')
vowelModifiersUni.append('ා')
vowelsUni.append('ආ')
vowels.append('a\\)')
vowelModifiersUni.append('ා')
vowelsUni.append('ඈ')
vowels.append('Aa')
vowelModifiersUni.append('ෑ')
vowelsUni.append('ඈ')
vowels.append('A\\)')
vowelModifiersUni.append('ෑ')
vowelsUni.append('ඈ')
vowels.append('ae')
vowelModifiersUni.append('ෑ')
vowelsUni.append('ඊ')
vowels.append('ii')
vowelModifiersUni.append('ී')
vowelsUni.append('ඊ')
vowels.append('i\\)')
vowelModifiersUni.append('ී')
vowelsUni.append('ඊ')
vowels.append('ie')
vowelModifiersUni.append('ී')
vowelsUni.append('ඊ')
vowels.append('ee')
vowelModifiersUni.append('ී')
vowelsUni.append('ඒ')
vowels.append('ea')
vowelModifiersUni.append('ේ')
vowelsUni.append('ඒ')
vowels.append('e\\)')
vowelModifiersUni.append('ේ')
vowelsUni.append('ඒ')
vowels.append('ei')
vowelModifiersUni.append('ේ')
vowelsUni.append('ඌ')
vowels.append('uu')
vowelModifiersUni.append('ූ')
vowelsUni.append('ඌ')
vowels.append('u\\)')
vowelModifiersUni.append('ූ')
vowelsUni.append('ඖ')
vowels.append('au')
vowelModifiersUni.append('ෞ')
vowelsUni.append('ඇ')
vowels.append('/\a')
vowelModifiersUni.append('ැ')
vowelsUni.append('අ')
vowels.append('a')
vowelModifiersUni.append('')
vowelsUni.append('ඇ')
vowels.append('A')
vowelModifiersUni.append('ැ')
vowelsUni.append('ඉ')
vowels.append('i')
vowelModifiersUni.append('ි')
vowelsUni.append('එ')
vowels.append('e')
vowelModifiersUni.append('ෙ')
vowelsUni.append('උ')
vowels.append('u')
vowelModifiersUni.append('ු')
vowelsUni.append('ඔ')
vowels.append('o')
vowelModifiersUni.append('ො')
vowelsUni.append('ඓ')
vowels.append('I')
vowelModifiersUni.append('ෛ')
nVowels = 26
specialConsonantsUni.append('ං')
specialConsonants.append('/\\n/g')
specialConsonantsUni.append('ඃ')
specialConsonants.append('/\\h/g')
specialConsonantsUni.append('ඞ')
specialConsonants.append('/\\N/g')
specialConsonantsUni.append('ඍ')
specialConsonants.append('/\\R/g')
specialConsonantsUni.append('ර්'+'\u200D')
specialConsonants.append('/R/g')
specialConsonantsUni.append('ර්'+'\u200D')
specialConsonants.append('/\\r/g')
consonantsUni.append('ඬ')
consonants.append('nnd')
consonantsUni.append('ඳ')
consonants.append('nndh')
consonantsUni.append('ඟ')
consonants.append('nng')
consonantsUni.append('ථ')
consonants.append('Th')
consonantsUni.append('ධ')
consonants.append('Dh')
consonantsUni.append('ඝ')
consonants.append('gh')
consonantsUni.append('ඡ')
consonants.append('Ch')
consonantsUni.append('ඵ')
consonants.append('ph')
consonantsUni.append('භ')
consonants.append('bh')
consonantsUni.append('ශ')
consonants.append('sh')
consonantsUni.append('ෂ')
consonants.append('Sh')
consonantsUni.append('ඥ')
consonants.append('GN')
consonantsUni.append('ඤ')
consonants.append('KN')
consonantsUni.append('ළු')
consonants.append('Lu')
consonantsUni.append('ද')
consonants.append('dh')
consonantsUni.append('ච')
consonants.append('ch')
consonantsUni.append('ඛ')
consonants.append('kh')
consonantsUni.append('ත')
consonants.append('th')
consonantsUni.append('ට')
consonants.append('t')
consonantsUni.append('ක')
consonants.append('k')
consonantsUni.append('ඩ')
consonants.append('d')
consonantsUni.append('න')
consonants.append('n')
consonantsUni.append('ප')
consonants.append('p')
consonantsUni.append('බ')
consonants.append('b')
consonantsUni.append('ම')
consonants.append('m')
consonantsUni.append('‍ය')
consonants.append('\\u005C' + 'y')
consonantsUni.append('‍ය')
consonants.append('Y')
consonantsUni.append('ය')
consonants.append('y')
consonantsUni.append('ජ')
consonants.append('j')
consonantsUni.append('ල')
consonants.append('l')
consonantsUni.append('ව')
consonants.append('v')
consonantsUni.append('ව')
consonants.append('w')
consonantsUni.append('ස')
consonants.append('s')
consonantsUni.append('හ')
consonants.append('h')
consonantsUni.append('ණ')
consonants.append('N')
consonantsUni.append('ළ')
consonants.append('L')
consonantsUni.append('ඛ')
consonants.append('K')
consonantsUni.append('ඝ')
consonants.append('G')
consonantsUni.append('ඨ')
consonants.append('T')
consonantsUni.append('ඪ')
consonants.append('D')
consonantsUni.append('ඵ')
consonants.append('P')
consonantsUni.append('ඹ')
consonants.append('B')
consonantsUni.append('ෆ')
consonants.append('f')
consonantsUni.append('ඣ')
consonants.append('q')
consonantsUni.append('ග')
consonants.append('g')
consonantsUni.append('ර')
consonants.append('r')
specialCharUni.append('ෲ')
specialChar.append('ruu')
specialCharUni.append('ෘ')
specialChar.append('ru')

def sinhala_to_singlish(input_text):
    output_array = []
    # input_text = list(input_text + ' ')
    try:
        for i, char in enumerate(input_text):
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

def singlish_to_sinhala(input_text):
    global text
    s = ""
    r = ""
    v = ""
    text = input_text
    for i in range(len(specialConsonants)):
        text = text.replace(specialConsonants[i], specialConsonantsUni[i])
    for i in range(len(specialCharUni)):
        for j in range(len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + specialCharUni[i]
            r = re.compile(s)
            text = r.sub(v, text)
    for j in range(len(consonants)):
        for i in range(len(vowels)):
            s = consonants[j] + "r" + vowels[i]
            v = consonantsUni[j] + "්‍ර" + vowelModifiersUni[i]
            r = re.compile(s)
            text = r.sub(v, text)
        s = consonants[j] + "r"
        v = consonantsUni[j] + "්‍ර"
        r = re.compile(s)
        text = r.sub(v, text)
    for i in range(len(consonants)):
        for j in range(nVowels):
            s = consonants[i] + vowels[j]
            v = consonantsUni[i] + vowelModifiersUni[j]
            r = re.compile(s)
            text = r.sub(v, text)
    for i in range(len(consonants)):
        r = re.compile(consonants[i])
        text = r.sub(consonantsUni[i]+"්", text)
    for i in range(len(vowels)):
        r = re.compile(vowels[i])
        text = r.sub(vowelsUni[i], text)
    return text
