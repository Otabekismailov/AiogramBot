from django.urls import path

from apps.views import CreateUser, CategoryListApi, CategoryParent, CommitCreateList, CourseList

urlpatterns = [
    path('user-create/', CreateUser.as_view(), name='user-create'),
    path('category-list/', CategoryListApi.as_view(), name='category-list'),
    path('category-parent-list/<int:pk>/', CategoryParent.as_view(), name='category-parent-list'),
    path('commit-create-list/', CommitCreateList.as_view(), name='commit-create-list'),
    path('course-list/<int:pk>/', CourseList.as_view(), name='course-list'),
]
