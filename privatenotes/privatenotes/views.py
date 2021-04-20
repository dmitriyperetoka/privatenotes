from django.shortcuts import render


def page_not_found(request, exception):  # noqa
    """Handle not found error."""
    return render(request, 'misc/404.html', status=404)
