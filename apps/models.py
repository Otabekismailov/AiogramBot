from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AccountManager(BaseUserManager):
    def create_user(self, user_id, password=None, **extra_fields):
        if user_id is None:
            raise TypeError('Username did not come')
        user = self.model(username=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(username=username, password=password, **extra_fields)
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


class DjangoCourse(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="django")
    title = models.CharField(max_length=255, null=True, blank=True, unique=True)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f'{self.title}'


class Commit(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commit")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user}"
