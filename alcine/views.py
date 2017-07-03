from alcine.models import *
from alcine.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from alcine.api_connect import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def retrieve(self, request, pk=None):
        profileList = Profile.objects.filter(idx=pk)
        if profileList:
            profile = Profile.objects.get(id=pk)
        else:
            dictObj = getDetailPersonRdir(pk)
            obj = Profile()
            obj.fill(getDetailPerson(pk))
            obj.save()
            return JsonResponse(json.loads(dictObj))
        profileSerielize = ProfileSerializer(profile)
        return Response(profileSerielize.data)

class ProfileimgViewSet(viewsets.ModelViewSet):
    queryset = Profileimg.objects.all()
    serializer_class = ProfileimgSerializer
    
    def retrieve(self, request, pk=None):
        modelList = Profileimg.objects.filter(idx=pk)
        if not modelList:
            dictObj = getImagesPersonRdir(pk)
            obj = Profileimg()
            obj.fill(getImagesPerson(pk))
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = Profileimg.objects.get(idx=pk)
        serialize = ProfileimgSerializer(model)
        return Response(serialize.data)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def retrieve(self, request, pk=None):
        modelList = Movie.objects.filter(id=pk)
        if not modelList:
            dictObj = getDetailMovieRdir(pk)
            obj = Movie()
            obj.fill(getDetailMovie(pk))
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = Movie.objects.get(idx=pk)
        serialize = MovieSerializer(model)
        return Response(serialize.data)

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = MovieArray.objects.all()
    serializer_class = MovieArraySerializer
    
    def retrieve(self, request, pk=None):
        modelList = MovieArray.objects.filter(idx=pk)
        if not modelList:
            if(pk=="1"):
                dictObj = getPopularMoviesRdir()
                objFill = getPopularMovies()
            elif(pk=="2"):
                dictObj = getTopMoviesRdir()
                objFill = getTopMovies()
            elif(pk=="3"):
                dictObj = getUpcomingMoviesRdir()
                objFill = getUpcomingMovies()
            elif(pk=="4"):
                dictObj = getNowplayingMoviesRdir()
                objFill = getNowplayingMovies()
            obj = MovieArray()
            obj.fill(objFill)
            obj.typeMovie = pk
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = MovieArray.objects.get(typeMovie=pk)
        serialize = MovieArraySerializer(model)
        return Response(serialize.data)

class MovieSimilarArrayViewSet(viewsets.ModelViewSet):
    queryset = MovieSimilarArray.objects.all()
    serializer_class = MovieSimilarArraySerializer
    
    def retrieve(self, request, pk=None):
        modelList = MovieSimilarArray.objects.filter(idx=pk)
        if not modelList:
            dictObj = getSimilarMoviesRdir(pk)
            obj = MovieSimilarArray()
            obj.fill(getSimilarMovies(pk))
            obj.idx = 0
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = MovieSimilarArray.objects.get(idx=pk)
        serialize = MovieSimilarArraySerializer(model)
        return Response(serialize.data)

class MovieCreditsArrayViewSet(viewsets.ModelViewSet):
    queryset = MovieCreditsArray.objects.all()
    serializer_class = MovieCreditsArraySerializer
    
    def retrieve(self, request, pk=None):
        modelList = MovieCreditsArray.objects.filter(idx=pk)
        if not modelList:
            dictObj = getMovieCreditsPersonRdir(pk)
            obj = MovieCreditsArray()
            obj.fill(getMovieCreditsPerson(pk))
            obj.idx = 0
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = MovieCreditsArray.objects.get(idx=pk)
        serialize = MovieCreditsArraySerializer(model)
        return Response(serialize.data)

class MovieCreditsCastArrayViewSet(viewsets.ModelViewSet):
    queryset = MovieCreditsCastArray.objects.all()
    serializer_class = MovieCreditsCastArraySerializer
    
    def retrieve(self, request, pk=None):
        modelList = MovieCreditsCastArray.objects.filter(idx=pk)
        if not modelList:
            dictObj = getCastPeopleRdir(pk)
            obj = MovieCreditsCastArray()
            obj.fill(getCastPeople(pk))
            obj.idx = 0
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = MovieCreditsCastArray.objects.get(idx=pk)
        serialize = MovieCreditsCastArraySerializer(model)
        return Response(serialize.data)

class PopularPeopleViewSet(viewsets.ModelViewSet):
    queryset = PopularPeople.objects.all()
    serializer_class = PopularPeopleSerializer
    
    def retrieve(self, request, pk=None):
        modelList = PopularPeople.objects.filter(id=0)
        if not modelList:
            dictObj = getPopularPeopleRdir()
            obj = PopularPeople()
            obj.fill(getPopularPeople())
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = PopularPeople.objects.get(id=1)
        serialize = PopularPeopleSerializer(model)
        return Response(serialize.data)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    def retrieve(self, request, pk=None):
        modelList = Video.objects.filter(id=0)
        if not modelList:
            dictObj = getVideoMovieRdir(pk)
            obj = Video()
            obj.fill(getVideoMovie(pk))
            obj.save()
            return JsonResponse(json.loads(dictObj))
        model = Video.objects.get(id=1)
        serialize = VideoSerializer(model)
        return Response(serialize.data)