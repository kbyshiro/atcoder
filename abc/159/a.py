def main():
    import sys
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    print(int(n*(n-1)/2 + m*(m-1)/2))


if __name__ == '__main__':
    main()