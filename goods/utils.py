from goods.models import Products


def q_search(query):
    query = (query or "").strip()

    if not query:
        return Products.objects.none()

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    keywords = [word for word in query.split() if len(word) > 1]
    if not keywords:
        return Products.objects.none()

    q_objects = None
    for token in keywords:
        token_filter = Products.objects.filter(
            name__icontains=token,
        ) | Products.objects.filter(description__icontains=token)
        q_objects = token_filter if q_objects is None else (q_objects | token_filter)

    result = q_objects.distinct().order_by("name")

    for product in result:
        highlighted_name = product.name
        highlighted_description = product.description
        for token in keywords:
            highlighted_name = highlighted_name.replace(
                token,
                f'<span style="background-color: yellow;">{token}</span>'
            )
            highlighted_name = highlighted_name.replace(
                token.title(),
                f'<span style="background-color: yellow;">{token.title()}</span>'
            )
            highlighted_description = highlighted_description.replace(
                token,
                f'<span style="background-color: yellow;">{token}</span>'
            )
            highlighted_description = highlighted_description.replace(
                token.title(),
                f'<span style="background-color: yellow;">{token.title()}</span>'
            )
        product.headline = highlighted_name
        product.bodyline = highlighted_description

    return result
