"""
Given a string, window length and how many spaces to shift, write a routine that will give the
string in the next window.
"""

def window_str_gen(str, window_length, shift):
    b = 0
    sl = len(str)
    while b < sl:
        e = min(b + window_length, sl)
        yield str[b:e]
        if e >= sl:
            break
        b += shift


str = "abcdefghijklmnopqrstuvwxyz"
window_len, shift = 4, 2
# window_len, shift = 1, 2
# window_len, shift = 0, 2
# window_len, shift = 28, 2
# window_len, shift = 4, 28
# window_len, shift = 4, 4
# window_len, shift = 1, 1
# window_len, shift = 1, 0

# str = 'abcdef'
# window_len, shift = 7, 2

wsg = window_str_gen(str, window_len, shift)
for ws in wsg:
    print('ws =', ws)
