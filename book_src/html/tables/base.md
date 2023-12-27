# Базовая структура таблицы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
## `<table>`
Для создания таблиц используется элемент `<table>`.

Контент таблицы описывается построчно.

## `<tr>`
Открывающий тег `<tr>`(1) обозначает начало новой строки таблицы.

После него помещаются элементы `<td>`, каждый из которых соответствует отдельной ячейке в этой строке.

Конец строки обозначается закрывающим тегом `</tr>`.

## `<td>`
Каждая ячейка таблицы должна быть представлена элементом `<td>`(2).

Конец ячейки обозначается закрывающим тегом `</td>`.

Некоторые браузеры автоматически создают линии вокруг таблиц и/или ячеек.
</div>

1.  Table row(*aнгл.*) — строка таблицы.
2.  Table data(*aнгл.*) — данные таблицы.

<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<table>
    <tr>
        <td>15</td>
        <td>15</td>
        <td>30</td>
    </tr>
    <tr>
        <td>45</td>
        <td>60</td>
        <td>45</td>
    </tr>
    <tr>
        <td>60</td>
        <td>90</td>
        <td>90</td>
    </tr>
</table>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/tableex.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/headers'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
