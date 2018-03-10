from django.conf.urls import url
from django.contrib import admin
from programBlog.views import Principal, Contato, Posts, ArtigoDetalhes, Login, Logout, Cadastro, MenuFiltroPosts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^ola/$', ola), #usado com funcoes
    url(r'^$', Principal.as_view(), name='principal'),
    url(r'^posts/$', Posts.as_view(),name='posts'),
    url(r'^contato/$', Contato.as_view(), name='contato'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^cadastro/$', Cadastro.as_view(), name='cadastro'),
    url(r'^posts/(?P<slug>[-\w]+)/$', MenuFiltroPosts.as_view(), name='filtroposts'),
    #url(r'^(?P<url>[-\w]+)/$', ArtigoDetalhes.as_view(), name='detalhes'),
    url(r'^(?P<pk>\d)', ArtigoDetalhes.as_view(), name='detalhes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
