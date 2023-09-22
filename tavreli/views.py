from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

html_home = """
<html>
<head>
    <title>Главная</title>
</head>
<body>
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Меня зовут Юрий и я рада приветствовать вас на моем сайте.</p>
</body>
</html>
"""

html_about = """
<html>
<head>
    <title>О себе</title>
</head>
<body>
    <h1>Обо мне</h1>
    <p>Меня зовут Юрий и я начинающий разработчик Django.</p>
    <p>Здесь я собираюсь делиться своими знаниями и опытом.</p>
</body>
</html>
"""


@csrf_exempt
def home_view(request):
    logger.info('Главная страница была посещена')
    return render(request, 'tavreli/home.html', {'html': html_home})


@csrf_exempt
def about_view(request):
    logger.info('Страница "О себе" была посещена')
    return render(request, 'tavreli/about.html', {'html': html_about})
