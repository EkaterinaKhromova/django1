def index(request):
    return render(
	    request,
		'mainpage/index.html',
		{}  # словарь контекста
	)