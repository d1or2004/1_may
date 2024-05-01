from django.urls import path
from .views import LandingAPIView, ArtistAPIView, AlbumAPIView, SongAPIView

urlpatterns = [
    path('landing/', LandingAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('album/', AlbumAPIView.as_view(), name='album'),
    path('song/', SongAPIView.as_view(), name='song'),
]
