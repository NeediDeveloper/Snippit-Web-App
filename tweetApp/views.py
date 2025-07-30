from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from tweet.models import Tweet


benefit_lines = [
    "Snippit is where your smallest thoughts find the biggest audiences — because every voice deserves to be heard.",
    "Don’t overthink it — just share it. Your unfiltered thoughts become powerful moments of connection.",
    "Sometimes, a sentence says more than a speech. Share your world, one Snippit at a time.",
    "Snippit gives you the space to be real — raw words, quick insights, and deep impact.",
    "Snippit isn’t just another platform — it’s your playground for ideas and feelings.",
    "From shower thoughts to midnight revelations — post what matters, short and sweet.",
    "It only takes a few words to spark a laugh, change a mind, or start a movement.",
    "Whether you're feeling funny, deep, random, or real — Snippit is your stage.",
    "Join a world where words move fast, and every Snippit tells a story.",
]

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html', {'tweets': tweets, "benefit_lines": benefit_lines})

def about(request):
    return render(request, 'about.html')

def privacypolicy(request):
    return render(request, 'privacy_policy.html')

def terms(request):
    return render(request, 'terms.html')