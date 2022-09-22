from shutil import register_unpack_format


def find(z):
    total = 0
    x = 0
    for i in z:
        if i == '':
            total += x
        x += 1
    if total == 0:
        return -1
    return total
    