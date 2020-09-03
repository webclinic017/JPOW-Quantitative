from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from jpow_app.models import SPY, Ratio, Insider, Compensation, UnusualOption
import json
from scipy import stats

def saveUser(data):
    username = data['username']
    email = data['email']
    password = data['password1']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

def home_page(request):
    if request.method == "POST":
        if 'login' in request.POST:
            form = LoginForm(data = request.POST)
            username = request.POST['username']
            password = request.POST['password']
            if form.is_valid():
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                form = LoginForm(data = request.POST)
                signform = SignUpForm(None)
            return render(request, 'jpow_app/home_page.html', {'formLogin': form, 'formSignup': signform})
        else:
            signform = SignUpForm(data = request.POST)
            if signform.is_valid():
                saveUser(request.POST)
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                form = LoginForm(None)
                signform = SignUpForm(data = request.POST)
                return render(request, 'jpow_app/home_page.html', {'formLogin': form, 'formSignup': signform})
    form = LoginForm()
    signform = SignUpForm()
    return render(request, 'jpow_app/home_page.html', {'formLogin': form, 'formSignup': signform})

def about_page(request):
    if request.method == "POST":
        if 'login' in request.POST:
            form = LoginForm(data = request.POST)
            username = request.POST['username']
            password = request.POST['password']
            if form.is_valid():
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/dashboard')
        else:
            signform = SignUpForm(data = request.POST)
            if signform.is_valid():
                saveUser(request.POST)
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/dashboard')
    form = LoginForm()
    signform = SignUpForm()
    return render(request, 'jpow_app/about_page.html', {'formLogin': form, 'formSignup': signform})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def dashboard_home(request):
    return render(request, 'jpow_app/dashboard_home.html')

@login_required
def retail_sentiment(request):
    #get current retail sentiment
    query = Ratio.objects.latest('Date')
    positive_sentiment = str(query.PositiveSentiment)
    date = query.Date.strftime("%b %d, %Y")

    #get historical retail sentiment
    query = Ratio.objects.all().order_by('Date')
    historical_sentiment = []
    historical_dates = []
    for obj in query:
        historical_sentiment.append(str(obj.PositiveSentiment))
        historical_dates.append(str(obj.Date))

    #get historical SPY data
    query = SPY.objects.all().order_by('Date')
    historical_price_spy  = []
    historical_dates_spy = []
    for obj in query:
        historical_price_spy.append(str(obj.closePrice))
        historical_dates_spy.append(str(obj.Date))
    return render(request, 'jpow_app/retail_sentiment.html', {'current_sentiment': json.dumps({'Date': date, 'sentiment': positive_sentiment, 'prior_sentiment': historical_sentiment[-2]}),
                                                            'historical_sentiment': json.dumps({'Date': historical_dates, 'sentiment': historical_sentiment}),
                                                            'spy': json.dumps({'Date': historical_dates_spy, 'closing price': historical_price_spy})})
@login_required
def insider_trading(request):
    objects = Insider.objects.all().order_by('-Date')
    ticker, senator, purchase, amount, date = [], [] , [], [], []
    for o in objects:
        ticker.append(o.Ticker)
        senator.append(o.Senator)
        purchase.append(o.PurchaseType)
        amount.append(o.Amount)
        date.append(str(o.Date))
    rows = zip(ticker, senator, purchase, amount, date)
    return render(request, 'jpow_app/insider_trading.html', {'rows': rows})

@login_required
def ceo_comp(request):
    ytdReturn = []
    ceoSalary = []
    tickers = []
    objects = Compensation.objects.all()
    for o in objects:
        ytdReturn.append(float(o.YTDReturn))
        ceoSalary.append(o.CeoSalary)
        tickers.append(o.Ticker)
    slope, intercept, r_value, p_value, std_err = stats.linregress(ceoSalary, ytdReturn)
    bestFit = [round((slope*x + intercept),2) for x in ceoSalary]
    ytdReturn = [str(x) for x in ytdReturn]
    return render(request, 'jpow_app/ceo_comp.html', {'data': json.dumps({'ytd': ytdReturn, 'sal': ceoSalary,
                                                                          'tickers': tickers, 'best_fit': bestFit})})

@login_required
def options(request):
    objects = UnusualOption.objects.all().order_by('ExpirationDate')
    ticker, type, strike, volume, oi, date = [], [] , [], [], [], []
    for o in objects:
        ticker.append(o.Ticker)
        type.append(o.Type)
        strike.append("$" + o.Strike + "0")
        volume.append(o.Volume)
        oi.append(o.OpenInterest)
        date.append(str(o.ExpirationDate))
    rows = zip(ticker, type, strike, volume, oi, date)
    return render(request, 'jpow_app/options.html', {'rows': rows})
