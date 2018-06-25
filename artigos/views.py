# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from artigos.models import Artigo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from artigos.forms import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#hierarquia de classes do django:
#View - Classe mae de todas as outras classes
#TemplateView  - Classe que tem como metodos principais : ContextMixin, TemplateResponseMixin, View

#exemplo de function based view
#def ola(request):
#    return render(request, 'index.html')

#classe para login_required - it is not working
class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)

#ContextMixin, TemplateResponseMixin,View
class Principal(TemplateView):
    template_name = "index.html"
    form_class = FormPesquisa

    #passando um context para a pagina principal para TemplateView
    #def get_context_data(self, *args, **kwargs):
    #    context = super(Principal, self).get_context_data(**kwargs)
    #    context['title'] = "About us"
    #    return context

    #para usar o render_to_response temos que herdar esse metodo do ContextMixin e TemplateResponseMixin
    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['usuario'] = request.user
    #     return self.render_to_response(context)

    #TemplateView, View
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class})

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            q = form.cleaned_data['lupa']
            resultado = Artigo.objects.filter(titulo__contains=q)
            return render(request, self.template_name, {'form':self.form_class, 'artigo':resultado})

#exemplo de class based view
#retirado de listview para que possamos passar o usuario
class Posts(LoginRequiredMixin, ListView):
    template_name='posts.html'
    context_object_name = 'artigos'
    paginate_by = 3

    def get_queryset(self):
        return Artigo.objects.all()

class MenuFiltroPosts(LoginRequiredMixin, ListView):
    template_name='posts.html'
    context_object_name = 'artigos'
    paginate_by = 2

    #exemplo de como pegar o slug field do urls
    # def get(self, request, *args, **kwargs):
    #     artigo = Artigo.objects.filter(titulo__contains= kwargs['slug'])
    #     paginator = Paginator(artigo, 1)
    #     page = request.GET.get('page')
    #     artigo = paginator.get_page(page)
    #     return render(request, self.template_name, {'artigos':artigo})

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Artigo.objects.filter(titulo__contains=slug)


class Contato(LoginRequiredMixin, FormView, TemplateView):
    template_name = "contato.html"
    form_class = FormContato
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        return super(Login, self).form_valid(form)
    

    def post(self, request, *args, **kwargs):
        pass

    #def get(self, request, *args, **kwargs):
        #return render(request, self.template_name)

#Antes usado omo detailView
class ArtigoDetalhes(LoginRequiredMixin, TemplateView):
    model = Artigo
    #slug_field = 'pk'
    #context_object_name = 'artigo'
    template_name = 'detail.html'

    # def get_context_data(self,**kwargs):
    #     context = super(ArtigoDetalhes,self).get_context_data(**kwargs)
    #     return context

    def get(self, request, *args, **kwargs):
        consulta = Artigo.objects.get(id = kwargs['pk'])
        return render(request, self.template_name, {'artigo':consulta})

class Login(FormView):
    template_name = "login.html"
    form_class = Formlogin
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        return super(Login, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        flag_nao_autorizado = False
        # estado = "vazio"
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                if user.is_active:
                    if user.is_staff:
                        login(request, user)
                        return redirect('http://programblog.life/')
                    else:
                        flag_nao_autorizado = True
                else:
                    flag_nao_autorizado = True
            else:
                flag_nao_autorizado = True

        return render(request, self.template_name, {'form':self.form_class, 'nao_permitido':flag_nao_autorizado})

# class Procurar(FormView):
#     template_name = 'index.html'
#     form_class = FormPesquisa
#     success_url = 'http://127.0.0.1:8000/pesquisa'
#
#     def form_valid(self, form):
#            email = form.cleaned_data['email']
#         return super(Procurar, self).form_valid(form)
#
#     def post(self, request, *args, **kwargs):
#         pass


class Logout(TemplateView):
    template_name = 'logout.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)

class Cadastro(FormView):
    template_name = "cadastro.html"
    form_class = FormCadastro
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        return super(Login, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            email = form.cleaned_data['email']
            senha1 = form.cleaned_data['senha1']
            senha2 = form.cleaned_data['senha2']
            if (senha1 == senha2):
                valida = True
            else:
                valida = False

            if (valida):
                try:
                    user = User.objects.create_user(usuario, email, senha1)
                    user.is_staff = False
                    user.save()
                    login(request, user)
                except Exception as err:
                    erro = err

                return redirect('http://127.0.0.1:8000/')
            else:
                erro = "Senha invalida"

        return render(request, self.template_name, {'form':self.form_class, 'erro':erro})
