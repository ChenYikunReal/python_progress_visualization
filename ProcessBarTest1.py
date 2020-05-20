import time
import progressbar

p = progressbar.ProgressBar()
n = 10

# 加上进度,就是将range(n)放到ProgressBar()中
for i in p(range(n)):
    # 每次延时0.1s
    time.sleep(0.1)
