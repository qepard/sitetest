# Объединение столбцов

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Иногда вам может понадобиться, чтобы ячейка таблицы занимала не один, а несколько столбцов. 

Атрибут `colspan` может быть использован с элементами `<th>` и `<td>` для обозначения, сколько столбцов должна занимать ячейка.

В примере справа вы можете видеть расписание, состоящее из пяти столбцов: первый содержит заголовок строки (день недели), оставшиеся четыре представляют собой часы. 

Если вы посмотрите на код ячейки с текстом «География», то увидите, что значение атрибута `colspan` равно 2, это значит, что ячейка должна занимать два столбца. 

Ячейка «Физкультура», расположенная на третьей строке, занимает три столбца.

Вы также можете видеть, что вторая и третья строки состоят из меньшего количества элементов `<td>`.
</div>
<div style="flex:1;margin-right:20px;width:60%;" markdown>
``` html title="Код"
<table>
    <tr>
        <th></th>
        <th>9:00</th>
        <th>10:00</th>
        <th>11:00</th>
        <th>12:00</th>
    </tr>
    <tr>
        <th>Понедельник</th>
        <td colspan="2">География</td>
        <td>Mузыка</td>
        <td>Изо</td>
    </tr>
    <tr>
        <th>Вторник</th>
        <td colspan="3">Физкультура</td>
        <td>География</td>
    </tr>
</table>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/colspanex.jpg"></figure></div></div>

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Дело в том, что если какая-либо ячейка занимает несколько столбцов, то занятые ею элементы `<td>` в коде не прописываются.
</div>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Для иллюстрации этого примера я использовал несколько стилей **CSS** с тем, чтобы показать вам, как одна ячейка может занимать сразу несколько столбцов.
</div></div>
<hr>

# Объединение строк

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
Кроме того, вам может понадобиться сделать так, чтобы одна ячейка занимала несколько строк.

Атрибут rowspan может быть использован с элементами `<th>` и `<td>` для обозначения, на сколько строк должна простираться ячейка.

В примере слева вы можете видеть, что телеканал *TV1000* показывает фильм с 18:00 до 20:00, а в это время на каналах *ТНТ* и *СТС* транслируются по две развлекательные телепередачи (каждая из которых длится один час).

Если вы посмотрите на последний элемент `<tr>`, то увидите, что он содержит только три элемента, несмотря на то что в таблице на рисунке ниже четыре столбца.

Это произошло потому, что в элементе `<tr>`, содержащем текст «Фильм», указан атрибут `rowspan`, благодаря которому он «поглотил» расположенную ниже ячейку.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<table>
    <tr>
        <th></th>
        <th>TV1000</th>
        <th>THT</th>
        <th>CTC</th>
    </tr>
    <tr>
        <th>20:00-21:00</th>
        <td rowspan="2">Фильм</td>
        <td>Ток-шоу</td>
        <td>Юмор</td>
    </tr>
    <tr>
        <th>21:00-22:00</th>
        <td>Ток-шоу</td>
        <td>Мультфильм</td>
    </tr>
</table>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/rowspanex.jpg"></figure></div></div>

Для иллюстрации этого примера я использовал несколько параметров стиля **CSS** с тем, чтобы показать вам, как одна ячейка может занять сразу несколько строк.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/headers'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/long'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
