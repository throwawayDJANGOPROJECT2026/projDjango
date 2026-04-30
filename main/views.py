from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME KZ - Главная'
        context['content'] = "Магазин мебели HOME KZ"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME KZ - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = (
            "HOME KZ — учебный интернет-магазин мебели и товаров для дома, "
            "адаптированный под рынок Казахстана. Мы показываем, как устроен "
            "каталог, корзина, оформление заказов и справочные страницы в одном проекте."
        )
        return context


class DeliveryPaymentView(TemplateView):
    template_name = 'main/delivery_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доставка и оплата'
        context['content'] = "Доставка и оплата"
        return context


class ContactsView(TemplateView):
    template_name = 'main/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контактная информация'
        context['content'] = "Контактная информация"
        return context
    

# def index(request):

#     context = {
#         'title': 'Home - Главная',
#         'content': "Магазин мебели HOME",
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': "О нас",
#         'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)