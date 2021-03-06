def new_password(dict_str):
    dict_str.update({8: dict_str.get(8) + 1})
    for i in reversed(range(1, 9)):
        if dict_str.get(i) > len(alphabet):
            dict_str.update({i: 1})
            dict_str.update({i - 1: dict_str.get(i - 1) + 1})

    return dict_str


class Some_Error(BaseException):
    None


alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict_str = {}

print('Помогаем Санте получить новый пароль по новым критериям...\n')

with open('input.txt', 'r') as INPUT:
    string = INPUT.readline()
    string = string.strip()

print('Старый пароль: ' + string)

counter = 1
for alpha in string:
    dict_str.update({counter: alphabet.find(alpha) + 1})
    counter += 1

values = list(dict_str.values())

while True:
    try:

        if alphabet.find('i') + 1 in dict_str.values() or alphabet.find('o') + 1 in dict_str.values() or alphabet.find(
                'l') + 1 in dict_str.values():
            raise Some_Error()

        string = str()
        for i in range(1, 9):
            string += alphabet[dict_str.get(i) - 1]

        new_array = []
        counter = 1
        try:
            for i in range(len(string)):
                if string[i] == string[i + 1]:
                    counter += 1
                else:
                    new_array.append([string[i], counter])
                    counter = 1
        except IndexError:
            new_array.append([string[i], counter])
def new_password(dict_str):
    dict_str.update({8: dict_str.get(8) + 1})
    for i in reversed(range(1, 9)):
        if dict_str.get(i) > len(alphabet):
            dict_str.update({i: 1})
            dict_str.update({i - 1: dict_str.get(i - 1) + 1})

    return dict_str



class Some_Error(BaseException):
    None


print('Помогаем Санте получить новый пароль по новым критериям...\n')

with open('input.txt', 'r') as INPUT:
    string = INPUT.readline()
    string = string.strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('Старый пароль: ' + string)


def PASSWORD_GENERATOR_3000(string):
    dict_str = {}


    counter = 1
    for alpha in string:
        dict_str.update({counter: alphabet.find(alpha) + 1})
        counter += 1

    values = list(dict_str.values())


    while True:
        try:

            if alphabet.find('i') + 1 in dict_str.values() or alphabet.find(
                    'o') + 1 in dict_str.values() or alphabet.find('l') + 1 in dict_str.values():
                raise Some_Error()


            string = str()
            for i in range(1, 9):
                string += alphabet[dict_str.get(i) - 1]



            new_array = []
            counter = 1
            try:
                for i in range(len(string)):
                    if string[i] == string[i + 1]:
                        counter += 1
                    else:
                        new_array.append([string[i], counter])
                        counter = 1
            except IndexError:
                new_array.append([string[i], counter])
            counter = 0
            for element in new_array:
                if element[1] > 1:
                    counter += 1
            if counter < 2:
                raise Some_Error()


            new_array = []
            for i in range(len(string) - 2):
                new_array.append(string[i] + string[i + 1] + string[i + 2])
            for element in new_array:
                if element in alphabet:
                    raise ZeroDivisionError()
            raise Some_Error()

        except Some_Error:
            dict_str = new_password(dict_str)
        except ZeroDivisionError:
            break
    return string


def PASSWORD_GENERATOR_1337_228(string):
    dict_str = {}
    counter = 1
    for alpha in string:
        dict_str.update({counter: alphabet.find(alpha) + 1})
        counter += 1

    values = list(dict_str.values())
    dict_str = new_password(dict_str)
    string = str()
    for i in range(1, 9):
        string += alphabet[dict_str.get(i) - 1]
    string = PASSWORD_GENERATOR_3000(string)
    return string


string = PASSWORD_GENERATOR_3000(string)
print('Новый пароль: ' + string)
string = PASSWORD_GENERATOR_1337_228(string)
print('Новейший пароль: ' + string)


with open('output2.txt', 'w') as O:
    O.write(string)