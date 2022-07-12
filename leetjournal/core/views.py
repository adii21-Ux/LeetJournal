from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def homepageView(request):
    if request.method == "POST":
        name = request.POST["problem-name"]
        difficulty = request.POST["difficulty"]
        explanation = request.POST["explanation"]
        language = request.POST["lang"]
        code = request.POST["code"]
        
        print(name+difficulty+explanation+language)
        print(code)
        
        
    return render(request, 'core/homepage.html')
