# -*- coding: utf-8 -*-
# @Time : 2023/1/28 23:04
# @Author : 曾得鹿
# @File : pro-con.py

import time


def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		
		print("consuming %s " % n)
		time.sleep(1)
		r = "ok"


def producer(gen):
	next(gen)
	n = 0
	while n < 5:
		n += 1
		print("produce %s " % n)
		result = gen.send(n)
		print("consumer return %s " % result)
	gen.close()
	

if __name__ == '__main__':
	gen = consumer()
	producer(gen)
