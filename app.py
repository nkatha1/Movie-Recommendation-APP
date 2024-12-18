from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your TMDb API key
api_key = '1508952fe8cbfa1f8c95dd194740cb99'

# Function to get popular movies from TMDb
def get_popular_movies():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []

# Function to search movies based on user query
def search_movies(query):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=en-US&page=1'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []

@app.route('/')
def home():
    movies = get_popular_movies()
    return render_template('index.html', movies=movies)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        movies = search_movies(query)
        return render_template('results.html', movies=movies)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
