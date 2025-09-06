# chatbot_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_logic import get_rag_response
import json

def chat_view(request):
    # This handles the initial page load (a GET request)
    if request.method == 'GET':
        return render(request, 'chatbot_app/chat.html')

    # This handles the AJAX request from the frontend (a POST request)
    if request.method == 'POST':
        try:
            # Get the user's message from the request body
            data = json.loads(request.body)
            user_message = data.get('message')

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            # Get the chatbot's response
            bot_response = get_rag_response(user_message)

            # Return the response as JSON
            return JsonResponse({'response': bot_response})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)