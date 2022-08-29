from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from categories import models as categories_models
from accounts import models as accounts_models

# Create your views here.
def home(request):
    return render(request, "main/index.html")
    
@user_passes_test(lambda u: u.is_staff)
def admin_panel(request, id):
    context = {
        "users": accounts_models.UserModel.get_all_users(),
        "posts": categories_models.Post.get_all_posts(),
        "categories": categories_models.Category.get_all_categories(),
        "forbidden_words": categories_models.ForbiddenWord.get_all_forbidden_words(),
    }
    
    return render(request, "main/admin_panel.html", context=context)
    