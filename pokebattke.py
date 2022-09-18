#!/usr/bin/env python
import random


A=[202,200,116,169,100,15,4,15,4]
NameA='裂咬陸鯊'
B=[146,150,106,200,90,17,12,17,12]
NameB='卡璞鳴鳴'
C=[136,222,170,58,80,7,8,7,8]
NameC='堅盾劍怪'
D=[155,218,111,143,100,4,2,4,2]
NameD='土地雲'

Alt=[[1,1,1,1,1,1/2,1,0,1/2,1,1,1,1,1,1,1,1,1],[2,1,1/2,1/2,1,2,1/2,0,2,1,1,1,1,1/2,2,1,2,1/2],[1,2,1,1,1,1/2,2,1,1/2,1,1,2,1/2,1,1,1,1,1],[1,1,1,1/2,1/2,1/2,1,1/2,0,1,1,2,1,1,1,1,1,2],[1,1,0,2,1,2,1/2,1,2,2,1,1/2,2,1,1,1,1,1],[1,1/2,2,1,1/2,1,2,1,1/2,2,1,1,1,1,2,1,1,1],[1,1/2,1/2,1/2,1,1,1,1/2,1/2,1/2,1,2,1,2,1,1,2,1/2],[0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1/2,1],[1,1,1,1,1,2,1,1,1/2,1/2,1/2,1,1/2,1,2,1,1,2],[1,1,1,1,1,1/2,2,1,2,1/2,1/2,2,1,1,2,1/2,1,1],[1,1,1,1,2,2,1,1,1,2,1/2,1/2,1,1,1,1/2,1,1],[1,1,1/2,1/2,2,2,1/2,1,1/2,1/2,2,1/2,1,1,1,1/2,1,1],[1,1,2,1,0,1,1,1,1,1,2,1/2,1/2,1,1,1/2,1,1,],[1,2,1,2,1,1,1,1,1/2,1,1,1,1,1/2,1,1,0,1],[1,1,2,1,2,1,1,1,1/2,1/2,1/2,2,1,1,1/2,2,1,1],[1,1,1,1,1,1,1,1,1/2,1,1,1,1,1,1,2,1,0],[1,1/2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1/2,1/2],[1,2,1,1/2,1,1,1,1,1/2,1/2,1,1,1,1,2,2,1]]

def type (A,B):
	x1=Alt[A[5]][B[7]]*Alt[A[5]][B[8]]
	x2=Alt[A[6]][B[7]]*Alt[A[6]][B[8]]
	if x1 >= x2:
		x3 = x1
	else:
		x3 = x2
	return x3
	
	
def damage(X):
	return (0.44*(X[1]/X[2])*(X[4])+2)

def FFF (P1,P2):
	Ia=0
	Ib=0
	hp1=P1[0]
	hp2=P2[0]
	Win=0
	while hp1 > 0:
		hp1=hp1-damage(P2)*type(P1,P2)
		Ia=Ia+1
	
	while hp2 > 0:
		hp2=hp2-damage(P1)*type(P1,P2)
		Ib=Ib+1
	
	if P1[3] > P2[3]:
		Ib=Ib+1
	else:
		Ia=Ia+1
		
	if P1[3] > P2[3]:
		if Ib == Ia:
			win=0
		else:
			win=1
	else :
		if Ib==Ia:
			win=1
		else:
			win=0
	return win

if FFF(A,B) + FFF(A,C) + FFF(A,D) > 0:
	print(NameA,"打贏了")
	if FFF(A,B) == 1:
		print(NameB)

	if FFF(A,C) == 1:
		print(NameC)

	if FFF(A,D) == 1:
		print(NameD)
else:
	print(NameA,"很爛，全輸")
print()

if FFF(B,A) + FFF(B,C) + FFF(B,D) > 0:
	print(NameB,"打贏了")
	if FFF(B,A) == 1:
		print(NameA)

	if FFF(B,C) == 1:
		print(NameC)

	if FFF(B,D) == 1:
		print(NameD)
else:
	print(NameB,"很爛，全輸")
print()
	
if FFF(C,A) + FFF(C,B) + FFF(C,D) > 0:
	print(NameC,"打贏了")
	if FFF(C,A) == 1:
		print(NameA)

	if FFF(C,B) == 1:
		print(NameB)

	if FFF(C,D) == 1:
		print(NameD)
else:
	print(NameC,"很爛，全輸")
print()

if FFF(D,A) + FFF(D,B) + FFF(D,C) > 0:
	print(NameD,"打贏了")
	if FFF(D,A) == 1:
		print(NameA)

	if FFF(D,B) == 1:
		print(NameB)

	if FFF(D,C) == 1:
		print(NameC)
else:
	print(NameD,"很爛，全輸")
print()

print('試試看')











