#!/usr/bin/python3
numbers = [(dig, git) for dig in range(0, 9) for git in range(dig+1, 10)]
output = ", ".join(["{}{}".format(dig, git) for dig, git in numbers])
print(output)
