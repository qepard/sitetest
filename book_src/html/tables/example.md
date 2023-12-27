# Пример таблицы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
В этом примере мы создадим таблицу, демонстрирующую клиентам разные тарифные планы на услуги размещения сайта на сервере (хостинг).

Первая строка и первый столбец таблицы представляют собой заголовки.
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Несмотря на то, что верхняя левая ячейка не содержит информации, для нее все равно создан отдельный элемент `<th>`.

Каждая ячейка таблицы должна быть представлена либо элементом `<th>`, либо `<td>`.
</div>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Для элемента `<th>` можно установить атрибут `scopе`, чтобы указать к чему относится данный заголовок: к строке или столбцу.

В последней строке таблицы используется атрибут `colspan` для объединения всех ее ячеек в одну.
</div></div>

``` html title="Код"
<html>
    <head>
        <title>Таблицы</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th></th>
                    <th scope="col">Хостинг "Домашний начальный"</th>
                    <th scope="col">Хостинг "Домашний Премиум"</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">Дисковое пространство</th>
                    <td>1 Гб</td>
                    <td>3 Гб</td>
                </tr>
                <tr>
                    <th scope="row">Трафик</th>
                    <td>15 Гб/мес</td>
                    <td>50 Гб/мес</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td></td>
                    <td colspan="2">Закажи сейчас и сэкономь 10%!</td>
                </tr>
            </tfoot>
        </table>
    </body>
</html>
```

<center>[Результат](/html-css-manual/assets/files/TABLEX.html){ .md-button }

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/tables/long'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms'"><span style="margin: 0 10px;">Следующая глава</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
