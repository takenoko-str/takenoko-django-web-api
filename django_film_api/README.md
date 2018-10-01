使い方
============

#### PIPインストール
```
pip3 install django
pip3 install djangorestframework django-filter djangorestframework-filters
pip3 install httpie
# 以下も入れるとshell表示がカラフルになります
pip3 install jupyter
pip3 install 'ipykernel<5.0.0'
pip3 install django-extensions
```

#### MySQLインストール・起動
```
brew install mysql
mysql.server start
```

#### スキーマ・データのインポート
- [Sakila](https://dev.mysql.com/doc/index-other.html)へアクセスしてデータをダウンロード

```
mysql -u root -p < sakila-db/sakila-schema.sql
mysql -u root -p < sakila-db/sakila-data.sql
```

#### プロジェクトの作成
```
django-admin startproject django_film_api
cd django_film_api
python3 manage.py startapp film
```

#### データベースのモデルを作成
```
vim django_film_api/film/models.py
```

#### フレームワークが使用するライブラリの設定
```
vim django_film_api/django_film_api/settings.py
```

#### データベースモデルの動作確認
```
python3 manage.py shell
# SAMPLE django_shell.ipynb
# OR 
python3 manage.py shell_plus --notebook
```

#### ビューを作成
```
vim django_film_api/film/views.py
```

#### ルーティングを行う
```
vim django_film_api/django_film_api/urls.py
```

#### DBセットアップ
```
python3 manage.py migrate
```

#### Webサーバを起動
- DBのデータをブラウザ上で見る事ができます
```
python3 manage.py runserver
```

#### JSONをリクエスト
- curlでもよいですが、httpコマンドを使ってみます
```
http 'http://localhost:8000/films.?page=2'
```

