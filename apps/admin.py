from django.contrib import admin

from apps.models import DjangoCourse, User, Commit, Category, CourseVideo


# Register your models here.
class CourseVideoStacked(admin.StackedInline):
    model = CourseVideo
    extra = 1


@admin.register(DjangoCourse)
class DjangoCourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_filter = ("id",)
    search_fields = ("title",)
    inlines = (CourseVideoStacked,)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "chat_id",)
    search_fields = ("username",)
    ordering = ("-id",)



@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "description",)
    list_filter = ("id",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)
