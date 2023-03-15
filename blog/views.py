from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class Learning_disabilities_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Learning_disabilities = True)

class Hearing_loss_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Hearing_loss = True)
    
class Cerebral_palsy_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Cerebral_palsy = True)
    
class Physical_disability_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Physical_disability = True)
    
class Vision_impairment_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Vision_impairment = True)
    
class Dyslexia_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Dyslexia = True)
    
class Stroke_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Stroke = True)
    
class Diabetes_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Diabetes = True)
    
class Spinal_cord_injury_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Spinal_cord_injury = True)
    
class Parkinsons_disease_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Parkinsons_disease = True)

class Neurological_disorder_PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    def get_queryset(self):
        return Post.objects.filter(Neurological_disorder = True)   
    

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','short_job_description', 'content','job_requirements', 'Learning_disabilities','Hearing_loss','Cerebral_palsy',
              'Physical_disability','Vision_impairment','Dyslexia','Stroke','Diabetes','Spinal_cord_injury','Parkinsons_disease','Neurological_disorder', 'contact_info']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','short_job_description', 'content','job_requirements', 'Learning_disabilities','Hearing_loss','Cerebral_palsy',
              'Physical_disability','Vision_impairment','Dyslexia','Stroke','Diabetes','Spinal_cord_injury','Parkinsons_disease','Neurological_disorder', 'contact_info']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def home(request):
    return render(request, 'blog/homepage.html')
