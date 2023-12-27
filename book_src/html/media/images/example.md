# Пример изображения

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
В приведенном примере логотип - это изображение в формате *GIF* (оно содержит однотонные участки), а фотографии сохранены в формате *JPEG*.

Основная фотография помещена в элемент `<figure>` языка **HTML5** и у нее есть подпись.
</div>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
Атрибут `alt` каждого из изображений предоставляет описание того, что можно видеть на рисунке, для посетителей сайта, использующих программы экранного доступа.

Атрибут `title` содержит дополнительную информацию, выводимую во всплывающей подсказке.
</div>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
В этом примере вы не увидите таких атрибутов, как `height`, `width` и `align`.

На сегодняшний день они считаются устаревшими и вместо них рекомендуется использовать соответствующие свойства каскадных таблиц стилей (**CSS**).
</div></div>

``` html title="Код"
<html>
    <head>
        <title>Изображения</title>
    </head>
    <body>
        <h1>
            <img src="images/logo.gif" alt="От А до Яблока" />
        </h1>
        <figure>
            <img src="images/chocolate-islands.jpg"
            alt="Шоколадные острова" 
            title="Уникальные кексы Шоколадных островов" />
            <p>
                <figcaption>
                    Этот рецепт для приготовления уникальных 
                    шоколадных кексов так прост и так восхитителен!
                </figcaption>
            </p>
        </figure>
        <h4>Еще рецепты:</h4>
            <p>
                <img src="images/lemon-posset.jpg"
                alt="Лимонный поссет" 
                title="Десерт - лимонный поссет" />
                <img src="images/roasted-brussel-sprouts.jpg"
                alt="Жареная брюссельская капуста" 
                title="Гарнир из жареной брюссельской капусты" />
                <img src="images/zucchini-cake.jpg" 
                alt="Яблочный пирог" 
                title="Яблочный пирог без охлаждения" />
            </p>
    </body>
</html>
```

<center>[Результат](/html-css-manual/assets/files/IMGEX.html){ .md-button }

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/figure'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/video'"><span style="margin: 0 10px;">Следующая глава</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
