from app.models.settings.feedback import Feedback


def get_all_feedback():
    feedback = Feedback.objects.all()
    return feedback


def add_new_feedback(request):
    data = request.POST
    user = request.user
    feedback = Feedback.objects.create(
        reporter=data['reporter'] if 'reporter' in data else '',
        title=data['title'] if 'title' in data else '',
        description=data['description'] if 'description' in data else '',
        status=1,
        user=user,
    )

    return feedback
