Todo
====

シンプルなTodoリスト管理アプリです。

## Requirement
- Python3.x
- Python3.5.2で動作確認

ライブラリ
```
Django==2.2
pytz==2019.1
sqlparse==0.3.0
```

## Usage

インストール後にmigrationファイルを作成してください。

```
$ python manage.py makemigration
$ python manage.py migrate
```

mirateが済んだらサーバーを起動します。

```
$ python manage.py runserver
```

ブラウザで

```
localhost:8000/myapp/
```

にアクセスしてください。


## Install

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[tcnksm](https://github.com/tcnksm)
