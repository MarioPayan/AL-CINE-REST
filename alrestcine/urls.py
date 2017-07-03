from django.conf.urls import url, include
from rest_framework import routers
from alcine import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'profile', views.ProfileViewSet)
router.register(r'profile-images', views.ProfileimgViewSet)
router.register(r'movie', views.MovieViewSet)
router.register(r'movies', views.MoviesViewSet)
router.register(r'people-important', views.PopularPeopleViewSet)
router.register(r'movie-credits', views.MovieCreditsArrayViewSet)
router.register(r'movie-cast', views.MovieCreditsCastArrayViewSet)
router.register(r'movie-similar', views.MovieSimilarArrayViewSet)
router.register(r'video', views.VideoViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]