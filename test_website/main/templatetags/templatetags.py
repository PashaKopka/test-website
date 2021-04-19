from django import template
from ..models import User

register = template.Library()


@register.inclusion_tag('main/post_detail.html', takes_context=True)
def get_user_liked_posts():
    request = context['request']
    user = User.objects.get(username=request.user.username)
    liked_posts = []
    for post in user.liked_posts.all():
        liked_posts.append(post.name)
    return {'liked_posts': liked_posts}
