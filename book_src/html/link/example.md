# Пример ссылки

<h2>Данный пример - это веб-страница о расписании кинофестивалей.</h2>

Элементу `<h1>` присвоен атрибут `id`, чтобы можно было создать ссылку, щелчок мышью по которой переместил бы посетителя с нижней части страницы в верхнюю. 

На странице также размещена ссылка на электронную почту, позволяющая написать автору веб-страницы.

Кроме того, на странице есть несколько ссылок на сайты, посвященные различным кинофестивалям.

В нижней части страницы расположена относительная ссылка на страницу «О сайте», находящуюся в той же директории, что и страница-пример.

``` html title="Код"
<html>
    <head>
        <title> Ссылки</title>
    </head>
    <body>
        <h1 id="top">Фестивали</h1>
        <h2>Кинофестивали</h2>
        <p>Здесь вы найдете информацию о кинофестивалях,
        которые пройдут в этом году.<br />Пожалуйста, 
        <a href="mailto:filmfestival@example.org"> свяжитесь с нами</a>, 
        если обладаете дополнительной информацией. </p>
        <h3>Февраль</h3>
        <p><a href="https://www.berlinale.de/en/HomePage.html">
        Берлинский международный кинофестиваль</a><br /> Берлин, Германия<br />7-17 февраля 2013 года</p>
        <h3>Май</h3>
        <p><a href="https://www.festival-cannes.com/ru.html">
        Каннский кинофестиваль</a><br />Канны, Франция<br /> 15-26 мая 2013 года</p>
        <p><a href="about.html">О сайте</a></p>
        <p><a href="#top">Вверх</a></p>
    </body>
</html>
```

<center>[Результат](/html-css-manual/assets/files/LINKEX.html){ .md-button }

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/target'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
