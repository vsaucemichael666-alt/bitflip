import random
import string


def generate_chaos_code(original_text, corrupted_text):

    total_text_weight = sum(ord(c) for c in original_text)

    error_index = -1
    original_char_code = 0
    corrupted_char_code = 0

    limit = min(len(original_text), len(corrupted_text))
    found = False

    for i in range(limit):
        if original_text[i] != corrupted_text[i]:
            error_index = i
            original_char_code = ord(original_text[i])
            corrupted_char_code = ord(corrupted_text[i])
            found = True
            break

    if not found:
        return "Ошибок не найдено"


    bit_difference = original_char_code ^ corrupted_char_code

    seed_value = (total_text_weight * (error_index + 1)) + bit_difference


    random.seed(seed_value)


    chars = string.ascii_letters + string.digits

    output_length = (seed_value % 16) + 8

    result = "".join(random.choice(chars) for _ in range(output_length))

    return result



res = generate_chaos_code("bdhsjlchp", "bdhs.lchp")


print( res )


