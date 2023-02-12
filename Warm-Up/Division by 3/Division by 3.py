import os
import sys
import time

DEBUG = os.getenv("_DEBUG")
if DEBUG:
    input = open("cmake-build-debug/input.txt", "r").readline
    # sys.stdout = open("output.txt", 'w')
else:
    input = sys.stdin.readline
    output = sys.stdout.write

def main(tc):
    a, b = map(int, input().split())
    def calc(n):
        ans = n // 3 * 2
        if n % 3 == 2:
            ans += 1
        return ans

    print(calc(b) - calc(a - 1))



if __name__ == '__main__':
    start_time = time.time()
    T = 1
    T = int(input())
    for tc in range(1, T + 1):
        print("Case %d:" % tc, end=' ')
        main(tc)
    if DEBUG:
        print("\n--- %0.0f ms ---" % ((time.time() - start_time) * 1000))
