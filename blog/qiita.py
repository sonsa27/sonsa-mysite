import requests
import random


class QiitaApiClient:
    """Qiita の API を叩く役割を持つクラス"""

    def get_django_articles(self):
        # get リクエストを送る
        response = requests.get(
            "https://qiita.com/api/v2/tags/django/items",
            headers={
                "Authorization": "Bearer 94e6ca5d87d111cb593369642d261581c3af62bd"},
        )

        # アクセストークンがない場合はこう
        # response = requests.get("https://qiita.com/api/v2/tags/django/items")
        # 画面の初期化
        qiita_articles = []
        # jsonはlist型（qiitaの投稿リスト）
        json = response.json()
        # json_articleはdict型
        for json_article in json:
            # dictから取り出す
            qiita_article = QiitaArticle(
                json_article["title"],
                json_article["url"],
            )
            qiita_articles.append(qiita_article)
        return qiita_articles


class QiitaArticle:

    def __init__(self, title, url):
        self.title = title
        self.url = url
