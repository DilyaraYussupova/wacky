from django.shortcuts import render,redirect, get_object_or_404
from .models import Widget
from django.views.generic.edit import CreateView

def index(request):
    return render(request, 'index.html')

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['widgets'] = Widget.objects.all()
        return context

def widget_delete(request, pk, template_name='widget_confirm_delete.html'):
    widget = get_object_or_404(Widget, pk=pk)    
    if request.method=='POST':
        widget.delete()
        return redirect('/')
    return render(request, template_name, {'object':widget})
