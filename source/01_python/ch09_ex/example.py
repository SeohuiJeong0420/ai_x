from customer import load_customers
from functions import fn1_insert_customer_info, fn2_print_customers
from functions import fn3_delete_customer, fn4_search_customer, fn5_save_customer_csv
from functions import fn9_save_customer_txt
def main():
    global customer_list
    customer_list = load_customers() # ch09_customers.txt의 내용을 load
    while True:
        print("1:입력|2:전체출력|3:삭제|4:이름검색|5:csv내보내기|9: 종료", end='')
        fn = input('메뉴선택 :')
        if fn == '1':
            #print('f1_호출한 결과를 customer에 받아 customer_lsit에 append')
            customer = fn1_insert_customer_info() #입력받은 내용으로 customer 객체를 반환
            customer_list.append(customer)
        elif fn == '2':
            #print('f2_호출')
            fn2_print_customers(customer_list)
        elif fn == '3':
            #print('f3_호출')
            fn3_delete_customer(customer_list)
        elif fn == '4':
            #print('f4_호출')
            fn4_search_customer(customer_list)
        elif fn == '5':
            #print('f5_호출')
            fn5_save_customer_csv(customer_list)
        elif fn == '9':
            #print('f9_호출')
            fn9_save_customer_txt(customer_list)
            break

if __name__ == '__main__':
    print(1)
    main()