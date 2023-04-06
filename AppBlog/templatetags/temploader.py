from django import template

register = template.Library()

@register.inclusion_tag("AppBlog/post_template.html")
def post_template(post):
    return {"posteo":post}

@register.inclusion_tag("AppBlog/post_template_reducido.html")
def post_template_reducido(post):
    return {"posteo":post}