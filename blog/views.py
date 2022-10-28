from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "blog/index.html")


def detail(request):
    return HttpResponse("detail page")


class AccountCreateView(View):
    def get(self, request):
        return render(request, "blog/register.html")

# post を追加
    def post(self, request):
        # ユーザー情報を保存する
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        # 登録完了画面を表示する
        return render(request, "blog/register_success.html")
# 登録完了画面を表示する


class AccountLoginView(LoginView):
    """ログインページのテンプレート"""
    template_name = 'blog/login.html'

    def get_default_redirect_url(self):
        """ログインに成功した時に飛ばされるURL"""
        return "/blog"


class AccountLogoutView(LogoutView):
    template_name = 'blog/logout.html'


class MypageView(LoginRequiredMixin, View):
    # ログインしてない場合ここに飛ばす
    login_url = '/blog/login'

    def get(self, request):
        return render(request, "blog/mypage.html")
