import sys
sys.path.append("..")
from User_Extension.models import *
from django.utils.deprecation import MiddlewareMixin

def front_user_middleware(get_response):
    print('front_user_middleware中间件初始化的代码。。。')
    def middleware(request):
        print('request到达view之前的代码。。。')
        user_id=request.session.get('user_id')
        if user_id:
            try:
                user=User.objects.get(pk=user_id)
                request.front_user=user
            except:
                request.front_user=None
        else:
            request.front_user = None
        response=get_response(request)
        print('request到达浏览器之前的代码。。。')
        return response

    return middleware

class FrontUserMiddleware(object):
    def __init__(self,get_response):
        print('front_user_middleware中间件初始化的代码。。。')
        self.get_response=get_response

    def __call__(self,request):
        print('request到达view之前的代码。。。')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = self.get_response(request)
        print('request到达浏览器之前的代码。。。')
        return response

class FrontUserMiddlewareMixin():
    def __init__(self,get_response):
        print('front_user_middleware中间件初始化的代码。。。')
        super(FrontUserMiddlewareMixin, self).__init__(get_response)
    def process_request(self,request):
        print('request到达view之前的代码。。。')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None

    def process_response(self, request,response):
        print('request到达浏览器之前的代码。。。')
        return response