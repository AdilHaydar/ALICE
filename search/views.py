from django.shortcuts import render
from articles.models import Article
from meeting_reports.models import MeetingReport
from researchs.models import Research
from django.db.models import Q
from itertools import chain

# Create your views here.

def search(request):

    q = request.GET.get('q',None)
    results = None
    if q:
        articles = Article.objects.filter(Q(title__icontains=q) |Q(content__icontains=q))
        meeting_reports = MeetingReport.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        researchs = Research.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

        results = list(chain(articles, meeting_reports, researchs))
    # ! Modellere get_absolute_url koy çünkü farklı farklı modeller geldiği için {% url '' %} ile link koyamam

    return render(request, 'search/search.html', {'results':results})


