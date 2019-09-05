import numpy as np

def p_box(key, values):
	li = [0 for _ in range(len(key))]
	for i,ele in enumerate(key):
		li[i] = value[ele]
	return li

def left_shift(key):
	return [key[-1]]+key[:len(key)-1]

def gen_keys(key):
	assert len(key)==10
	key = p_box([3,5,2,7,4,10,1,9,8,6], key)
	part1 = left_shift(key[:5])
	part2 = left_shift(key[5:])
	key1 = p_box([6,3,7,4,3,5,10,9], part1+part2)
	part1 = left_shift(part1)
	part2 = left_shift(part2)
	key2 = p_box([3,1,7,6,8,4,10,2], part1+part2)
	return key1, key2

def main():
	print("Welcome to world's most secure ")
