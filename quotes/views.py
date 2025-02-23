from django.shortcuts import render
import requests 
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def random_quote(request):
    try:
        response = requests.get("https://api.quotable.io/random",verify=False)  # Fetch quote from API
        if response.status_code == 200:
            return Response(response.json())  # Return the quote as JSON
        else:
            return Response({"error": "Failed to fetch quote"}, status=500)
    except requests.exceptions.RequestException as e:
        return Response({"error": f"API request failed: {str(e)}"}, status=500)
    

def index(request):
    return render(request,'index.html')

