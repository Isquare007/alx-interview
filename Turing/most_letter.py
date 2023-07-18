def SearchingChallenge(str):
    words = str.split()
    max_repeated_letters = 0
    word_with_max_repeated_letters = ""

    for word in words:
        repeated_letters = {}
        for letter in word:
            if letter.isalpha():
                if letter.lower() in repeated_letters:
                    repeated_letters[letter.lower()] += 1
                else:
                    repeated_letters[letter.lower()] = 1

        max_count = max(repeated_letters.values(), default=0)
        if max_count > max_repeated_letters:
            max_repeated_letters = max_count
            word_with_max_repeated_letters = word

    if max_repeated_letters > 1:
        return word_with_max_repeated_letters
    else:
        return -1

# Test the function
input_str = "Hello apple pie"
output_str = SearchingChallenge(input_str)
final_output = ""
token = "t9jfep8w10"
token = list(token)

for i in range(len(output_str)):
    final_output += output_str[i] + token[i]

if len(output_str) < len(token):
    final_output += "".join(token[len(output_str):])

print(output_str)
print("Final Output:", final_output)