from django.db import models

# Create your models here.
        
class User(models.Model):
    login_id = models.CharField(max_length=50, unique=True)
    login_pw = models.CharField(max_length=128)  # 비밀번호 길이를 늘림
    user_nickname = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
        
    