from django.shortcuts import render
from django.http import JsonResponse
from .huggingface_utils import get_response 

def chatbot(request):
    return render(request, "chatbottemplate.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def get_response_view(request):
    user_msg = request.GET.get('msg')
    
    if not user_msg:
        return JsonResponse({'error': 'No message provided'}, status=400)
        
    try:
       
        bot_reply = get_response(user_msg)
        
        
        if "[INST]" in bot_reply:
            bot_reply = bot_reply.split("[/INST]")[-1].strip()
            
        return JsonResponse({'reply': bot_reply})
        
    except Exception as e:
        print(f"Error in get_response_view: {str(e)}")
        return JsonResponse(
            {'reply': "Sorry, I'm having trouble processing your request."},
            status=500
        )
