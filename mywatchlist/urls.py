# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_xml_id
from mywatchlist.views import show_json
from mywatchlist.views import show_json_id
from mywatchlist.views import show_html

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_id, name='show_json_id'),
    path('html/', show_html, name='show_html'),
]