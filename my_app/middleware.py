from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print("Middleware1 的 process_request方法！")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("Middleware1 的 process_view方法！")

    def process_response(self, request, response):
        print("Middleware1 的 process_response 方法！")
        return response

    def process_exception(self, request, exception):
        print("Middleware1 的 process_exception 方法！")


block_ip = ["127.0.0.1"]
class BlackListMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        remote_ip = request.META.get("REMOTE_ADDR")
        print(remote_ip)
        if remote_ip in block_ip:
            return HttpResponse("你的IP地址受限！")
        print("Middleware1 的 process_request方法！")