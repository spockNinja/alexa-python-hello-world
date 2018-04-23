import requests

GITHUB_API = 'https://api.github.com'
REPO_SEARCH = GITHUB_API + '/search/repositories'


def search_repositories(query):
    search_params = {
        'q': query
    }
    search_response = requests.get(REPO_SEARCH, params=search_params)
    return search_response.json()
