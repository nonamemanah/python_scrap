from pprint import pprint

from lesson4.services.news_service import NewsService


def main():
    __service = NewsService()
    '''__service.sync_news()'''
    items = __service.get_news()
    for item in items:
        pprint(item)


if __name__ == '__main__':
    main()
