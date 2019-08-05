from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30,null=False)
    password_hash=models.CharField(max_length=128)
    class Meta:
        db_table='bbs_user'#指定的表名
