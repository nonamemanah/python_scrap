from lesson4.repositories.mail_repository import MailRepository


def main():
    repository = MailRepository()
    news_items = repository.get_data()
    for item in news_items:
        print(item)

if __name__ == '__main__':
    main()
