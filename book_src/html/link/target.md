# Открытие ссылок в новом окне

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;width:40%;" markdown>
## target

Чтобы создать ссылку, открывающую страницу в новом окне браузера, вы можете воспользоваться атрибутом `target` открывающего тега элемента `<a>`.

Значение этого атрибута должно быть установлено в `_blank`.

</div><div style="flex:1;margin-right:10px;width:60%;" markdown>
``` html title="Код"
<a href="http://www.imdb.com" target="_blank">
База данных фильмов во Всемирной паутине</a>
(открывается в новом окне)
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/targetex.png"></figure></div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;width:50%;" markdown>
Чаще всего ссылки данного вида ставятся, когда щелчок по ним должен вести к переходу на сторонний сайт.
</div><div style="flex:1;margin-right:10px;width:50%;" markdown>
В этом случае создатели сайтов надеются, что посетитель вернется на их сайт по завершении просмотра открывшейся страницы.
</div></div>

В обычной ситуации следует избегать открытия ссылок в новом окне, однако если вы используете этот прием, то будет не лишним заранее предупредить посетителя, что страница откроется в новом окне.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/mail'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
