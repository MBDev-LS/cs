def t(s):
    i = (s+s).find(s, 1, -1)
    return None if i == -1 else s[:i]

print(t('abcdabcabc'))