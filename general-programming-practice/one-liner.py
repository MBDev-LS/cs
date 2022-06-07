
def marksify(cc: str) -> str:
    bar = "".join(('#'*(len(cc.lstrip())-4), cc.lstrip()[-4:]))
    return '#'*(len(cc.rstrip())-4) + cc.rstrip()[-4:]


print(marksify('123456789'))
