import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie data
movies = {
    'title': ['The Matrix', 'John Wick', 'Avengers', 'Inception', 'The Prestige'],
    'description': [
        'A hacker discovers reality is fake and joins a rebellion.',
        'A man takes revenge after his dog is killed.',
        'Superheroes team up to save the world.',
        'A thief enters dreams to steal secrets.',
        'Two magicians compete with deadly tricks.'
    ]
}

df = pd.DataFrame(movies)

# Convert text to numbers (TF-IDF)
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])

# Compare similarities
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend function
def recommend(movie_name):
    index = df[df['title'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_movies = [df['title'][i[0]] for i in scores[1:4]]
    return top_movies

# Try it
fav = 'Inception'
print(f"\nIf you liked '{fav}', you may also like:")
for m in recommend(fav):
    print("- " + m)
