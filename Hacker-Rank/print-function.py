if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150:
        for i in range(1,n+1):
            print(str(i),end='')
"""
end='' tells Python not to add a newline or space after printing
So when the loop runs,
They are printed continuously on the same line, forming one output string.
"""