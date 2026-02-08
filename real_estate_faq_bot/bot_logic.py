from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faq_data import FAQ_DATA

# Prepare questions and answers
questions = list(FAQ_DATA.keys())
answers = list(FAQ_DATA.values())

# Convert questions into vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_bot_response(user_query):
    query_vector = vectorizer.transform([user_query])
    similarity_scores = cosine_similarity(query_vector, question_vectors)

    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I couldn’t find an exact answer. Please consult a real estate expert."

    return answers[best_match_index]
