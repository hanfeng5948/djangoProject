from django.db import models

# Create your models here.
from django.db import models


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class SmInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    LM = models.CharField(max_length=50, verbose_name='栏目一')
    LM2 = models.CharField(max_length=50, verbose_name='栏目二')
    LM3 = models.CharField(max_length=50, verbose_name='栏目三')
    PAIXU = models.IntegerField(verbose_name='排序')
    TITLE = models.CharField(max_length=150, verbose_name='标题')
    ADDRESS = models.CharField(max_length=254, verbose_name='寺庙地址')
    ZHUCHI = models.CharField(max_length=254, verbose_name='主持')
    CONTENT = models.TextField(verbose_name='正文代码')
    ZZ = models.CharField(max_length=50)  # 未知、预留字段
    CREATETIME = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    UPTIME = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    ISDELETE = models.BooleanField(default=False, verbose_name='是否删除')
    HIT = models.IntegerField(verbose_name='阅读数')
    OUTURL = models.TextField(verbose_name='外链信息的外链地址')
    TITLECOLOR = models.CharField(max_length=50, verbose_name='标题颜色')
    TITLEBOLD = models.BooleanField(default=False, verbose_name='标题加粗')
    PIC = models.TextField(verbose_name='缩略图，用于推荐时显示小图片')
    TJ = models.IntegerField(verbose_name='推荐浏览页上下文，设置顺序，不大于4')
    TOUTIAO = models.IntegerField(verbose_name='推荐首页，设置顺序，不大于4')
    ONTOP = models.IntegerField(verbose_name='是否置顶，设置置顶顺序')
    ADDUSER = models.CharField(max_length=254, verbose_name='添加信息用户')
    HTITLE = models.CharField(max_length=254, verbose_name='信息副标题')
    FILENAME = models.CharField(max_length=254, verbose_name='信息附件')
    LAIYUAN = models.CharField(max_length=254, verbose_name='信息来源')
