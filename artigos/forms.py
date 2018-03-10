from artigos.models import *
from django import forms

class Formlogin(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput, label="Usuario")
    senha = forms.CharField(widget=forms.PasswordInput, label = "Senha")

class FormContato(forms.Form):
    nome = forms.CharField(widget=forms.TextInput, label="Nome")
    email = forms.EmailField(label="Email")
    texto = forms.CharField(widget=forms.Textarea, label="Comentario")

class FormPesquisa(forms.Form):
    lupa = forms.CharField(widget=forms.TextInput, label='')

class FormCadastro(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput, label="Usuario")
    email = forms.EmailField(label="Email")
    senha1 = forms.CharField(widget=forms.PasswordInput, label = "Senha")
    senha2 = forms.CharField(widget=forms.PasswordInput, label = "Senha (Novamente)")
