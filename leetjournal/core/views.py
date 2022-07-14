from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import problemModel
from django.http import HttpResponse
# Create your views here.

@csrf_exempt
def homepageView(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            name = request.POST["problem-name"]
            difficulty = request.POST["difficulty"]
            explanation = request.POST["explanation"]
            language = request.POST["lang"]
            code = request.POST["usercode"]
        
            object = problemModel(user=request.user, name=name, difficulty=difficulty, approach=explanation, language=language, code=code)
            object.save()
        else:
            return HttpResponse("Please login first")
        
    return render(request, 'core/homepage.html')

def getUserProblems(request):
    if request.method == "GET":
        problems = problemModel.objects.filter(user = request.user)
        return HttpResponse(problems)
    return HttpResponse("Error")