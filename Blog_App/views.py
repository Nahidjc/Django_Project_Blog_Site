from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import  CreateView,UpdateView,DeleteView,TemplateView,ListView,DetailView,View
from Blog_App.models import Like,Blog,Comment
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from Blog_App.forms import ComentForm
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog_App/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'Blog_App/blog_list.html'
@login_required
def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = ComentForm()
    already_liked=Like.objects.filter(blog=blog,user=request.user)
    if already_liked:
        liked= True
    else:
        liked= False


    if request.method == 'POST':
        comment_form = ComentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog=blog
            comment.save()
            HttpResponseRedirect(reverse('Blog_App:blog_details',kwargs={'slug':slug}))

    return render(request,'Blog_App/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})
@login_required
def liked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Like.objects.filter(blog=blog,user=user)
    if not already_liked:
        liked_post =Like(blog=blog,user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('Blog_App:blog_details',kwargs={'slug':blog.slug}))
@login_required
def Unliked(request,pk):
    blog=Blog.objects.get(pk=pk)
    user=request.user
    already_liked=Like.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog_App:blog_details',kwargs={'slug':blog.slug}))
class Myblogs(LoginRequiredMixin,TemplateView):
    template_name="Blog_App/my_blog.html"
class UpdateBlogs(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog_content','blog_image')
    template_name='Blog_App/edit_blog.html'
    def get_success_url(self,**kwargs):
        return reverse_lazy('Blog_App:blog_details', kwargs={'slug':self.object.slug})



class DeleteBlog(LoginRequiredMixin,DeleteView):
    model=Blog
    template_name='Blog_App/delete_blog.html'

    success_url = reverse_lazy('Blog_App:my_blog')