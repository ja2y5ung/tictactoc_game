
#-*- coding=cp949 
#-*- coding: euc-kr
##한글 주석 사용

# 터틀을 t라는 이름으로 사용
import turtle as t
# random 선언
import random

t.pencolor("black")

# 사각형 9개 그리는 함수(왼쪽 위가 첫 번째 사각형)
def draw_board():
    t.hideturtle()
    # 창 크기 
    x = 500
    y = 500
    # 사각형을 반복하여 그릴때 간격, 첫 사각형 위치
    interval_y = 153.3
    interval_x = interval_y
    t.speed(0)
    t.setup(x,y)
    x = 230*(-1)
    y = 230
    # 사각형 1개를 9번 반복해서 그림
    for i in range(0,3):
        for j in range(0,3):
            t.penup()
            t.goto(x,y)
            t.pendown()
            t.goto(x+interval_x,y)
            t.goto(x+interval_x,y-interval_y)
            t.goto(x,y-interval_y)
            t.goto(x,y)
            x = x + interval_x
        y = y - interval_y
        interval_x = interval_x*(-1)
    # pen 사용하고 나서는 항상 penup()
    t.penup()
    
# number 값으로 받은 정수와 같은 위치의 x,y좌표 반환 함수
def squareNo(number):
    # 각각의 사각형  x,y 값 위해 다차리스트 2개 선언 후 임의의 값 넣어줌
    matrix_x = [[1,2,3],[4,5,6],[7,8,9]]
    matrix_y = [[1,2,3],[4,5,6],[7,8,9]]
    count = 1
    t.speed(0)
     # 사각형을 반복하여 그릴때 간격, 첫 사각형 중앙 점
    interval_y = 153.3
    interval_x = interval_y
    x = 230*(-1)
    y = 230
    x = x + interval_x/2 
    y = y - interval_y/2
    # number 값으로 받은 정수와 같은 위치의 x,y좌표 반환
    for i in range(0,3):
        for j in range(0,3):
            t.goto(x,y)
            matrix_x[i][j] = x
            matrix_y[i][j] = y
            x = x + interval_x
            # number 값과 같으면 x,y 반환
            if(number == count):
                return matrix_x[i][j],matrix_y[i][j]
            count += 1
        # 1,2,3 번째가 끝나면 다시 다음 줄 왼쪽 부터 4,5,6 하기위해 x 값 왼쪽으로 옮김
        for j in range(0,3):
            x = x - interval_x
            t.goto(x,y)
        y = y - interval_y

# O 그리는 함수
def draw_circle(x,y):
    # 사각형 중앙에 그려주기 위해 y값 조정
    y = y-60
    t.goto(x,y)
    t.pendown()
    t.circle(60)
    t.penup()

# X 그리는 함수 
def draw_X(x,y):
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(80)
    t.penup()
    # 사각형 중앙을 기준으로 45도씩 선 4개 그림
    for i in range(0,3):
        t.goto(x,y)
        t.right(90)
        t.pendown()
        t.forward(80)
        t.penup()
    t.right(45)

# 사람(human)한테 값 입력 받아 정해진 위치에 O 그려줌
def human(square_H,square_C):
    i = 1
    while  i == 1:
        number_H = int(input("번호를 입력하세요(1~9) : "))
        # 입력 받은 값이(1~9) 사이이고 X를 이미 그린 위치가 아니면 실행
        if (number_H in square_H)&(square_C[number_H-1] != "C"):
            # 입력 받은 값에 대한 x,y 값을 반환해주는 함수 호출
            x,y = squareNo(number_H)
            # 해당 x,y 값에 O그려줌
            draw_circle(x,y)
            # 그려준 후에는 중복으로 그려지는 것을 막기위해 "H"라는 값을 임의로 넣어줌
            square_H[number_H-1] = "H"
            i = 0
            return square_H,number_H
        else:
            # (1~9) 사이 값이 아니거나 중복이면 다시 입력하게 함
            print("\n잘못된 입력값입니다.\n")

# 컴퓨터(computer)가 임의로 값을 생성하여 X 그려줌            
def computer(square_H,square_C):
    i = 1
    while i == 1:
        # (1~9) 사이 임의의 랜덤 값 
        number_C = random.randint(1,9)
        # 랜덤 값이 square_C 에 존재하고 O를 이미 그린 위치가 아니면 실행
        if (number_C in square_C)&(square_H[number_C-1] != "H"):
            # 랜덤 값에 대한 x,y 값을 반환해주는 함수 호출
            x,y = squareNo(number_C)
            # 해당 x,y 값에 X그려줌
            draw_X(x,y)
            # 그려준 후에는 중복으로 그려지는 것을 막기위해 "C"라는 값을 임의로 넣어줌
            square_C[number_C-1] = "C"
            i = 0
            return square_C,number_C
        else:
            # 랜덤 값이 square_C 에 존재하지 않거나 중복이면 다시 입력하게 함
            i = 1
# 사람(human)이 이기는 경우를 판별하는 함수
def human_win(square_H):
    # 가로 줄이 모두 O로 채워진 경우 판별
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # 가로 줄의 세개의 값이 "H"로 모두 같다면 0 반환
            if (square_H[a] == 'H' and square_H[a+1]=='H') and (square_H[a+1] =='H'and square_H[a+2]=='H'):
                return 0
        # 다음 줄로 이동
        a += 3
        
    # 다음 줄로 이동하는 a 값 초기화
    # 세로 줄이 모두 O로 채워진 경우 판별
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # 세로 줄의 세개의 값이 "H"로 모두 같다면 0 반환
            if (square_H[a] == 'H' and square_H[a+3]=='H') and (square_H[a+3] =='H'and square_H[a+6]=='H'):
                return 0
        # 다음 줄로 이동
        a +=1
        
    # 대각 선 줄이 모두 O로 채워진 경우 판별

    # 왼쪽 대각선 줄의 세개의 값이 "H"로 모두 같다면 0 반환
    if (square_H[0] =='H' and square_H[4]=='H') and (square_H[4] =='H' and square_H[8]=='H'):
        return 0
    # 오른쪽 대각선 줄의 세개의 값이 "H"로 모두 같다면 0 반환
    elif (square_H[2] =='H' and square_H[4]=='H') and (square_H[4] =='H' and square_H[6]=='H'):
        return 0

# 컴퓨터(computer)이 이기는 경우를 판별하는 함수
def computer_win(square_C):
    # 가로 줄이 모두 X로 채워진 경우 판별
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # 가로 줄의 세개의 값이 "C"로 모두 같다면 0 반환
            if (square_C[a] == 'C' and square_C[a+1]=='C') and (square_C[a+1] =='C'and square_C[a+2]=='C'):
                return 0
        # 다음 줄로 이동
        a += 3
    # 다음 줄로 이동하는 a 값 초기화
    # 세로 줄이 모두 O로 채워진 경우 판별
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # 세로 줄의 세개의 값이 "C"로 모두 같다면 0 반환
            if (square_C[a] == 'C' and square_C[a+3]=='C') and (square_C[a+3] =='C'and square_C[a+6]=='C'):
                return 0
        # 다음 줄로 이동
        a +=1

        
    # 대각 선 줄이 모두 X로 채워진 경우 판별

    # 왼쪽 대각선 줄의 세개의 값이 "C"로 모두 같다면 0 반환    
    if (square_C[0] =='C' and square_C[4]=='C') and (square_C[4] =='C' and square_C[8]=='C'):
        return 0
    # 오른쪽 대각선 줄의 세개의 값이 "C"로 모두 같다면 0 반환
    elif (square_C[2] =='C' and square_C[4]=='C') and (square_C[4] =='C' and square_C[6]=='C'):
        return 0

# 수 무르기 함수
def cancel(square_H,square_C,number_H,number_C):
    # O 지우기(human)
    
    # 바로 직전에 number_H 값 사용 하여 직전에 그려진 곳과 동일한 x,y 값 사용
    x,y = squareNo(number_H)
    y = y-60
    t.goto(x,y)
    # 같은 위치에 횐색으로 그려줌
    t.pencolor("white")
    t.pendown()
    t.circle(60)
    t.penup()
    # 같은 위치에 다시 수를 둘 수 있게 "H" 였던 값을 number_H(숫자) 값으로 변경
    square_H[number_H-1] = number_H

    # X 지우기(computer)

    # 바로 직전에 number_C 값 사용 하여 직전에 그려진 곳과 동일한 x,y 값 사용
    x,y = squareNo(number_C)
    t.goto(x,y)
    # 같은 위치에 횐색으로 그려줌
    t.pencolor("white")
    t.right(45)
    t.pendown()
    t.forward(80)
    t.penup()
    for i in range(0,3):
        t.goto(x,y)
        t.right(90)
        t.pendown()
        t.forward(80)
        t.penup()
    t.right(45)
    # 같은 위치에 다시 수를 둘 수 있게 "C" 였던 값을 number_C(숫자) 값으로 변경
    square_C[number_C-1] = number_C
    
    # pencolor를 원래대로 변경
    t.pencolor("black")

# main 함수
def main():
    # 전체 틀을 그려주는 함수 호출
    draw_board()
    square_H = [1,2,3,4,5,6,7,8,9]
    square_C = [1,2,3,4,5,6,7,8,9]
    number_H = 0
    number_C = 0
    # 그려주는 O,X 만 진하게 그리위해 이 위치에 선언
    t.pensize(10)
    count = 0
    while 1:
        # 처음으로 사람(human)이 먼저 수를 둠
        square_H,number_H = human(square_H,square_C)
        # human_win() 에서 0을 반환받으면 이기는 경우
        if 0==human_win(square_H):
            print("승리했습니다.")
            break
        # 사람이 먼저 수를 두므로 무승부일 경우 항상 square_H[]안에 그림 O 의값 즉 "H"의 개수가 5개임
        for i in range (0,9):
            if square_H[i] == "H":
                count = count + 1
                #square_H[]안에 O 의값 즉 "H"의 개수가 5개 일 경우 무승부
                if count == 5:
                    print("무승부입니다.")
                    break
        count = 0

        # 컴퓨터(computer)가 랜덤하게 X를 그림
        square_C,number_C = computer(square_H,square_C)
        # computer_win() 에서 0을 반환받으면 패배하는 경우
        if 0==computer_win(square_C):
            print("패배했습니다.")
            break
        
        # 0 입력하면 수 무르는 함수 호출, 아닐 경우는 임의로 1 입력하게 함
        back = int(input("\n무르려면 0을 입력하세요.\n아니면 1 입력\n"))
        if back == 0:
            cancel(square_H,square_C,number_H,number_C)
    #tertle 종료 선언
    t.done()
#main 함수 호
main()


