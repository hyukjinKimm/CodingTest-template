a = [0, 1, 2, 3, 4, 5]
# s인덱스 부터 e 인덱스 까지(포함) 의 중앙 구하기 
s = 1 
e = 4 
R = (e-s+1)//2  # 짝수개에선 중앙에서 오른쪽 인덱스 
L = (e-s)//2 # 짝수개에선 중앙에서 왼쪽 인덱스 
# 홀수개 원소면  둘다 중앙이 나옴 

# s 인덱스를 처음에 더해줘야함 !!
print(s+R) # s + R 인덱스 가! 중앙 오른쪽꺼
print(s+L) # s + L 인덱스 가! 중앙 왼쪽꺼

