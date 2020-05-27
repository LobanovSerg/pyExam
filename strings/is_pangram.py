def is_pangram(text):
    x = (set('abcdefghijklmnopqrstuvwxyz')
           - set(text.lower()))
    return not x

txt = input()

print(is_pangram(txt))
