# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.utils.html import format_html


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.BooleanField(default=True)
    hireDate = models.DateField(default=now)


class SmInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    # LM = models.CharField(max_length=50, verbose_name='栏目一')
    LM = models.ForeignKey('lm',
                           related_name='old_lmcode',
                           default='30',
                           on_delete=models.SET_DEFAULT,
                           verbose_name='栏目归属'
                           )
    # LM3 = models.CharField(max_length=50, verbose_name='栏目三')
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

    def __str__(self):
        return self.TITLE

    class Meta:
        verbose_name = '寺庙信息'
        verbose_name_plural = '寺庙信息'

    def colored_name(self):
        color_code = 'red'
        return format_html(
            '<span style="color:{};">{}</span>', color_code, self.LM.lmtitle
        )
    colored_name.short_description = '栏目名称'


class lm(models.Model):
    id = models.AutoField(primary_key=True)
    lmoldcode = models.IntegerField(db_index=True)
    lmtitle = models.CharField(max_length=32, null=True, blank=True, verbose_name='栏目归属')
    lmlevel = models.IntegerField()
    lmcode = models.CharField(max_length=27, default='001000000')
    pic = models.CharField(max_length=254, null=True, blank=True)
    mb = models.IntegerField(default=10)
    fontcolor = models.CharField(default='#000000', max_length=10)
    show = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    up_user = models.TextField(default='admin', blank=True, null=True)

    def __str__(self):
        return self.lmtitle

    class Meta:
        ordering = ('lmoldcode', 'lmlevel')
        verbose_name = '栏目信息'
        verbose_name_plural = '栏目信息'


class Province(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=10)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='city2province')

    def __str__(self):
        return str(self.name)


class Person(models.Model):
    name = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='person2city')

    def __str__(self):
        return str(self.name)
