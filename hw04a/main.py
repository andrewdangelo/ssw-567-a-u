# Want to get: list of repos and # of commits per repo

import json
import requests
import urllib.parse


def getUserRepos(userId):
    response = requests.get('https://api.github.com/users/' + userId + '/repos').json()
    repos = []
    if response:
        for repo in response:
            response_commits = requests.get(
                'https://api.github.com/repos/' + userId + '/' + repo["name"] + '/commits').json();
            if response_commits:
                repos.append("Repo: " + repo["name"] + " Number of commits: " + str(len(response_commits)))
            else:
                print("error retrieving data")
        return repos

    else:
        print("Error retrieving data")


print(getUserRepos('andrewdangelo'))
