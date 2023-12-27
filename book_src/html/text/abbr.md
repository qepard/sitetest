# Аббревиатуры и акронимы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;" markdown>
## &lt;abbr&gt;

При употреблении в тексте какого-либо акронима или аббревиатуры следует воспользоваться тегом `<abbr>`. В открывающем теге можно использовать атрибут title для указания расшифровки сокращения.

В языке **HTML4** для описания акронимов был реализован специальный элемент `<acronym>`. 

Для отображения расшифровки акронима использовался атрибут `title` (аналогичный атрибуту элемента `<abbr>`). 

В языке **HTML5** и для аббревиатур, и для акронимов используется тег `<abbr>`.

</div>
<div style="flex: 1;" markdown>
``` html title="Код"
<p><abbr title="Профессоp">Пр.</abbr>
Стивен Хокинг - физик-теоретик и космолог.</р>
<p><acronym title="Национальное агентство
по аэронавтике и исследованию космического
пространства">NASA</acronym> проводит несколько
невероятных космических экспериментов.</p>
```
<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/abbr.jpg"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/bqq'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/citedfn'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
