# convert CamelCase to snake_case
def convert_to_python_case(text):
    lst = list(text)
    lst[0] = lst[0].lower()
    for i in range(1, len(lst)):
        if lst[i].isupper():
            lst[i] = '_' + lst[i].lower()
    return ''.join(lst)

txt = input()

print(convert_to_python_case(txt))
