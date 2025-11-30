import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scoring import score_task

@csrf_exempt
def analyze_tasks(request):

    # Handle OPTIONS (Preflight request)
    if request.method == "OPTIONS":
        return HttpResponse(status=200)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        tasks = data.get("tasks", [])
        for task in tasks:
            task["score"] = score_task(task)

        sorted_tasks = sorted(tasks, key=lambda x: x["score"], reverse=True)

        return JsonResponse({"results": sorted_tasks}, safe=False)

    # Fallback for unsupported methods
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def suggest_tasks(request):
    if request.method == "GET":
        # In real scenario fetch from DB
        return JsonResponse({
            "message": "Top 3 tasks suggestion feature pending DB integration."
        })
