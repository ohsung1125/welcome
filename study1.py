# open(): 파일을 특정한 모드로 여는 함수
# 읽을때는 r, 쓸 때는 w
# readline() : 파일 객체로부터 한 줄씩(\n) 문자열을 읽는 함수
# readlines() : 전체 내용을 한번에 [리스트]에 담는 함수
f= open("input.txt","r", encoding="UTF-8")
# f : 파일 객체 -> intput.txt를 읽기
#f.seek(9)
#f.seek() : 읽을 위치를 선정해주는 함수 (한 한글문자당 3byte씩 할당)
count= 0
while count <3:
    data=f.readline()
    count++1
    print("%d 번째 줄: %s" %(count,data), end='')


data = f.read()
print(data)

f.close() # 해당 파일에 대한 리소스(메모리 할당) 사용이 끝남
