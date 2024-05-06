from django.db.models import Avg

def calculate_average_rating(cheese):
    ratings = cheese.ratings.all() 
    avg_rating = ratings.aggregate(Avg('rating_value'))['rating_value__avg'] 
    return avg_rating or 0
