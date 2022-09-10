
def marksify(cc: str) -> str:
    return '#'*(len(cc.rstrip())-4) + cc.rstrip()[-4:]


print(marksify('123456789'))
