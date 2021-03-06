"""FeedBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from login import views
from boards import views as boards_views
urlpatterns = [
    path('admin/', admin.site.urls,name = 'admin'),
    path('index/',views.index,name = 'index'),

    path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'views_register'),
    path('logout/',views.logout,name = 'logout'),
    path('boards/',boards_views.home,name = 'boards_home'),
    path('create_course/',views.CreateCourse,name = 'create_course'),
    path('personal_center/',views.PersonalCenter,name = 'personal_center'),
    path('update/',views.Update,name = 'update'),
    re_path(r'^index/choose/(?P<pk>\d+)/$',views.choose_course,name = 'choose_course'),
    re_path(r'^course/(?P<pk>\d+)/$',views.Course,name = 'course'),
    re_path(r'^course/(?P<pk>\d+)/assistant/$',views.assistant,name = 'assistant'),
    re_path(r'^course/(?P<pk>\d+)/search/$',views.search,name = 'search'),
    re_path(r'^course/(?P<pk>\d+)/search/assistant_select/(?P<user_pk>\d+)$',views.search_select,name = 'search_select'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)$',views.assistant_select,name = 'assistant_select'),
    re_path(r'^course/(?P<pk>\d+)/stu_assistant_select/(?P<user_pk>\d+)$',views.stu_assistant_select,name = 'stu_assistant_select'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/pri_grade/$',views.pri_grade,name = 'pri_grade'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/pri_update/$',views.pri_update,name = 'pri_update'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/pri_assign/$', views.pri_assign,name='pri_assign'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/pri_delete/$', views.pri_delete,name='pri_delete'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/pri_resource/$', views.pri_resource,name='pri_resource'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/cancel_pri1/$',views.cancel_pri1,name = 'cancel_pri1'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/cancel_pri2/$',views.cancel_pri2,name = 'cancel_pri2'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/cancel_pri3/$',views.cancel_pri3,name = 'cancel_pri3'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/cancel_pri4/$',views.cancel_pri4,name = 'cancel_pri4'),
    re_path(r'^course/(?P<pk>\d+)/assistant_select/(?P<user_pk>\d+)/cancel_pri5/$',views.cancel_pri5,name = 'cancel_pri5'),
    re_path(r'^course/(?P<pk>\d+)/update/$',views.course_update,name = 'course_update'),
    re_path(r'^media/(?P<path>.*)/$', views.Download, name='download'),
    re_path(r'^course/(?P<course_pk>\d+)/delete/(?P<user_pk>\d+)$',views.delete_student,name = 'delete_student'),
    re_path(r'^course/(?P<course_pk>\d+)/delete_assistant/(?P<user_pk>\d+)$',views.delete_assistant,name = 'delete_assistant'),
    re_path(r'^course/(?P<course_pk>\d+)/delete_stu_assistant/(?P<user_pk>\d+)$',views.delete_stu_assistant,name = 'delete_stu_assistant'),
    re_path(r'^personal_center/(?P<course_pk>\d+)/delete/(?P<user_pk>\d+)$',views.drop_course,name = 'drop_course'),
    re_path(r'^personal_center/(?P<course_pk>\d+)/delete_teacher/(?P<user_pk>\d+)$',views.delete_course,name = 'delete_course'),
    re_path(r'^boards/(?P<pk>\d+)/$', boards_views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', boards_views.new_topic, name='new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', boards_views.topic_posts, name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/delete/$', boards_views.delete_topic, name='delete_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/delete/$', boards_views.delete_post, name='delete_post'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',boards_views.reply_topic, name='reply_topic'),
    re_path(r'^course/(?P<pk>\d+)/homework/$',views.HomeworkList,name = 'homework_list'),
    re_path(r'^course/(?P<pk>\d+)/homework/new/$',views.Assign,name = 'new_homework'),
    re_path(r'^course/(?P<pk>\d+)/homework/(?P<homework_pk>\d+)/$',views.HomeworkContent,name = 'homework_content'),
    re_path(r'^course/(?P<pk>\d+)/homework/(?P<homework_pk>\d+)/delete/$',views.delete_homework,name = 'delete_homework'),
    re_path(r'^course/(?P<pk>\d+)/homework/(?P<homework_pk>\d+)/submit/$',views.HomeworkSubmit,name = 'homework_submit'),
    re_path(r'^course/(?P<pk>\d+)/homework/(?P<homework_pk>\d+)/submitcon/(?P<sub_pk>\d+)$',views.SubmitCon,name = 'subcon'),
    re_path(r'^course/(?P<pk>\d+)/homework/(?P<homework_pk>\d+)/submitcon_grade/(?P<sub_pk>\d+)$',views.GiveGrade,name = 'give_grade'),
    re_path(r'^course/(?P<pk>\d+)/resource/$',views.ResourceList,name = 'resource_list'),
    re_path(r'^course/(?P<pk>\d+)/resource/new/$',views.NewResource,name = 'new_resource'),
    re_path(r'^course/(?P<pk>\d+)/resource/(?P<resource_pk>\d+)/$',views.ResourceCon,name = 'resource_content'),
    re_path(r'^course/(?P<pk>\d+)/resource/(?P<resource_pk>\d+)/delete/$',views.resource_delete,name = 'resource_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

