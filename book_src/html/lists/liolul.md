# Упорядоченные и неупорядоченные списки

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## &lt;li&gt;

Каждый элемент списка помещается между открывающим тегом `<li>` и закрывающим тегом `</li>`.

По умолчанию браузеры автоматически расставляют нужные отступы для элементов списков.

Иногда при просмотре существующих страниц вы будете встречать аргумент type в элементе `<ol>`, который используется для указания типа нумерации (буквы, римские и арабские цифры и т.п.).

## &lt;ol&gt;

Упорядоченные списки создаются при помощи элемента `<ol>`.

## &lt;ul&gt;

Неупорядоченные списки создаются при помощи элемента `<ul>`.

</div>
<div style="flex: 1;width:60%;" markdown>
``` html title="Код"
<p>Рецепт</p>
<ul>
    <li>1 кг картофеля</li>
    <li>100 мл молока</li>
    <li>50 г соленого масла</li>
    <li>Тертый мускатный opex</li>
    <li>Соль и перец по вкусу</li>
</ul>
<p>Порядок действий</p>
<ol>
    <li>Порежьте картофель кубиками.</li>
    <li>Варите картофель в соленой воде на медленном огне 
    в течение 15-20 минут до размягчения.</li> 
    <li>Подогрейте и смешайте молоко, 
    сливочное масло и мускатный орех.</li>
    <li>Слейте воду из кастрюли и потолките картофель.</li>
    <li>Перемешайте картофель со смесью из молока, 
    масла и мускатного ореха.</li>
<ol>
```
<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/liolulex.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/lists'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/lists/dltd'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
