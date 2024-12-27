from django.views import generic

# Create your views here.
from .models import Product, Question
from .forms import ProductForm, QuestionForm

class ReadProduct(generic.ListView):
    model = Product
    template_name = 'read.html'
    context_object_name = 'books'

class CreateProduct(generic.CreateView):
    model = Product
    template_name = 'create_and_update.html'
    context_object_name = 'product'
    form_class = ProductForm
    success_url = '/read/'


class UpdateProduct(generic.UpdateView):
    model = Product
    template_name = 'create_and_update.html'
    context_object_name = 'product'
    form_class = ProductForm
    success_url = '/read/'

class DetailProduct(generic.DetailView):
    model = Product
    template_name = 'detail.html'

class DeleteProduct(generic.DeleteView):
    model = Product
    success_url = '/read/'

    def dispatch(self, request, *args, **kwargs):
        request.method = 'POST'
        return super().dispatch(request, *args, **kwargs)
    

class ReadQuestions(generic.ListView):
    model = Question
    template_name = ''
    context_object_name = 'question'


class DetailQuestion(generic.DetailView):
    model = Question
    template_name = ''
    


class CreateQuestion(generic.CreateView):
    model = Question
    template_name = ''
    success_url = '/read/'
    form_class = QuestionForm
    context_object_name = 'question'

class UpdateQuestion(generic.UpdateView):
    model = Question
    template_name = ''
    success_url = '/read/'
    form_class = QuestionForm
    context_object_name = 'question'

class DeleteQuestion(generic.DeleteView):
    model = Question
    success_url = '/read/'

    def dispatch(self, request, *args, **kwargs):
        request.method = 'POST'
        return super().dispatch(request, *args, **kwargs)
