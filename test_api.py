"""Модуль тестирует GitHub API на языке Python"""
import os
import requests
from dotenv import load_dotenv


load_dotenv()

GITHUB_USER = os.getenv('GITHUB_USER')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')
GITHUB_API_URL = "https://api.github.com/user/repos"


def create_repo(repo_name: str) -> bool:
    """
    Создает новый репозиторий на GitHub
    :param repo_name: имя репозитория
    :return True в случае успеха, иначе False
    """
    response = requests.post(
        GITHUB_API_URL,
        auth=(GITHUB_USER, GITHUB_TOKEN),
        json={"name": repo_name,
              "description": 'for fun and education', "private": False}
    )
    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
        return True
    else:
        print(f"Failed to create repository: {response.json()}")
        return False


def check_repo_exists(repo_name: str) -> bool:
    """
    Проверяет наличие репозитория на GitHub
    :param repo_name: имя репозитория
    :return True в случае существования, иначе False
    """
    response = requests.get(
        f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}",
        auth=(GITHUB_USER, GITHUB_TOKEN)
    )
    if response.status_code == 200:
        print(f"Repository '{repo_name}' exists.")
        return True
    elif response.status_code == 404:
        print(f"Repository '{repo_name}' does not exist.")
        return False
    else:
        print(f"Failed to check repository: {response.json()}")
        return False


def delete_repo(repo_name: str) -> bool:
    """
    Удаляет новый репозиторий на GitHub
    :param repo_name: имя репозитория
    :return True в случае успеха, иначе False
    """
    response = requests.delete(
        f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}",
        auth=(GITHUB_USER, GITHUB_TOKEN)
    )
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
        return True
    else:
        print(f"Failed to delete repository: {response.json()}")
        return False


def main():
    if check_repo_exists(REPO_NAME):
        delete_repo(REPO_NAME)
    if create_repo(REPO_NAME):
        delete_repo(REPO_NAME)


if __name__ == "__main__":
    main()
