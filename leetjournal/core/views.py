from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import problemModel
from django.http import HttpResponse
# Create your views here.


def homepageView(request):
    if request.user.is_authenticated:
        return render(request, 'core/homepage.html')
    else:
        return redirect("user:loginuser") 
    
@csrf_exempt
def submitSolution(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST["problem-name"]
            difficulty = request.POST["difficulty"]
            explanation = request.POST["explanation"]
            language = request.POST["lang"]
            code = request.POST["usercode"]
            
            object = problemModel(user=request.user, name=name, difficulty=difficulty, approach=explanation, language=language, code=code)
            object.save()
        return redirect('core:homepage')
    else:
        return redirect("user:loginuser")

def getUserSolutions(request):
    if request.method == "GET":
        problems = problemModel.objects.filter(user = request.user)
        return render(request, 'core/solutions.html', {'solutions':problems})
    return HttpResponse("Error")