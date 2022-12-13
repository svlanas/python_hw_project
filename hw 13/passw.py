def test_passw(func):
    def test_1():
        rules = "Пароль має бути довжиною не менше 8 символів, містити "\
              " принаймні 1 цифру, 1 букву та 1 спеціальний символ. \nПароль "\
              "не може містити пробільні символи чи символи табуляції"
        print(rules)
        passw = func()
        while passw is None:
            print("ПОМИЛКА! Введений пароль містить пробільні символи, "\
                  "символи табуляції чи пустий")
            print(rules)
            passw = func()
        return passw

    def test_2():
        spec_chars = "\"!$%&()*+,-.:;<=>?@^_`\'{|}]"
        passw = test_1()
        while True:
            message = ""
            if len(passw) < 8:
                message = message + "ПОМИЛКА! пароль містить менше 8 символів\n"
            elif not any(map(lambda char: char.isalpha(), passw)) is True:
                message = message + "ПОМИЛКА! пароль не містить жодної букви\n"
            elif not any(map(lambda char: char.isdigit(), passw)) is True:
                message = message + "ПОМИЛКА! пароль не містить жодної цифри\n"
            elif not any(map(lambda char: char in spec_chars, passw)) is True:
                message = message + "ПОМИЛКА! пароль не містить спеціальних " \
                                    "символів\n"
            else:
                break
            print(message)
            passw = test_1()
        return lambda: print("Пароль відповідає вимогам")
    return test_2()


@test_passw
def password():
    passw = input("Введіть пароль ")
    if " " in passw.expandtabs() or passw == "":
        return
    else:
        return passw


if __name__ == "__main__":
    password()
