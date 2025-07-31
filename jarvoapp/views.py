'''
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .gemini_api import ask_gemini  # 👈 import your Gemini API logic

def home(request):
    return render(request, 'jarvoapp/home.html')

@csrf_exempt
def ask(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("command")

            if not user_input:
                return JsonResponse({"response": "Kya bolna hai batao bhai 😅"}, status=400)

            reply = ask_gemini(user_input)

            return JsonResponse({"response": reply})

        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"response": "Sirf POST request allow hai bhai."}, status=405)
'''
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .gemini_api import ask_jarvo  # ✅ sahi function import

def home(request):
    return render(request, 'jarvoapp/home.html')

@csrf_exempt
def ask(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("command")

            if not user_input:
                return JsonResponse({"response": "Kya bolna hai batao bhai 😅"}, status=400)

            reply = ask_jarvo(user_input)  # ✅ yahan bhi sahi function ka call

            return JsonResponse({"response": reply})

        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"response": "Sirf POST request allow hai bhai."}, status=405)
