list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']


rental = '모든 도서가 대여 가능한 상태입니다.'

missing_book = [rental_book[i] for i in range(len(rental_book)) if bool(rental_book[i] in list_of_book)==False]

for i in range(len(rental_book)):
    if rental_book[i] in list_of_book:
        if i == len(rental_book)-1:
            print('모든 도서가 대여 가능한 상태입니다.')
            break
        else:
            continue
    else:
        for k in range(len(missing_book)):
            print(f'{missing_book[k]} 을/를 보충하여야 합니다.')
        break


# Review of Professor
# 방법 1
missing_book = [book for book in rental_book if book not in list_of_book]  
# rental_book의 각 요소인 book[i]에 대해 book이 list_of_book에 없다면 missing_book에 집어넣겠다.

if missing_book :
    for missing in missing_book :
        print(f"{missing} 을/를 보충하여야 합니다.")
else:
    print("모든 도서가 대여 가능합니다.")