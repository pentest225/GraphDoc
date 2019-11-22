from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    
# Proposition de mes applications

#     1=>Blog applications
#         Pour la gestions de notre blog 
#     2=>Customers 
#         Pour la gestions des menbres et des visiteurs (je pense qu'un mambre peux aussi etre un visiteur dans le cas ou luis meme consulte des articles d'un ou plusieurs autres menbres )
#     3=>AllConfig 
#         Pour les configurations du frote et des differentes sections du site 
#     4=>Contact 
#         Pour la gestions des souscriptions des message et toute autre informations relative a la localisation de la stucture 
        
# Models par applications 
#     Blog applications
#         Category
#         Articles
#         Comment 
#         responseComent 
#         Tags
#         Likes


#     Customers
#         memberes
#         visitors


#     Contact
#         souscribers
#         message
#         

#    Config 
        # headerFront
        # footerFront
        # allInfo
        # locationsMap


class EmailSubscriber(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField()