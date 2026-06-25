secret_code = input("enter any secret code: ")

for shift in range(1, 26):
    decoded_word = ""

    for char in secret_code:
        # Check if the character is an uppercase letter
        if char.isupper():
            alphabet_code = ord(char) - 65
            new_number = (alphabet_code - shift) % 26
            decoded_word += chr(new_number + 65)
            
        # Check if the character is a lowercase letter
        elif char.islower():
            alphabet_code = ord(char) - 97
            new_number = (alphabet_code - shift) % 26
            decoded_word += chr(new_number + 97)
            
        # If it's a space or punctuation, just leave it as it is!
        else:
            decoded_word += char

    print(f"Shift {shift}: {decoded_word}")