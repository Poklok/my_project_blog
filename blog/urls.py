from django.urls import path, re_path
from blog.views import post_list, post_detail, social_links
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', post_list, name='post_list'),
                  re_path(r'^tag/(?P<tag_slug>[-\w]+)/$', post_list, name='post_list_by_tag'),
                  path('post/<int:pk>', post_detail, name='post_detail'),
                  path('social_links', social_links, name='social_links'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
