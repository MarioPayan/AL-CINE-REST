from alcine.models import *
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileimgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profileimg
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieArray
        fields = '__all__'

class MovieCreditsArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCreditsArray
        fields = '__all__'

class MovieCreditsCastArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCreditsCastArray
        fields = '__all__'

class PopularPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPeople
        fields = '__all__'

class MovieSimilarArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSimilarArray
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'