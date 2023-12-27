# Использование языка HTML для описания структуры веб-страниц

## Заголовки в HTML

В окне браузера вы можете увидеть документ с абсолютно таким же содержимым, как и на скриншоте программы Word на предыдущей странице — [Веб пример](/html-css-manual/assets/files/HTMLEX.html){ .md-button .md-button--primary }

Для описания структуры веб-документа необходимо добавить немного кода к тексту, который вы хотите отобразить на экране.

## Код

Ниже на странице приведен код примера на языке HTML.

``` html title="Код страницы"
<html>
    <body>
        <h1>Это основной заголовок</h1>
        <p>Этот текст может быть введением к тексту, помещенному под заголовком.
            Он может быть достаточно длинным, поэтому автоматически переносится на новую строку. 
            Также, данный текст может быть разделен на несколько разделов с подзаголовками.
        </p>
        <h3>Это подзаголовок</h3>
        <p>Часто при написании статей используют подзаголовки для лучшего понимания содержания публикации.
            Такими приемами пользуются все: от копирайтеров до создателей сайтов.
            Они используются во всех бумажных и веб документах.</p>
        <h2>Еще один подзаголовок</h2>
        <p>Вот еще один пример подзаголовка.</p>
    </body>
</html>
```

**HTML-код** выделен <span style="color:#3B77E0;">голубым</span> цветом. Он состоит из символов, помещенных между двух угловых скобок: "&lt;&gt;". Все это называется **HTML-элементами**.

Элементы, как правило, состоят из двух тегов: открывающего и закрывающего. (Внутри закрывающего тега также имеется косая черта,&#171;/&#187;, иначе называемая слеш.) 

Каждый HTML-элемент сообщает браузеру какую-либо информацию о тексте, помещенном между открывающим и закрывающим тегами.

!!!info "Важно"
    <center>Не волнуйтесь по поводу того, что вы не понимаете его назначения.</center>

    Уже со следующей страницы вы начнете подробно знакомиться с ним. Обратите внимание, что HTML-код напечатан голубым цветом, а текст, выводимый на экран, — белым/черным.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/struct/MSWord/'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='meaning/'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
