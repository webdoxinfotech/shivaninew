from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
	post = Post.objects.order_by('-created_date')
	return render(request, 'post_list.html', {'post' : post})

def post_detail(request):
	pass