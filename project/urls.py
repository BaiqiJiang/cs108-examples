# urls.py
# Author: Baiqi Jiang
# Description: Import url patterens here.
# Date: 2021.4


from django.urls import path
from .views import * # our view class definition

urlpatterns = [
    path("",HomePageView.as_view(), name="home_page"),
    path("help",HelpPageView.as_view(), name="help"),
    path("termsofuse",ShowTermsOfUsePageView.as_view(), name="terms_of_use"),
    path("phylum",ShowAllPhylaView.as_view(), name="show_all_phyla"),
    path("class",ShowAllClassesView.as_view(), name="show_all_classes"),
    path("create_class", CreateClassView.as_view(), name='create_class'),
    path("phylum/<int:phylum_pk>/update_class/<int:class_pk>", UpdateClassView.as_view(), name="update_class"),
    path("phylum/<int:phylum_pk>/delete_class/<int:class_pk>", DeleteClassView.as_view(), name='delete_class'),
    path("phylum/<int:pk>", ShowPhylumView.as_view(), name="show_phylum"),
    path("phylum/<int:phylum_pk>/class/<int:class_pk>", ShowClassView.as_view(), name="show_class"),
    path("profile",ShowAllProfileView.as_view(), name="show_all_profiles"),
    path("profile/<int:pk>", ShowProfileView.as_view(), name="show_profile"),
    path("profile/<int:profile_pk>/update_profile", UpdateProfileView.as_view(), name="update_profile"),
    path("profile/<int:profile_pk>/delete_profile", DeleteProfileView.as_view(), name="delete_profile"),
    path("create_profile", CreateProfileView.as_view(), name='create_profile'),
    path("comments", WriteCommentsView.as_view(), name='comments'),
]