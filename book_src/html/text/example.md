# Пример

## Это очень простая HTML-страница, демонстрирующая разметку текста. 

Структурная разметка текста включает такие элементы как `<h1>`, `<h2>` и `<p>`.

Семантическая информация представлена в таких элементах, как `<cite>` и `<em>`.

``` html title="Код"
<html>
    <head>
        <title>Текст</title>
    </head>
    <body>
        <hl>Роман без названия</h1>
        <h2>Глава 1</h2>
        <p>Мария стояла перед окном уже около часа. 
            На столе, между экземплярами <i>"GEO"</i> и других журналов, 
            в которых публиковались ее статьи, лежала зачитанная книга 
            <cite>"В дороre"</cite>. 
            Это была любимая книга Марии еще со школьной скамьи, 
            и чем больше времени она проводила в четырех стенах этой комнаты, 
            тем больше она понимала, что хочет вырваться на свободу. </p>
        <p>Последние десять лет она провела в этой комнате, 
            сидя под плакатом с цитатой Оскара Уайльда, гласящей: 
            <q>Работа - это убежище для людей, которым больше нечем заняться</q>. 
            Хотя многие считали ее поистине пионерскую работу по изучению 
            <dfn>генома</dfn> человека большим достижением, 
            Марию не покидала мысль, что у нее 
            <em>есть</em> более достойные занятия…</р>
    </body>
</html>
```

<center>[Результат](/html-css-manual/assets/files/TEXTEX.html){ .md-button }

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/insdel'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/lists'"><span style="margin: 0 10px;">Следующая глава</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
