from django.http import HttpResponse
from .generate import generate_video  # Импортируй функцию generate_video

def generate_video_view(request):
    text = request.GET.get('text', '')

    if not text:
        return HttpResponse("Text parameter is required", status=400)

    output_path = "output.mp4"
    try:
        generate_video(text)
    except Exception as e:
        return HttpResponse(str(e), status=500)

    try:
        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="output.mp4"'
            return response
    except Exception as e:
        return HttpResponse(str(e), status=500)

    #   1. .venv/Scripts/activate
    #   2. python manage.py runserver
    #   3. http://127.0.0.1:8000/videoapp/generate/?text='vash text'
