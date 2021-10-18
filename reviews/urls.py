from django import urls
from django.urls import path

from reviews.models import Reviews
from . import views
urlpatterns = [
    path('',views.ReviewView.as_view(),name="index"),
    path('thank_you',views.ThankYouView.as_view(),name="thank_you"),
    path('reviews',views.ReviewsListView.as_view(),name="reviews_all"),
    path('reviews/favorite',views.AddFavoriteView.as_view(),name="add_favorite"),
    path('reviews/<int:pk>',views.SingleReviewView.as_view(),name="single_review"),
]
