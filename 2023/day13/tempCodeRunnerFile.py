 data = file.readlines()
    return data
def findVertical(line):
    left = 0
    right = len(line) -1
    while left < right:
        if line[left] == line[right]:
            left += 1
            right -= 1
        else:
            right = len(line)-1
            # left += 1
            if line[left] != line[right]:
                left += 1
    if left == right:
        return False
    else:
        return left 