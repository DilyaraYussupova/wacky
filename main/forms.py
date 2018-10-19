from django.forms import Widget

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']