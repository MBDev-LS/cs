
from lists import lst1 as lst

for j in range(len(lst)):
    iMin = j
    for i in range(j+1, len(lst)):
        if lst[i] < lst[iMin]:
            iMin = i

    if iMin != j:
        lst[iMin], lst[j] = lst[j], lst[iMin]

print(lst)

# Implemented using the explanation and phseudocode from this video: https://youtu.be/g-PGLbMth_g
