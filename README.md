Todo
====

シンプルなTodoリスト管理アプリです。

## Desscription

シンプルなTooリスト管理アプリです。
Djangoでのユーザーモデルの作成と認証の確認のために作成しました。

## Requirement
- Python3.x
- Python3.5.2で動作確認
- ライブラリ
```
Django==2.2
pytz==2019.1
sqlparse==0.3.0
```

## Install

クローン用のディレクトリを作成し移動します。
```
$ mkdir 'ディレクトリ名' 
$ cd 'ディレクトリ名'
```

移動した先でプロジェクトをクローンしてください。

```
$ git clone https://github.com/morumotto/SampleProject.git
```

## Usage　

インストール後にプロジェクトに移動します。

```
$ cd SampleProject
```

移動後、プロジェクト下にあるreuirements.txtを使い、ライブラリをインストールします。

```
$ pip install -r requirements.txt
```
migrationファイルを作成します。

```
$ python manage.py makemigrations
$ python manage.py migrate
```

mirateが済んだらサーバーを起動します。

```
$ python manage.py runserver
```

ブラウザで

```
http://localhost:8000/myapp/
```

にアクセスしてください。トップページが表示されます。
