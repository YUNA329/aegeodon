from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from expenses.serializers import ExpenseSerializer

@api_view(['POST'])
def expense_create(request):
    data = request.data
    data['user'] = request.user.id  # 현재 인증된 사용자를 owner로 설정

    serializer = ExpenseSerializer(data=data)
    if serializer.is_valid():
        expense = serializer.save()

        response_data = {
            'expense_id': expense.id,
            'date': expense.date,
            'category': expense.category,
            'expense_type': expense.expense_type,
            'expense_price': expense.expense_price,
            'memo': expense.memo
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

