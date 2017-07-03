from django.db import models
    
class Profile(models.Model):
    also_known_as = models.TextField()
    biography = models.TextField()
    birthday = models.TextField()
    deathday = models.TextField(null=True)
    gender = models.IntegerField()
    idx = models.IntegerField(default=0)
    name = models.TextField()
    place_of_birth = models.TextField()
    popularity = models.DecimalField(max_digits=20, decimal_places=8)
    profile_path = models.TextField()
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class Profileimg(models.Model):
    idx = models.IntegerField(default=0)
    profiles = models.TextField()
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class Movie(models.Model):
    idx = models.IntegerField(default=0)
    backdrop_path = models.TextField()
    genre = models.TextField()
    tagline = models.TextField()
    status = models.TextField()
    popularity = models.DecimalField(max_digits=20, decimal_places=8)
    vote_average = models.DecimalField(max_digits=20, decimal_places=8)
    production_companies = models.TextField()
    release_date = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class MovieArray(models.Model):
    results =  models.TextField()
    typeMovie = models.TextField()
    idx = models.IntegerField(default=0)
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class MovieSimilarArray(models.Model):
    results =  models.TextField()
    typeMovie = models.TextField()
    idx = models.IntegerField(default=0)
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class MovieCreditsArray(models.Model):
    idx = models.IntegerField(default=0)
    results =  models.TextField()
    crew =  models.TextField()
    cast =  models.TextField()
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class MovieCreditsCastArray(models.Model):
    idx = models.IntegerField(default=0)
    results =  models.TextField()
    crew =  models.TextField()
    cast =  models.TextField()
    
    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class PopularPeople(models.Model):
    results =  models.TextField()

    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])

class Video(models.Model):
    results =  models.TextField()

    def fill(self, initial_data):
        for key in initial_data:
            if hasattr(self, str(key)):
                if (not initial_data[key]):
                    initial_data[key] = ""
                setattr(self, key, initial_data[key])
