import json

import requests


class GitHubRepository:
    _base_url = 'https://api.github.com'

    def getUserRepositories(self, user_name):
        url = f"{self._base_url}/users/{user_name}/repos"
        response = requests.get(url)
        if response.ok:
            result = []
            items = json.loads(response.text)
            for item in items:
                result.append(item['name'])

            return result
        else:
            return []

def main():
    repository = GitHubRepository()
    result = repository.getUserRepositories('nonamemanah')
    for item in result:
        print(item)


if __name__ == '__main__':
    main()
