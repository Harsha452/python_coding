def split_and_join(line):
    # write your code here
    lineA = line.split()
    lineA = '-'.join(lineA)
    return lineA
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
