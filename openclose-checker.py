# coding=utf-8


def yes_no_input():
    while True:
        choice = raw_input("This will read open or close information 'Type anything': ").lower()
        if choice in ['運行', '全面滑走可能', '平常運転','○','● ','open','OPEN','Open','◎','◯','一部滑走可能']:
            return True
        elif choice in ['運休','時間外','運転見合わせ','close','CLOSE','Close','－','×','-','営業終了','ー']:
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('リフト運行中')
    else:
        print('運休')
