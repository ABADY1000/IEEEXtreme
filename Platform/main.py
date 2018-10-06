from collections import namedtuple

LINE_NUMBER, BALLS_NUMBER = (int(x) for x in input().split())

line = namedtuple('ball', ['start', 'end', 'length'])

lines = []
for _ in range(LINE_NUMBER):
    start, end = (int(x) for x in input().split())
    lines.append(line(start, end, abs(start - end)))

balls = (int(x) for x in input().split())

def numberOfFallBall(aline:line):
    isThere = False
    for ball in balls:

        if ball >= aline.start and ball <= aline.end:
            isThere = True
            yield ball
    if not isThere :
        return None

def moveLeftCost(aball:line):
    pass


print(list(numberOfFallBall(lines[0])))
    

