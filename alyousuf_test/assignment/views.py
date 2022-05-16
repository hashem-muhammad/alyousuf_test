from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from assignment import forms
from assignment.models import Post
# Create your views here.


def testview(request):
    return render(request, 'index.html', {
        'title': 'Home'
    })


def loginView(request):
    form = forms.loginForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            email = cleaned_data['email']
            password = cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None and user.is_authenticated:
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'assets/pages/login.html', {
        'title': 'Login',
        'form': form,
    })


@login_required(login_url='/login/')
def uploadCsvView(request):
    data = {}
    if "GET" == request.method:
        return render(request, "assets/pages/csv.html", data)
    # if not GET, then proceed
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            check_file = 'should be CSV only'
            return render(request, 'assets/pages/csv.html', {'done': check_file})
        fs = FileSystemStorage()
        filename = fs.save(csv_file.name, csv_file)
        uploaded_file_url = fs.path(filename)
        with open(uploaded_file_url, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                Post.objects.bulk_create([Post(
                    title=row[0],
                    details=row[1],
                    image=row[2],
                    posted_date=datetime.date.today()
                )])
        done_upload = 'File Uploaded'
        return render(request, 'assets/pages/csv.html', {'done': done_upload})
    return render(request, 'assets/pages/csv.html')


def contentView(request):
    if "GET" in request.method:
        page = request.GET.get('page', 1)
        post_data = Post.objects.values(
            'id', 'title', 'image', 'details', 'posted_date')

        paginator = Paginator(post_data, 4)
        try:
            post_data = paginator.page(page)
        except PageNotAnInteger:
            post_data = paginator.page(1)
        except EmptyPage:
            post_data = paginator.page(paginator.num_pages)
    return render(request, "assets/pages/content.html", {'response': post_data})
