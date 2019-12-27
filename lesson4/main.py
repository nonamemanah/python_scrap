from lesson4.repositories.mail_repository import MailRepository


def main():
    repository = MailRepository()
    repository.get_data()


if __name__ == '__main__':
    main()
