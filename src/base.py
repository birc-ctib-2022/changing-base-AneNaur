"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    
    #1*2^0 = 1
    #31//2=15 (rest 1) -> 15//2=7 (rest 1) -> 7//2=3 (rest 1) -> 3//2=1 (rest 1) -> 1//2=0 (rest 1) => 11111
    #31//8=3 (rest 7) -> 3//8=0 (rest 3) => 37
    #31//16=1 (rest 15=F) -> 1//16=0 (rest 1) => 1F

    assert 2 <= b <= 16
    liste=[]
    while n >= b:
        liste.append(digits[n%b])
        n=n//b
    else:
        liste.append(digits[n%b])
    return "".join(liste[::-1])  # FIXME: return n in the right base

#print(change_to_base(1,2))
#print(change_to_base(31,2))
#print(change_to_base(31,8))
#print(change_to_base(31,16))
