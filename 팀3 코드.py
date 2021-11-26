import random

def num_1():
        return random.randrange(100,500)
def num_2():
        return random.randrange(100,500)
    
areas = ["서울",
         "경기",
         "충남",
         "충북",
         "경남",
         "경북",
         "전남",
         "전북",
         "제주"];

sum_n = 0
man = 0
woman = 0

while True:     
    hap = 0
    i = num_1()
    j = num_2()
    hap = i + j
    
    myarea=input(str(list(areas))+"중 지역을 선택하세요")
    if myarea in areas:
        print("%s의 총 확진자수는 %d명 성별에 따른 확진자수는 <남: %d명 , 여: %d명>입니다." %(myarea, hap,i,j))
        sum_n += hap
        man += i
        woman += j
    elif myarea=='':
        break
    else:
        print("지역을 다시 설정해주세요.")


print("현재까지의 코로나 확진자수 : %d명 <남 : %d명, 여: %d명>"%(sum_n, man ,woman))


if(man > woman):
    print("남자 확진자 수가 여자 확진자 수 보다 %d명 많습니다." %(man - woman))
elif(man == woman):
    print("남자 확진자 수가 여자 확진자 수가 같습니다")
else:
    print("여자 확진자 수가 남자 확진자 수 보다 %d명 많습니다." %(woman - man))


    
