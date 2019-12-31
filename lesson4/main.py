from os import system, name

from lesson4.services.news_service import NewsService

__service = NewsService()

def main():
    __show_main_menu()

def __show_main_menu():
    __clear_screen()
    print('--- Главное меню ---')
    print('1. Синхронизация новостей')
    print('2. Показать новости')
    print('0. Выход')
    answer = int(input('Ваш выбор: '))
    if not __check_input(answer):
        __show_main_menu()
        return
    __action(answer)

def __check_input(answer):
    right_answers = [0, 1, 2]
    if answer not in right_answers:
        print('Ваш выбор не правильный')
        return False
    return True

def __clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def __action(action_type):
    if action_type == 1:
        __service.sync_news()
    elif action_type == 2:
        items = __service.get_news()
        __show_news(items)
    elif action_type == 0:
        quit(0)
    else:
        print('Ваш выбор не правильный')
    __show_main_menu()

def __show_news(items):
    for item in items:
        print(item.title)
        print(item.source)
        print(item.link)
        print(item.publication_date)
        print(10 * '-')


if __name__ == '__main__':
    main()
