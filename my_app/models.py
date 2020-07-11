from django.db import models

# Create your models here.


class NormalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(excerpt__exact="normal")


class SecretManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(excerpt__exact="secret")


class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    modified_time = models.DateTimeField(auto_now_add=True, auto_created=True, null=True)
    excerpt = models.CharField(max_length=400, default="None")
    category = models.ForeignKey("Category")
    tags = models.ManyToManyField("Tag")
    # noraml_objects = NormalManager()
    # secret_objects = SecretManager()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Score(models.Model):
    class Meta:
        verbose_name = "分数表"
        verbose_name_plural = "分数表"
    name = models.CharField(max_length=10, verbose_name="姓名")
    math = models.PositiveIntegerField(verbose_name="数学")
    chinese = models.PositiveIntegerField(default=88, verbose_name="语文")

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=20)
    grade = models.ForeignKey("Grade")
    gender = models.BooleanField(default=False)


class GradeManager(models.Manager):
    def search_title_by_kw(self, kw):
        return self.filter(name__contains=kw)

    def get_queryset(self):
        return super().get_queryset().filter(is_delete=0)


class Grade(models.Model):
    name = models.CharField(max_length=50)
    num = models.PositiveIntegerField(default=10)
    created_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)
    grade_manager = GradeManager()


class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=400)

    def __str__(self):
        return self.username


class People(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IDCard(models.Model):
    num = models.CharField(max_length=18)
    people = models.OneToOneField(People, on_delete=models.PROTECT)

    def __str__(self):
        return self.num
