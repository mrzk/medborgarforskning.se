from django.urls import path
from django.urls import re_path
from blog.views import BlogPostListView
from blog.views import BlogPostDateDetailView
from blog.views import BlogPostIndexView
from blog.views import BlogPostYearArchiveView
from blog.views import BlogPostMonthArchiveView
from blog.views import BlogPostDayArchiveView
from django.views.generic.dates import DateDetailView
from blog.models import Post

app_name = 'blog'

urlpatterns = [
    # Example: / Note: this will extend whatever is is urls.py path so if the project urls.py has "blog/" this pattern would run as "blog/"
    path('', BlogPostIndexView.as_view(model=Post), name='blog_list_view'),
    # Example: /2020/ Note: this will extend whatever is is urls.py path so if the project urls.py has "blog/" this pattern would run as "blog/2020"
    path('<int:year>/',
        BlogPostYearArchiveView.as_view(),name="archive_year_numeric"),
    # Example: /2020/04/
    path('<int:year>/<int:month>/',
        BlogPostMonthArchiveView.as_view(month_format='%m'),
        name="archive_month_numeric"),
    # Example: /2020/04/21/
    path('<int:year>/<int:month>/<int:day>/',
        BlogPostDayArchiveView.as_view(month_format='%m'),
        name="archive_day_numeric"),
    path('<int:year>/<str:month>/<int:day>/<str:slug>/', BlogPostDateDetailView.as_view(model=Post, date_field="published", month_format='%m'),name="archive_date_detail"),
    ]
