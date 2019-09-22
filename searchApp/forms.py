# This is meant to create the form to be used on the searchPage
# This form would be the default render before you do anything

from django.forms import ModelForm
from searchApp.models import actualBook

class searchInputForm(ModelForm):
    """  search input form to be used as display on search page """

    def __init__(self, *args, **kwargs):
        super(searchInputForm, self).__init__(*args, **kwargs)
        self.fields['actualbookTitle'].required = False
        self.fields['actualbookTitle'].label = "Book"

        self.fields['actualbookCategory'].required = False
        self.fields['actualbookCategory'].label = "Genre "

    #
    class Meta:
        """        model to link form to    """
        model = actualBook
        fields = ('actualbookTitle', 'actualbookCategory',)
        # fields_required = ('actualbookTitle',)
