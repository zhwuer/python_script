import wda
from tqdm import tqdm

c = wda.Client('http://localhost:8100/')
s = c.session()
total = 0
try:
    while (True):
        s.swipe_left()
        s.swipe_left()
        s.tap(300, 700)
        s.tap(375, 200)
        s.tap(375, 400)
        s.tap(50, 80)
        tapCount = 300
        for i in tqdm(range(tapCount)):
            s.tap(330, 730)
        total += i/2
        s.tap(530, 730)
        s.tap(725, 1300)
        s.swipe_right()
        s.swipe_right()
        s.tap(300, 700)
        s.tap(600, 170)
        s.tap(375, 700)
        s.tap(375, 670)
        s.tap(725, 1300)
except KeyboardInterrupt:
    total += i/2
    print("总共增加了%d点铸造经验" % total)