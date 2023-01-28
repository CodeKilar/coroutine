import time

def generator():
	print("generator begin")
	y = 2
	x = yield y
	print("generator end x:%s y=%s" % (x, y))
	time.sleep(1)
	x = 19

gen = generator()
result = next(gen) # 运行到yield的地方
y = gen.send(10)    # 从yield处继续执行下去
print(y)
