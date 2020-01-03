import hashlib
import random

num = 0
temp = 0
masterpassword = '629'
dic = {'naver': 'naver12', 'daum': 'daum12'}


def xor(value) :    
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(value,masterpassword));

'''
    위 return부분 코드가 아래 주석 코드와 같은 역할을 수행함 (파이썬 한줄 코딩 문법)
    
    먼저 ord()함수는 문자 'a'를 ord(a)하면 a의 유니코드 숫자로 변환
    chr()은 유니코드로 변환된 숫자를 다시 문자열로 변환
    join() 함수는 dic ['a', 'b', 'c']가 있다 할때 조인앞에 '+'가있으면
    a+b+c의 하나의 문자열로 합쳐줌 만약 ''이면?
    abc로 합쳐짐
    zip()함수 a = [1,2,3] b = [4, 5, 6] 이면 zip함수가 1,4를 한번에 2,5를 3,6이렇게
    묶어주는 역할을 함
    
    result = '';
    for a,b in zip(value,masterpassword) :
        result += chr(ord(a) ^ ord(b));
    return result;
'''

def choice(x):
    nu = [1,2,3,4,5,6,7,8,9,0]
    upe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    loe = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    spe = ['!','@','#','$','%','^','&','*']
    
    rand = random.randrange(1,x-2);
    character = rand;

    rand = random.randrange(1,x-character-1);
    upper = rand;
    
    rand = random.randrange(1,x - character - upper);
    lower = rand;

    number = x - character - upper - lower;

    print("비밀번호의 길이 : ",x);
    print("\n특수문자 길이 : ", character);
    print("\n대문자 길이 : ", upper);
    print("\n소문자 길이 : ", lower);
    print("\n숫자 길이 : ", number);
    stringvalue = ''

    while 1 :

        value = random.randrange(1,5)
        if value == 1 and character > 0:
            stringvalue += spe[random.randrange(0,7)];
            character-=1;

        elif value == 2 and upper > 0:
            stringvalue += upe[random.randrange(0,25)];
            upper-=1;

        elif value == 3 and lower > 0:
            stringvalue += loe[random.randrange(0,25)];
            lower-=1;

        elif value == 4 and number > 0:
            stringvalue += str(nu[random.randrange(0,9)]);
            number-=1;

        elif character == 0 and upper == 0 and lower == 0 and number == 0:
            break;

    return stringvalue;

while 1 :
    print("사용할 번호를 입력하세요 \n");
    print("1 : 모든 비밀번호 해시 값 보기 \n");
    print("2 : 평상시 비밀번호 보기 \n");
    print("3 : 안전한 비밀번호 추천 받기 \n");
    print("4 : 3자리 숫자 / 소문자 / 대문자 찾기 \n");

    num = int(input());

    print("==============================");

    if num == 1:
        print("마스터 비밀번호를 입력하세요 \n");
        temp = input();
        if temp == masterpassword :
            print("naver : " , hashlib.sha256(dic['naver'].encode()).hexdigest());
            print("daum : " , hashlib.sha256(dic['daum'].encode()).hexdigest());
        else :
            print("비밀번호 오류 다시 진행 해주세요!\n");
            
    elif num == 2 :
        
        print("naver : " , xor(dic['naver']));
        print("naver : " , xor(dic['daum']));

    elif num == 3 :
        print("비밀번호 추천 받기 \n");
        x = random.randrange(4,10);
        print("\n비밀번호 : ", choice(x),"\n");

    elif num == 4 :
        print("3 \n");

    print("==============================");