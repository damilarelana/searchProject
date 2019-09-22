from __future__ import unicode_literals #this is just for version compatibility

from django.db import models

# Create your models here.

class bookCategory(models.Model):
    """
    defines book category data model
    making categories primary table linked to by books
    no need to generate the id column ourselves

    """

    categoryName = models.CharField(blank=True, null=True, max_length=254)

    def __str__(self):
        """ returns a string value of the category"""
        return self.categoryName


class actualBook(models.Model):
    """
    define the actual book data model
    it links to category so foreignkey variable is needed
    that foreignkey is then assigned as its category
    django generates foreignkey by passing primary object to foreignkey()
    note that format "\{0\} - \{1\}".format(self.actualbookTitle, self.actualbookCategory)
    returns a string i.e. "..." (the format part is just in terms of formating the string)
    e.g.  it would return "Usain Bolt - Sports"
    """

    actualbookTitle = models.CharField(blank=True, null=True, max_length=254)
    actualbookCategory = models.ForeignKey(bookCategory)

    def __str__(self):
        """
            returns a string value of the category
            returns both bookTitle and bookCategory
            formated to return both together same time
        """
        return "{0} - {1}".format(self.actualbookTitle, self.actualbookCategory)
