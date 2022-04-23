import django_filters


from training import models


def owner(request):
    """Custom Function to filter choices at current training plan based on current user"""
    return models.TrainingPlanName.objects.filter(owner=request.user)


class SnippetFilter(django_filters.FilterSet):
    """Custom filter for Current training plan view,
    allow user to choose one of created by him training plans"""
    training_plan_name = django_filters.ModelChoiceFilter(queryset=owner)

    class Meta:
        model = models.TrainingPlanName
        fields = ['training_plan_name']
