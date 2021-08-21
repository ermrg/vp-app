from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from app.forms.settings.feedback import FeedbackForm
from app.services.settings.feedbackService import get_all_feedback, add_new_feedback


@login_required
def list_feedback(request):
    feedbacks = get_all_feedback()
    return render(request, 'app/backend/settings/feedback/index.html', {'feedbacks': feedbacks})


@login_required
def create_feedback(request):

    if request.method == 'GET':
        return render(request, 'app/backend/settings/feedback/create.html')

    form = FeedbackForm(request.POST)
    if form.is_valid():
        try:
            feedback = add_new_feedback(request)

            if request.is_ajax():
                data = serializers.serialize('json', [feedback])
                return JsonResponse(data, safe=False)

            messages.success(request, 'feedback created successfully!')
            return redirect('feedback')

        except Exception:
            if request.is_ajax():
                return HttpResponse('Failed')
            messages.error(request, 'Can not create Position')
            return redirect('feedback')

    else:
        messages.error(request, 'Invalid Input')
        return render(request, 'app/backend/settings/feedback/create.html', {'form': form})
