def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    
    if k == 0:
        return -1

    result = 1
    counter = 0
    while counter < k:
        result = result * (n - counter)
        counter += 1
  
    return result




def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    total = 0
    while y:
        # while y will iterate as long as y is not zero
        # 123 % 10 = 3, 120 // 10 = 12, 12 % 10 = 2, 12 // 10 = 1, res = 3+2+1
        last = y % 10
        y //= 10
        total += last

    return total






def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    just_saw_an_eight = False
    while n > 0:
        last = n % 10
        n //= 10
        if last == 8 and just_saw_an_eight:
            return True
        if last == 8:
            just_saw_an_eight = True
        else:
            just_saw_an_eight = False
    return False



    

        


