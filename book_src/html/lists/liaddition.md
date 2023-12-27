# Вложенные списки

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## Списки второго уровня

Внутри элемента `<li>` допустимо создание вложенного списка, или списка второго уровня.

Браузеры отображают вложенные списки с большим отступом по сравнению с основным, или родительским, списком.

Кроме того, браузер, как правило, также изменяет вид маркеров вложенного неупорядоченного списка.
</div>
<div style="flex: 1;width:50%;" markdown>
``` html title="Код"
<ul>
    <li>Муссы</li>
    <li>Пирожные
        <ul>
            <li>Круассаны</li>
            <li>Наполеон</li>
            <li>Чизкейки</li>
            <li>Профитроли</li>
        </ul>
    </li>
    <li>Торты</li>
</ul>
```
<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/liaddition.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/lists/dltd'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/lists/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>

