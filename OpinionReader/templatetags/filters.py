from django import template

register = template.Library()

@register.filter
def list_to_string(value):
    words =[]
    try:
        for keyword_assoc in value:
            words.append(keyword_assoc.keyword.key_name)
        return '，'.join(words)
    except (IndexError, ValueError, TypeError):
        return None

@register.filter
def get_domain_name(value):
    try:
        if value == "wechat":
            return "微信"
        elif value == "webpage":
            return "网页"
        elif value == "weibo.com":
            return "微博"
        else:
            return "其他"
    except (IndexError, ValueError, TypeError):
        return None