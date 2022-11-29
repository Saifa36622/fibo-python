def palindrome_type(n):
    ans = ""
    str_n = str(n)
    str_n_reverse = str_n[::-1]
    n_reverse = int(str_n_reverse)
    un_bn = bin(n)
    bn = un_bn[2::]
    re_bn = bn[::-1]
    if n == n_reverse and bn == re_bn:
        return "Decimal and binary"
    elif n == n_reverse and bn != re_bn:
        return "Decimal only"
    elif n != n_reverse and bn == re_bn:
        return "Binary only"
    else :
        return "Neither"
# print(palindrome_type(1934391))
# print(palindrome_type(9994521))
# print(palindrome_type(8337738))
