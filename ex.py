
#-*- coding=cp949 
#-*- coding: euc-kr
##�ѱ� �ּ� ���

# ��Ʋ�� t��� �̸����� ���
import turtle as t
# random ����
import random

t.pencolor("black")

# �簢�� 9�� �׸��� �Լ�(���� ���� ù ��° �簢��)
def draw_board():
    t.hideturtle()
    # â ũ�� 
    x = 500
    y = 500
    # �簢���� �ݺ��Ͽ� �׸��� ����, ù �簢�� ��ġ
    interval_y = 153.3
    interval_x = interval_y
    t.speed(0)
    t.setup(x,y)
    x = 230*(-1)
    y = 230
    # �簢�� 1���� 9�� �ݺ��ؼ� �׸�
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
    # pen ����ϰ� ������ �׻� penup()
    t.penup()
    
# number ������ ���� ������ ���� ��ġ�� x,y��ǥ ��ȯ �Լ�
def squareNo(number):
    # ������ �簢��  x,y �� ���� ��������Ʈ 2�� ���� �� ������ �� �־���
    matrix_x = [[1,2,3],[4,5,6],[7,8,9]]
    matrix_y = [[1,2,3],[4,5,6],[7,8,9]]
    count = 1
    t.speed(0)
     # �簢���� �ݺ��Ͽ� �׸��� ����, ù �簢�� �߾� ��
    interval_y = 153.3
    interval_x = interval_y
    x = 230*(-1)
    y = 230
    x = x + interval_x/2 
    y = y - interval_y/2
    # number ������ ���� ������ ���� ��ġ�� x,y��ǥ ��ȯ
    for i in range(0,3):
        for j in range(0,3):
            t.goto(x,y)
            matrix_x[i][j] = x
            matrix_y[i][j] = y
            x = x + interval_x
            # number ���� ������ x,y ��ȯ
            if(number == count):
                return matrix_x[i][j],matrix_y[i][j]
            count += 1
        # 1,2,3 ��°�� ������ �ٽ� ���� �� ���� ���� 4,5,6 �ϱ����� x �� �������� �ű�
        for j in range(0,3):
            x = x - interval_x
            t.goto(x,y)
        y = y - interval_y

# O �׸��� �Լ�
def draw_circle(x,y):
    # �簢�� �߾ӿ� �׷��ֱ� ���� y�� ����
    y = y-60
    t.goto(x,y)
    t.pendown()
    t.circle(60)
    t.penup()

# X �׸��� �Լ� 
def draw_X(x,y):
    t.goto(x,y)
    t.right(45)
    t.pendown()
    t.forward(80)
    t.penup()
    # �簢�� �߾��� �������� 45���� �� 4�� �׸�
    for i in range(0,3):
        t.goto(x,y)
        t.right(90)
        t.pendown()
        t.forward(80)
        t.penup()
    t.right(45)

# ���(human)���� �� �Է� �޾� ������ ��ġ�� O �׷���
def human(square_H,square_C):
    i = 1
    while  i == 1:
        number_H = int(input("��ȣ�� �Է��ϼ���(1~9) : "))
        # �Է� ���� ����(1~9) �����̰� X�� �̹� �׸� ��ġ�� �ƴϸ� ����
        if (number_H in square_H)&(square_C[number_H-1] != "C"):
            # �Է� ���� ���� ���� x,y ���� ��ȯ���ִ� �Լ� ȣ��
            x,y = squareNo(number_H)
            # �ش� x,y ���� O�׷���
            draw_circle(x,y)
            # �׷��� �Ŀ��� �ߺ����� �׷����� ���� �������� "H"��� ���� ���Ƿ� �־���
            square_H[number_H-1] = "H"
            i = 0
            return square_H,number_H
        else:
            # (1~9) ���� ���� �ƴϰų� �ߺ��̸� �ٽ� �Է��ϰ� ��
            print("\n�߸��� �Է°��Դϴ�.\n")

# ��ǻ��(computer)�� ���Ƿ� ���� �����Ͽ� X �׷���            
def computer(square_H,square_C):
    i = 1
    while i == 1:
        # (1~9) ���� ������ ���� �� 
        number_C = random.randint(1,9)
        # ���� ���� square_C �� �����ϰ� O�� �̹� �׸� ��ġ�� �ƴϸ� ����
        if (number_C in square_C)&(square_H[number_C-1] != "H"):
            # ���� ���� ���� x,y ���� ��ȯ���ִ� �Լ� ȣ��
            x,y = squareNo(number_C)
            # �ش� x,y ���� X�׷���
            draw_X(x,y)
            # �׷��� �Ŀ��� �ߺ����� �׷����� ���� �������� "C"��� ���� ���Ƿ� �־���
            square_C[number_C-1] = "C"
            i = 0
            return square_C,number_C
        else:
            # ���� ���� square_C �� �������� �ʰų� �ߺ��̸� �ٽ� �Է��ϰ� ��
            i = 1
# ���(human)�� �̱�� ��츦 �Ǻ��ϴ� �Լ�
def human_win(square_H):
    # ���� ���� ��� O�� ä���� ��� �Ǻ�
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # ���� ���� ������ ���� "H"�� ��� ���ٸ� 0 ��ȯ
            if (square_H[a] == 'H' and square_H[a+1]=='H') and (square_H[a+1] =='H'and square_H[a+2]=='H'):
                return 0
        # ���� �ٷ� �̵�
        a += 3
        
    # ���� �ٷ� �̵��ϴ� a �� �ʱ�ȭ
    # ���� ���� ��� O�� ä���� ��� �Ǻ�
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # ���� ���� ������ ���� "H"�� ��� ���ٸ� 0 ��ȯ
            if (square_H[a] == 'H' and square_H[a+3]=='H') and (square_H[a+3] =='H'and square_H[a+6]=='H'):
                return 0
        # ���� �ٷ� �̵�
        a +=1
        
    # �밢 �� ���� ��� O�� ä���� ��� �Ǻ�

    # ���� �밢�� ���� ������ ���� "H"�� ��� ���ٸ� 0 ��ȯ
    if (square_H[0] =='H' and square_H[4]=='H') and (square_H[4] =='H' and square_H[8]=='H'):
        return 0
    # ������ �밢�� ���� ������ ���� "H"�� ��� ���ٸ� 0 ��ȯ
    elif (square_H[2] =='H' and square_H[4]=='H') and (square_H[4] =='H' and square_H[6]=='H'):
        return 0

# ��ǻ��(computer)�� �̱�� ��츦 �Ǻ��ϴ� �Լ�
def computer_win(square_C):
    # ���� ���� ��� X�� ä���� ��� �Ǻ�
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # ���� ���� ������ ���� "C"�� ��� ���ٸ� 0 ��ȯ
            if (square_C[a] == 'C' and square_C[a+1]=='C') and (square_C[a+1] =='C'and square_C[a+2]=='C'):
                return 0
        # ���� �ٷ� �̵�
        a += 3
    # ���� �ٷ� �̵��ϴ� a �� �ʱ�ȭ
    # ���� ���� ��� O�� ä���� ��� �Ǻ�
    a=0
    for i in range(0,3):
        for j in range(0,3):
            # ���� ���� ������ ���� "C"�� ��� ���ٸ� 0 ��ȯ
            if (square_C[a] == 'C' and square_C[a+3]=='C') and (square_C[a+3] =='C'and square_C[a+6]=='C'):
                return 0
        # ���� �ٷ� �̵�
        a +=1

        
    # �밢 �� ���� ��� X�� ä���� ��� �Ǻ�

    # ���� �밢�� ���� ������ ���� "C"�� ��� ���ٸ� 0 ��ȯ    
    if (square_C[0] =='C' and square_C[4]=='C') and (square_C[4] =='C' and square_C[8]=='C'):
        return 0
    # ������ �밢�� ���� ������ ���� "C"�� ��� ���ٸ� 0 ��ȯ
    elif (square_C[2] =='C' and square_C[4]=='C') and (square_C[4] =='C' and square_C[6]=='C'):
        return 0

# �� ������ �Լ�
def cancel(square_H,square_C,number_H,number_C):
    # O �����(human)
    
    # �ٷ� ������ number_H �� ��� �Ͽ� ������ �׷��� ���� ������ x,y �� ���
    x,y = squareNo(number_H)
    y = y-60
    t.goto(x,y)
    # ���� ��ġ�� Ⱥ������ �׷���
    t.pencolor("white")
    t.pendown()
    t.circle(60)
    t.penup()
    # ���� ��ġ�� �ٽ� ���� �� �� �ְ� "H" ���� ���� number_H(����) ������ ����
    square_H[number_H-1] = number_H

    # X �����(computer)

    # �ٷ� ������ number_C �� ��� �Ͽ� ������ �׷��� ���� ������ x,y �� ���
    x,y = squareNo(number_C)
    t.goto(x,y)
    # ���� ��ġ�� Ⱥ������ �׷���
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
    # ���� ��ġ�� �ٽ� ���� �� �� �ְ� "C" ���� ���� number_C(����) ������ ����
    square_C[number_C-1] = number_C
    
    # pencolor�� ������� ����
    t.pencolor("black")

# main �Լ�
def main():
    # ��ü Ʋ�� �׷��ִ� �Լ� ȣ��
    draw_board()
    square_H = [1,2,3,4,5,6,7,8,9]
    square_C = [1,2,3,4,5,6,7,8,9]
    number_H = 0
    number_C = 0
    # �׷��ִ� O,X �� ���ϰ� �׸����� �� ��ġ�� ����
    t.pensize(10)
    count = 0
    while 1:
        # ó������ ���(human)�� ���� ���� ��
        square_H,number_H = human(square_H,square_C)
        # human_win() ���� 0�� ��ȯ������ �̱�� ���
        if 0==human_win(square_H):
            print("�¸��߽��ϴ�.")
            break
        # ����� ���� ���� �ιǷ� ���º��� ��� �׻� square_H[]�ȿ� �׸� O �ǰ� �� "H"�� ������ 5����
        for i in range (0,9):
            if square_H[i] == "H":
                count = count + 1
                #square_H[]�ȿ� O �ǰ� �� "H"�� ������ 5�� �� ��� ���º�
                if count == 5:
                    print("���º��Դϴ�.")
                    break
        count = 0

        # ��ǻ��(computer)�� �����ϰ� X�� �׸�
        square_C,number_C = computer(square_H,square_C)
        # computer_win() ���� 0�� ��ȯ������ �й��ϴ� ���
        if 0==computer_win(square_C):
            print("�й��߽��ϴ�.")
            break
        
        # 0 �Է��ϸ� �� ������ �Լ� ȣ��, �ƴ� ���� ���Ƿ� 1 �Է��ϰ� ��
        back = int(input("\n�������� 0�� �Է��ϼ���.\n�ƴϸ� 1 �Է�\n"))
        if back == 0:
            cancel(square_H,square_C,number_H,number_C)
    #tertle ���� ����
    t.done()
#main �Լ� ȣ
main()


