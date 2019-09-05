import numpy as np

expansion_key=[4,1,2,3,2,3,4,1]
s_key1=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
s_key2=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
straight_key1=[1,3,4,2]

def expansion_box(key, value):
	sol=[value[key[i]-1] for i in range(len(key))]
	return sol

def sbox(key, a):
	x,y=int('0b'+str(a[0])+str(a[3]),2),int('0b'+str(a[1])+str(a[2]),2)
	sol=bin(key[x][y])[2:]
	return [int(sol[0]),int(sol[1])]

def xor(a, b):
	return [a[i]^b[i] for i in range(len(a))]

def sdes_fun(key, right):
	ex_right=expansion_box(key, right)
	xor_right=xor(a,ex_right)
	s_right=sbox(xor_right[:4],s_key1) + sbox(xor_right[4:],s_key2)
	straight_right=expansion_box(straight_key1, s_right)
	return straight_right

def round(key, a):
	left,right=a[:4],a[4:]
	right1= sdes_fun(key, right)
	return right, xor(left, right1)



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

