#coding: cp949

addmission=0
rank="노인"
ticket_free=3
ticket_discount=5
ticket_count=0

while ticket_free!=0:
    ticket_count+=1
    age=int(input("나이를 입력하세요. : "))

    while True:
        if age<0:
            age=int(input("나이를 다시 입력하세요. :"))
        else:
            if age<4 :
                addmission=0
                rank="유아"
            elif age<14 :
                addmission=2000
                rank="어린이"
            elif age<19 :
                addmission=3000
                rank="청소년"
            elif age<66 :
                addmission=5000
                rank="성인"
            else:
                addmission=0
        
            if addmission==0:
                print("귀하는",rank,"등급이며, 요금은 무료 입니다.")
                ticket_count-=1
                break
            else:
                print("귀하는",rank,"등급이며, 요금은 ",addmission,"원 입니다.")
                pay_type=int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용 카드): "))

                if pay_type==1:
                    pay=int(input("요금을 입력하세요. :"))
                    if pay<addmission:
                        print(addmission-pay,"원 모자랍니다. 입력하신",pay,"원을 반환합니다.")
                        ticket_count-=1                       
                    elif pay==addmission:
                        print("감사합니다. 티켓을 발행합니다.")
                    else:
                        print("감사합니다. 티켓을 발행하고 거스름돈",pay-addmission,"원을 반환합니다.")
                elif pay_type==2:
                    print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
                    if 60<=age<=65:
                        print(int(addmission*0.9*0.95),"원 결제 되었습니다. 티켓을 발행합니다.")
                    else:
                        print(int(addmission*0.9),"원 결제 되었습니다. 티켓을 발행합니다.")
                break
               
    if ticket_count==0:
        continue
    elif ticket_count%7==0:
        ticket_free-=1
        print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓:",ticket_free,"장")
    elif ticket_count%4==0:
        ticket_discount-=1
        print("축하합니다. 연간회원권 구매 이벤트에 당첨되었습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓:",ticket_discount,"장")
    else:
        continue
        
