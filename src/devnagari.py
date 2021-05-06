# Example: ascii
print('ascii(क) =', ascii('क'))
print('ascii(ब) =', ascii('ब'))
print('ascii(रा) =', ascii('रा'))
print('ascii(दी) =', ascii('दी'))
print('ascii(र्व) =', ascii('र्व'))
print('ascii(खि) =', ascii('खि'))
print('ascii(ढ) =', ascii('ढ'))
print('ascii(यै) =', ascii('यै'))
print('ascii(ष) =', ascii('ष'))

# Example: ord, chr
print('ord(ष) =', ord('ष'))
print('chr(ord(ष)) =', chr(ord('ष')))
print('ord(ा) =', ord('ा'))
print('chr(ord(ा)) =', chr(ord('ा')))
print('ord(अ) =', ord('अ'))
print('chr(ord(अ)) =', chr(ord('अ')))
print('ord(आ) =', ord('आ'))
print('chr(ord(आ)) =', chr(ord('आ')))
print('ord(्) =', ord('्'))
print('chr(ord(्)) =', chr(ord('्')))

# The following code gives exception since खि is a string of length two
# print('ord(खि) =', ord('खि'))
# print('chr(ord(खि)) =', chr(ord('खि')))
