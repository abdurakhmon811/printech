from django import template


register = template.Library()


@register.filter
def truncate_20(text):
    """Show the first 20 characters of the text and at the end, put three dots."""

    return f'{text[:20]}...'


@register.filter
def truncate_200(text):
    """Show the first 200 characters of the text and at the end, put three dots..."""

    return f'{text[:200]}...'


@register.filter
def truncate_without_dots_20(text):
    """Just show the first 20 characters of the text."""

    return f'{text[:20]}'


@register.filter
def highlight_searched(text, val):
    """Highlight the searched word in a text."""
    from haystack.utils.highlighting import Highlighter

    highlight = Highlighter(val, html_tag='mark', max_length=400)
    return highlight.highlight(text)


@register.filter
def separate_with_space(value):
    """Separate money values with commas."""

    return format(value, ',').replace(',', ' ')


@register.filter
def hide_5_5(string):
    """Hide some of the letters of the provided string."""

    start = slice(0, 5)
    middle = slice(5, 10)
    end = slice(10, 16)

    result = f'{"*" * len(string[start])}{string[middle]}{"*" * len(string[end])}'

    return result
