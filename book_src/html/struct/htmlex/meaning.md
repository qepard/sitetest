# Структура веб-страниц

## Значение кода

Теперь давайте более детально рассмотрим код, с которым вы познакомились на предыдущей странице, нажимая на знак (1), описывающий каждый элемент:
{ .annotate }

1.  Это аннотация-описание.

<div class="annotate" markdown>
``` html title="Код страницы"
<html>(1)
    <body>(2)
        <h1>Это основной заголовок</h1>(3)
        <p>Этот текст может быть введением к тексту, помещенному под заголовком.
            Он может быть достаточно длинным, поэтому автоматически переносится на новую строку. 
            Также, данный текст может быть разделен на несколько разделов с подзаголовками.
        </p>(4)
        <h3>Это подзаголовок</h3>(5)
        <p>Часто при написании статей используют подзаголовки для лучшего понимания содержания публикации.
            Такими приемами пользуются все: от копирайтеров до создателей сайтов.
            Они используются во всех бумажных и веб документах.</p>(6)
        <h2>Еще один подзаголовок</h2>(7)
        <p>Вот еще один пример подзаголовка.</p>(8)
    </body>(9)
</html>(10)
```
</div>

1.  Открывающий тег **&lt;html&gt;** означает, что все, помещенное между ним и закрывающим тегом **&lt;/html&gt;**, является HTML-кодом.
2.  Тег **&lt;body&gt;** сообщает, что все, помещенное между ним и закрывающим тегом **&lt;/body&gt;**, должно быть отображено в основном окне браузера.
3.  Текст между тегами **&lt;h1&gt;** и **&lt;/h1&gt;** представляет основной заголовок.
4.  Абзац текста должен быть помещен между тегами **&lt;p&gt;** и **&lt;/p&gt;**.(1)
    { .annotate }

    1.  От *англ.* paragraph — абзац.

5.  Текст между тегами **&lt;h3&gt;** и **&lt;/h3&gt;** представляет подзаголовок.
6.  Это еще один абзац текста, помещенный между тегами **&lt;p&gt;** и **&lt;/p&gt;**.
7.  Еще один подзаголовок между тегами **&lt;h2&gt;** и **&lt;/h2&gt;**.
8.  Еще один абзац текста между тегами **&lt;p&gt;** и **&lt;/p&gt;**.
9.  Закрывающий тег **&lt;/body&gt;** означает окончание контента, который должен быть отображено в основном окне браузера.
10. Закрывающий тег **&lt;/html&gt;** означает конец HTML-кода.

Элементы аналогичны контейнерам. Они сообщают какую-либо информацию о тексте, расположенном между открывающи и закрывающим тегами.

## Теги

|||
|:-:|:-:|
|<div style="display: flex; justify-content: space-between; width: 100%;"><svg width="400" height="200" xmlns="http://www.w3.org/2000/svg"><text x="110" y="99" font-family="Roboto" font-size="80">&lt;p&gt;</text><text x="60" y="155" font-family="Roboto" font-size="24">Открывающий тег</text></svg></div>|<div style="display: flex; justify-content: space-between; width: 100%;"><svg width="400" height="200" xmlns="http://www.w3.org/2000/svg"><text x="105" y="100" font-family="Roboto" font-size="80">&lt;/p&gt;</text><text x="70" y="155" font-family="Roboto" font-size="24" font-size="small">Закрывающий тег</text></svg></div>|

Символы в скобках означают, для каких целей можно использовать данный тег.

Например, тегом `р` обозначается абзац текста.

Отличием закрывающего тега является наличие `/` после символа `<`.

Термины «тег» и «элемент» зачастую используются как синонимы.

Однако, строго говоря, элемент включает в себя и открывающий тег, и закрывающий, а также любой контент, расположенный между ними.

## Атрибуты

Атрибуты предоставляют дополнительную информацию о содержимом HTML-элементов. Они располагаются воткрывающем теге элемента и состоят из двух частей: {==имени==} и {==значения==}, разделенных знаком «равно».

```html title="Пример атрибута"
<p lang="ru">Текст на русском языке.</p>
```

**Имя** атрибута определяет, какого рода дополнительную информацию о содержимом элемента вы намереваетесь сообщить, в то время как **значение** — это собственно информация или настройка элемента, изменяемая атрибутом. Значение следует заключить в двойные кавычки. 

У разных атрибутов могут быть различные значения.
В качестве примера приводится атрибут `lang`, используемый, для обозначения языка текста данного элемента.

``` html title="Пример атрибута"
<p lang="en-US">Paragraph is English</p>
```

Большинство атрибутов могут быть использованы только с определенными элементами. Несмотря на это некоторые атрибуты (например, `lang`) допускается ставить в любом элементе. Значением атрибута `lang` может быть сокращенное обозначение языка содержимого элемента. Браузеры должны распознавать это сокращение.

Большинство значений атрибутов могут быть либо предопределенными, либо установленными в соответствии с принятыми стандартами. 
По мере изучения атрибутов вы также узнаете и о доступных для них значениях. 

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/struct/htmlex/'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/struct/bhtelem'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>

<script>function changeSVGColor(color) {var svgs = document.getElementsByTagName('svg');for (var i = 0; i < svgs.length; i++) {var svg = svgs[i];var textElements = svg.getElementsByTagName('text');for (var j = 0; j < textElements.length; j++) {textElements[j].style.fill = color;}}}var body = document.body;var observer = new MutationObserver(function(mutations) {mutations.forEach(function(mutation) {if (mutation.attributeName === 'data-md-color-scheme') {var theme = body.getAttribute('data-md-color-scheme');if (theme === 'slate') {changeSVGColor('white');} else {changeSVGColor('black');}}});});observer.observe(body, { attributes: true });</script>
