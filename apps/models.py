from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AccountManager(BaseUserManager):
    def create_user(self, chat_id, password=None, **extra_fields):
        if chat_id is None:
            raise TypeError('Username did not come')
        user = self.model(chat_id=chat_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, chat_id, password=None, **extra_fields):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(chat_id=chat_id, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = AccountManager()
    USERNAME_FIELD = 'chat_id'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = False
        ordering = ["-id"]

    def __str__(self):
        return f'{self.first_name} | {self.username}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Category(BaseModel):

    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="child", blank=True, null=True)

    def __str__(self):
        return self.name


class DjangoCourse(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=255, null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return f'{self.title}'


class CourseVideo(BaseModel):
    video = models.FileField(upload_to="videos/")
    course = models.ForeignKey(DjangoCourse, on_delete=models.CASCADE, related_name="course_video")


class Commit(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commit")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"
