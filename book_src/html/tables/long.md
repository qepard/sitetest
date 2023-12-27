# Длинные таблицы

В языке **HTML** существуют три элемента, помогающих отличить основной контент страницы от первой и последней ее строк (которые иногда содержат принципиально отличающуюся информацию).

Эти элементы полезны людям, использующим программы экранного доступа, а кроме того, они помогают вам выделять данные разделы таблицы особым стилем (что вы научитесь делать, начав изучать **CSS**).

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `<thead>`

Заголовки таблицы должны быть помещены в элемент `<thead>`.
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `<tbody>`

Основное содержимое (тело) таблицы должно находиться внутри элемента `<tbody>`.
</div></div>
<div style="margin-top:-20px" markdown>
## `<tfoot>`

Последняя, завершающая, строка таблицы должна быть указана внутри элемента `<tfoot>`.

По умолчанию очень немногие браузеры хоть как-либо выделяют содержимое этих трех элементов, однако веб-дизайнеры изменяют их внешний вид с помощью каскадных таблиц стилей (**CSS**).
</div>
<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>

``` html title="Код"
<table>
    <thead>
        <tr>
            <th>Дата</th>
            <th>Прибыль</th>
            <th>Расход</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>1-e января</th>
            <th>250</th>
            <th>36</th>
        </tr>
        <tr>
            <th>2-е января</th>
            <th>285</th>
            <th>48</th>
        </tr>
            <th>31-e января</th>
            <th>129</th>
            <th>64</th>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <td></td>
            <th>7824</th>
            <th>1241</th>
        </tr>
    </tfoot>
</table>
```
</div>
<div style="flex:1;width:50%;" markdown>
<figure style="margin-top:-5px"><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/longtablex.png"></figure></div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
Часть **HTML**-редакторов, встроенных в системы управления контентом (*CMS*), обладает инструментами, которые позволяют создавать таблицы.

Если первая строка вашей таблицы содержит только элементы `<th>`, то вы можете увидеть, как редактор автоматически вставит элемент `<thead>`.
</div>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
Одна из причин использования элементов `<thead>` и `<tfoot>` заключается в том, что если ваша таблица слишком длинная для единовременного отображения на экране (или для печати), то браузер будет отображать и заголовок (`<thead>`) и последнюю строку (`<tfoot>`), когда пользователь станет прокручивать вашу таблицу.
</div>
<div style="flex:1;width:33%;" markdown>
Так делается, чтобы пользователи могли видеть, в каких столбцах находятся отображаемые данные.

Однако эта функция присутствует не во всех современных браузерах.
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/union'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
