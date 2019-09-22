from django.shortcuts import render
from django.http import HttpResponse
from searchApp.models import bookCategory, actualBook
from searchApp.forms import searchInputForm
import datetime

# from . import views           #the . represents like saying from all apps

# Create your views her.

# Create simple Hello response
def indexPage(request):
    currentDateTime = datetime.datetime.now()
    return render(request, 'baseTemplates/basePage.html', {'currentDateTime': currentDateTime})

# reference the templates
def searchPage(request):
    if request.GET:

        # form object is initialised with GET request
        searchInputFormValue = searchInputForm(request.GET)

        # test if form data is valid (i.e. both field being filled)
        if searchInputFormValue.is_valid():
            # cleaned_data[] is used instead of data[] due to validating form
            # import pdb; pdb.set_trace()

            try:
                requestCategoryID = request.GET['actualbookCategory']
            except:
                requestCategoryID = None

            # when book is selected but category is blank
            # import pdb; pdb.set_trace()
            if searchInputFormValue.cleaned_data['actualbookTitle'] and searchInputFormValue.cleaned_data['actualbookCategory'] == None:
                searchResult = actualBook.objects.filter(actualbookTitle__icontains=searchInputFormValue.cleaned_data['actualbookTitle'])
                return render(request, 'resultPage.html', {'searchResult': searchResult})

            # when book is blank but category is selected
            elif searchInputFormValue.cleaned_data['actualbookTitle'] is None and searchInputFormValue.cleaned_data['actualbookCategory'].categoryName:
                searchResult = actualBook.objects.filter(actualbookCategory_id=requestCategoryID)
                return render(request, 'resultPage.html', {'searchResult': searchResult})

            # when both book and category are selected (also handles even if category is wrong i.e. filter parameters works like an innerjoin or and statement)
            elif searchInputFormValue.cleaned_data['actualbookTitle'] and searchInputFormValue.cleaned_data['actualbookCategory'].categoryName:
                searchResult = actualBook.objects.filter(actualbookTitle__icontains=searchInputFormValue.cleaned_data['actualbookTitle'], actualbookCategory_id__exact=requestCategoryID)
                return render(request, 'resultPage.html', {'searchResult': searchResult})

        else :
            # handeles the scenario when data inputed is not valid
            searchInputFormValue = searchInputForm()
            return render(request, 'searchPage.html', {'searchInputFormValue': searchInputFormValue})

    # handles when there is no get request
    searchInputFormValue = searchInputForm()
    return render(request, 'searchPage.html', {'searchInputFormValue': searchInputFormValue})
