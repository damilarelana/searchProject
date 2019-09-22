from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from searchApp.models import actualBook, bookCategory

# Create your tests here.

# define the testCases for the project
class searchAppTestCase(TestCase):
    """  Tests for the searchApp application  """

    # define initial parameters (e.g. Client, Data, etc.) to be used for testing
    def setUp(self):
        """ initialize the Client, Data etc. """
        self.client = Client()
        self.url = reverse('searchPage')
        self.testCategoryValue = bookCategory.objects.create(categoryName='AndelaTestCategory')
        self.testBookValue = actualBook.objects.create(actualbookTitle='Hello Fellows', actualbookCategory=self.testCategoryValue)

    # define actual test scenarios

    # test if the searched book does not exist when no category is selected
    def test_if_searchedBook_does_not_exist_with_no_category_selected(self):
        query = {'actualbookTitle' : 'Kanye loves Kanye'}
        response = self.client.get(self.url, query)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "book not found")

    # test if the searched book exists when no category is selected
    def test_if_searchedBook_exists_with_no_category_selected(self):
        query = {'actualbookTitle': 'Hello Fellows'}
        response = self.client.get(self.url, query)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, query['actualbookTitle'])

    # test if the searched book does not exist when category is selected
    def test_if_searchedBook_does_not_exists_with_category_selected(self):
        query = {'actualbookTitle': 'Kanye loves Kanye', 'actualbookCategory': 'AndelaTestCategory'}
        response = self.client.get(self.url, query)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "book not found")
        self.assertContains(response, query['actualbookCategory'])

    # test if the searched book does exists when category is selected
    def test_if_searchedBook_exists_with_category_selected(self):
        query = {'actualbookTitle':'Hello Fellows', 'actualbookCategory':'AndelaTestCategory'}
        response = self.client.get(self.url, query)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, query['actualbookTitle'], html=True)
        self.assertContains(response, query['actualbookCategory'])
