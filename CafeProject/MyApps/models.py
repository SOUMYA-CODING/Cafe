from django.db import models


# Food Category
class FoodCategory(models.Model):
    fc_name = models.CharField(max_length=50)
    fc_craeted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fc_name
