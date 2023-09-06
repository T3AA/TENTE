def longest_common_prefix(a, b):
    prefix = ""
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            prefix += a[i]
        else:
            break
    return prefix

a = input('a = ')
b = input('b = ')
print('-----')
c = longest_common_prefix(a, b)
print('LCP:', c)

