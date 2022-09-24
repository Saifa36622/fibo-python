def string_even(x):
    y = 0
    sum = 0
    po = 0
    #if x.replace(' ','') == '':
      #  return ("Error")
    if x.isnumeric():
        while y < len(x) :
            if int(x[y]) % 2 == 0:
                sum += y
            elif int(x[y]) % 2 != 0:
                po += 1
            y += 1
        return po + sum
    else :
        return ("Error")

print(string_even("142536982"))
print(string_even("0123"))
print(string_even("   "))
#in line 7 and 15 - 16 use to check white space that -> line 5 6 can do it too
