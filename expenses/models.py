from django.db import models
from users.models import User
from pets.models import Pet

# Create your models here.
# models.py
from django.db import models
from users.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', '식비(사료/간식)'),
        ('med', '의료비'),
        ('items', '생활용품'),
        ('toys', '장난감'),
        ('insurance', '보험'),
        ('facilities', '보육(애견 유치원/카페/호텔 등)'),
        ('etc', '기타'),
    ]
    
    FIXED_EXPENSE = 'fixed'
    VARIABLE_EXPENSE = 'variable'
    EXPENSE_TYPE_CHOICES = [
        (FIXED_EXPENSE, '고정비'),
        (VARIABLE_EXPENSE, '변동비'),
    ]

    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    category = models.BooleanField(default = True)
    expense_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    expense_price = models.PositiveIntegerField()
    memo = models.TextField()

    class Meta:
        db_table = 'expense'

    def __str__(self):
        return f"{self.expense_type} - {self.expense_price}"
    
    @property
    def Monthexpense(self):
        # 이 카테고리의 월별 총 지출 계산
        total_monthly_expense = Expense.objects.filter(
            user=self.user,
            expense_type=self.expense_type,
            date__year=self.date.year,
            date__month=self.date.month
        ).aggregate(total=models.Sum('expense_price'))['total'] or 0
        
        return total_monthly_expense
