#!/usr/bin/python3
for ch in reversed(range(97, 123)):
    print("{:c}".format(ch if (ch % 2 == 0) else (ch - 32)), end='')

#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format((c - (ord('a') - ord('A'))) if c % 2 else c), end='')