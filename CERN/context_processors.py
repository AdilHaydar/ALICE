from articles.models import Article

def last_three_articles(request):
    articles = Article.objects.all()[:3]
    return {'last_three_articles':articles}