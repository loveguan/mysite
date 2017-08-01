from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.
user_list = [{"user": "jack", "pwd": "abc"},
             {"user": "tom", "pwd": "ABC"}
             ]


def index(request,**kargs):
    # return HttpResponse("hello")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # temp = {"user": username, "pwd": password}
        models.UserInfo.objects.create(user=username,pwd=password)
        print('eeeeeeweweewew')
        print(request)
    user_list=models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})
def test(request):
    # color_obj=models.Colors.objects.create(colors="黑")
    # color_obj = models.Colors.objects.create(colors="黑")
    # models.Ball.objects.create(color=color_obj, description="黑球")
    # a=models.Ball.objects.get(description="黑球").color.colors
    # color_obj = models.Colors.objects.create(colors="绿")
    # models.Ball.objects.create(color=color_obj, description="绿球")
    # a = models.Ball.objects.get(description="绿球").color.colors
    # models.Ball.objects.get(description="红球").delete()  # 对象和QuerySet都有方法delete()
    # models.Colors.objects.filter(colors="红").delete()
    # a = models.Ball.objects.get(description="红球").color.colors
    color_obj = models.Colors.objects.filter(colors="黑")  # .get()等同于.filter().first()
    if color_obj:
        color_obj.colors = "灰"
        color_obj.save()
        models.Ball.objects.filter(description="黑球").update(color=color_obj, description="灰球")
    a=models.Colors.objects.all()
    return render(request,'test.html',{"data":a})



