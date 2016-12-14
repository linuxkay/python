# coding=utf-8


def yes_no_input():
    while True:
        choice = raw_input("This will read open or close information 'Type anything': ").lower()
        if choice in ['運行', '全面滑走可能', '平常運転','○','yes','ya']:
            return True
        elif choice in ['close','CLOSE','－','No','-']:
            return False


if __name__ == '__main__':
    if yes_no_input():
        print('運営中')
    else:
        print('運休')
