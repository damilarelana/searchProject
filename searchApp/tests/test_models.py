from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from searchApp.models import actualBook, bookCategory

# Create your tests here.

# test the View
class searchAppModelsTest(TestCase):
    """  Tests searchApp models  """

    # define initial parameters (e.g. Client, Data, etc.) to be used for testing
    def setUp(self):
        """ initialize Data, Client etc. """
        self.categoryTemp = bookCategory.objects.create(categoryName='AndelaModelsTestCategory')
        self.bookTemp = actualBook.objects.create(actualbookTitle='Hello Fellow Models', actualbookCategory=self.categoryTemp)
        self.clientTemp = Client()

    # delete the test values created in the database
    def tearDown(self):
        bookCategory.objects.all().delete()
        actualBook.objects.all().delete()

    # test getting existing category directly from database
    def test_get_category_from_db(self):
        categoryGetTemp = bookCategory.objects.get(categoryName='AndelaModelsTestCategory')
        if hasattr(categoryGetTemp,'__str__'):
            self.assertEqual(categoryGetTemp.__str__(), 'AndelaModelsTestCategory')


    # test getting existing book directly from database
    def test_get_book_from_db(self):
        bookGetTemp = actualBook.objects.get(actualbookTitle='Hello Fellow Models')
        if hasattr(bookGetTemp,'__str__'):
            self.assertEqual(bookGetTemp.__str__(), 'Hello Fellow Models - AndelaModelsTestCategory')

    # test filtering for a book
    def test_filter_book_from_db(self):
        bookFilterTemp = actualBook.objects.filter(actualbookTitle__icontains='Hello Fellow Models')
        if bookFilterTemp:
            for bookFilterTempResults in bookFilterTemp:
                self.assertEqual(bookFilterTemp.get().__str__(), 'Hello Fellow Models - AndelaModelsTestCategory')
