from django.conf.urls import url
from my_app.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^index/(\d*)$', index, name='index'),
    url(r'^post/$', save_post, name='post'),
    url(r'^post/(\d)', detail, name='detail'),
    url(r'^update/(\d+)$', update_post, name='update'),
    url(r'^delete/(\d+)$', delete_post, name='delete'),
    url(r'^gen_post/', gen_post, name='gen_post'),
    url(r'^gen_score/', gen_score, name='gen_score'),
    url(r'^form', get_form, name='form'),
    url(r'^template_demo', template_demo, name='template_demo'),
    url(r'^register/', register, name='register'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
]
