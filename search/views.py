from django.core import paginator
from django.shortcuts import render
from articles.models import Article
from meeting_reports.models import MeetingReport
from researchs.models import Research
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def search(request):

    q = request.GET.get('q',None)
    results = None
    context = {'results':results}
    if q:
        articles = Article.objects.filter(Q(title__icontains=q) |Q(content__icontains=q))
        meeting_reports = MeetingReport.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        researchs = Research.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

        results = list(chain(articles, meeting_reports, researchs))

        page = request.GET.get('page',1)

        paginator = Paginator(results, 10)

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        context = {'results':results}

    return render(request, 'search/search.html', context)


