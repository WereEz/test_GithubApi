# GitHub API

Проект содержит автоматический автоматический тест для проверки работы с GitHub API на языке Python. Тест умеет создавать, проверять наличие и удалять репозиторий на GitHub


## Требования

- Python 3.11+
- python-dotenv==1.0.0
- requests==2.27.1

## Установка
1. Клонируйте репозиторий:
```
    git clone https://github.com/wereez/test_GithubApi.git
```
2. Установите зависимости:
```
   pip install -r requirements.txt
```
3. Перейдите в директорию:
 ```
   cd test_GithubApi
```
4. Настройте переменные окружения:
В файле .env укажите свои значения для:
```
GITHUB_USER=Имя пользователя гитхаб
GITHUB_TOKEN=Созданный на https://github.com/settings/tokens/new токен
REPO_NAME=Имя репозитория для теста
```
5. Запустите:
```
   python test_api.py
```
