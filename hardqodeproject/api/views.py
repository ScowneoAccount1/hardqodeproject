from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from main.models import Product, Products_Access, Lesson
from users.models import User
import json
from rest_framework import serializers

@api_view(['GET'])
def help(request):
    ans = {
        'задание 2 часть1': 'api/lessons/<str:user_id>',
    }
    return Response(ans)

@api_view(['GET'])
def users_allowed_lessons(request, userid):
    if request.user.is_authenticated:
        user     =  User.objects.get(pk=int(userid))
        products_ = Product.objects.all()
        allowed_products = Products_Access.objects.filter(user=user)
        allowed_lessons = [v.lesson for i, v in enumerate(allowed_products.all()[0].products.all())]
        # print([v.products.all() for i, v in enumerate(user.allowed_products.all())][0])

        allowed_lessons_ids = [v.pk if v!=None else 'rm' for i, v in enumerate(allowed_lessons)] #list of all ids of allowed lessons
        allowed_lessons_ids = list(filter(('rm').__ne__, allowed_lessons_ids)) #removing ones that re None

        allowed_lessons = Lesson.objects.filter(id__in=allowed_lessons_ids)

        print(allowed_lessons)

        # allowed_lessons = json.dumps(allowed_lessons)
        # print(allowed_lessons)
        # product  = ProductSerializer(allowed_products, many=True)
        lessons = ProductSerializer(allowed_lessons, many=True)


        return Response(lessons.data)
    else:
        return None