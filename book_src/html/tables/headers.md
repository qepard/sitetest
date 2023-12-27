# Заголовки таблиц

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
## `<th>`
Элемент `<th>`(1) используется точно так же, как и элемент `<td>`, однако его назначение - создание заголовка строки или столбца.

Помните, что даже если ячейка не содержит данных, то вы все равно должны представить ее пустым элементом `<td>` или `<th>`, в противном случае таблица будет некорректно отображена в браузере. (В примере первая ячейка первой строки пустая.)

Употребление элемента `<th>` помогает людям, использующим программы экранного доступа, улучшает результативность индексирования таблиц поисковыми системами, а еще этот элемент помогает управлять оформлением таблиц при использовании **CSS**.
</div>

1.  Table heading(*англ.*) — заголовок таблицы.

<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<table>
    <tr>
        <th></th>
        <th scоpe="col">Суббота</th>
        <th scоpe="col">Bоскресенье</th>
    </tr>
    <tr>
        <th scоpе="row">Продано билетов</th>
        <td>120</td>
        <td>135</td>
    </tr>
    <tr>
        <th scope="row">Выручка</th>
        <td>18 000 руб.</td>
        <td>20 250 руб.</td>
    </tr>
</table>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/tableheaders.png"></figure></div></div>

<div style="display:flex;margin-top:-20px;" class="annotate" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Для обозначения того, относится ли данный заголовок к строке или столбцу, вы можете воспользоваться атрибутом scope элемента `<th>`.
</div>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Этот атрибут способен принимать одно из двух значений: `row`(1) или `col`(2) для обозначения, к чему именно (к строке или столбцу) относится данный заголовок.
</div></div>

1.  Row (*англ.*) — строка.
2.  Column (*англ.*) — столбец.

Как правило, браузеры выделяют полужирным шрифтом содержимое элемента `<th>` и выравнивают его по центру ячейки.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/base'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/union'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
