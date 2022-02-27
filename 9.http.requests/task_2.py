import os,requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        r = requests.get(f'{url}/upload?path=test.txt&overwrite=true', headers=headers).json()
        requests.put(r['href'], files={'file': os.path.abspath(file_path)})

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = './file_to_yadisk/text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
