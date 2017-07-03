import requests
import json

urlBase = "https://api.themoviedb.org/3/";
apiKey = "518d83af872f927b98cfe36a90cd05b0";
language = "en-US";
adult = "false";

def getObj(url):
    content = getJson(url)
    obj = json.loads(content)
    return obj

def getJson(url):
    parameters = {
        "api_key": apiKey,
        "language": language
    }
    response = requests.get(url, params=parameters)
    content = response.content.decode('UTF-8')
    return content

def makeUrl(search):
    url = urlBase + search 
    return url

def getPopularMovies():
    return getObj(makeUrl("movie/popular"))

def getPopularMoviesRdir():
    return getJson(makeUrl("movie/popular"))
  
def getPopularPeople():
    return getObj(makeUrl("person/popular"))

def getPopularPeopleRdir():
    return getJson(makeUrl("person/popular"))

def getDetailPerson(idx):
    return getObj(makeUrl("person/" + idx))

def getDetailPersonRdir(idx):
    return getJson(makeUrl("person/" + idx))

def getMovieCreditsPerson(idx):
    return getObj(makeUrl("person/" + idx + "/movie_credits")) 

def getMovieCreditsPersonRdir(idx):
    return getJson(makeUrl("person/" + idx + "/movie_credits")) 

def getSearchPerson(query):
    url = makeUrl("search/person")
    parameters = {
        "api_key": apiKey,
        "language": language,
        "query": query,
        "page": 1,
        "include_adult": "false"
    }
    response = requests.get(url, params=parameters)
    print(response)
    content = response.content.decode('UTF-8')
    obj = json.loads(content)
    return obj

def getImagesPerson(idx):
    return getObj(makeUrl("person/" + idx + "/images")) 

def getImagesPersonRdir(idx):
    return getJson(makeUrl("person/" + idx + "/images"))

def getDetailMovie(idx):
    return getObj(makeUrl("movie/" + idx))

def getDetailMovieRdir(idx):
    return getJson(makeUrl("movie/" + idx))

def getVideoMovie(idx):
    return getObj(makeUrl("movie/" + idx + "/videos"))

def getVideoMovieRdir(idx):
    return getJson(makeUrl("movie/" + idx + "/videos"))

def getTopMovies():
    return getObj(makeUrl("movie/top_rated"))

def getTopMoviesRdir():
    return getJson(makeUrl("movie/top_rated"))

def getUpcomingMovies():
    return getObj(makeUrl("movie/upcoming"))

def getUpcomingMoviesRdir():
    return getJson(makeUrl("movie/upcoming"))

def getNowplayingMovies():
    return getObj(makeUrl("movie/now_playing"))

def getNowplayingMoviesRdir():
    return getJson(makeUrl("movie/now_playing"))

def getSimilarMovies(idx):
    return getObj(makeUrl("movie/" + idx + "/similar"))

def getSimilarMoviesRdir(idx):
    return getJson(makeUrl("movie/" + idx + "/similar"))

def getCastPeople(idx):
    return getObj(makeUrl("movie/" + idx + "/credits"))
  
def getCastPeopleRdir(idx):
    return getJson(makeUrl("movie/" + idx + "/credits"))
  
