# УСЛОВИЕ:
# Посчитать процентное соотношение букв в тексте. Заглавные и строчные приравниваются.
# Вывести словарь: ключ - буква, значение - процент (до десятых),
# в котором эта буква встречается в тексте.

TEXT = 'Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Donec rutrum congue leo eget malesuada.'


def percentage(TEXT):

    all_letters = []
    no_repeat_letter = []
    for words in TEXT.lower():
        words = words.rstrip('.,: !?')
        for let in words:
            all_letters.append(let)
            if not let in no_repeat_letter:
                no_repeat_letter.append(let)

    dict_key = [l for l in no_repeat_letter]
    dict_values = [round(all_letters.count(l) * 100 / len(all_letters), 1) for l in all_letters]
    result = zip(dict_key, dict_values)

    return dict(result)

# print(percentage(TEXT))

# УСЛОВИЕ:
# Дан текст и ограничение длины текста (в количестве символов).
# Необходимо, в случае, если текст не помещается в
# ограничение обрезать его, но при этом слова не должны обрываться
# на середине (исключение первое слово),
# и в конце нужно добавить троеточие ("...").


def limit_symbol(text, limit=0):
    end = '...'
    trim_text = ''
    if limit >= len(text):
        return text
    
    for i, word in enumerate(text.split()):
        trim_text += word + ' '

        if len(trim_text[:-1] + end) > limit:
            if i == 0:
                return word[: limit - len(end)] + end
            return trim_text[:-len(word) - 2] + end

# print(limit_symbol(TEXT, 13))