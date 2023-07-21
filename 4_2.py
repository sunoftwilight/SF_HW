list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기'] 

for i in range(len(rental_book)):
    if rental_book[i] in list_of_book:
        if i == len(rental_book)-1:
            print('모든 도서가 대여 가능한 상태입니다.')
            break
        else:
            continue
    else:
        print(f'{rental_book[i]}은/는 보유하고 있지 않습니다')
        break


# Review of Professor
# 방법 1
is_rental = False               # 모든 도서가 렌탈이 가능한지 여부
for rental in rental_book:
    is_book = False             # 렌탈북이 북리스트에 보유 중인지의 여부
    for book in list_of_book:
        if rental == book :
            is_book = True
            is_rental = True   
            break
    if not is_book :            # 북리스트에 없을 경우에 출력
        print(f'{rental}은/는 보유하고 있지 않습니다.')
        break
if is_rental :
    print('모든 도서가 대여 가능한 상태입니다.')


# # 방법 2
is_rental = True
for rental  in rental_book :
    if rental not in list_of_book:
        print(f'{rental} 은/는 보유하고 있지 않습니다.')
        is_rental = False
if is_rental :
        print('모든 도서가 대여 가능한 상태입니다.')
