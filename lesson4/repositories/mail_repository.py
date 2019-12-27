from lesson4.repositories.repository import Repository


class MailRepository(Repository):
    def __init__(self):
        self.base_url = 'https://mail.ru'

