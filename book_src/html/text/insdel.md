# Исправление контента

<div style="display:flex;" markdown>
<div style="flex:1;margin-top:-20px;margin-right:10px;" markdown>
## &lt;ins&gt; &lt;del&gt;

Элемент `<ins>` может быть использован для отображения контента, добавленного в документ, в то время как `<del>` - для отображения удаленного контента.

Содержимое элемента `<ins>`, как правило, выделяется подчеркиванием, тогда как элемента `<del>` зачеркиванием.

</div>
<div style="flex:1;margin-top:-20px;" markdown>
## &lt;s&gt;

Элемент `<s>` позволяет обозначить, что какая-то информация ошибочна или устарела<br>(но при этом ее не следует убирать со страницы).

Как правило, содержимое элемента `<s>` будет выведено на экран перечеркнутым. 

В старых версиях языка **HTML** использовался элемент `<u>` для вывода текста с подчеркиванием, однако он постепенно уходит в прошлое.
</div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;" markdown>
``` html title="Код"
<p>Это была <del>худшая</del> 
<ins>лучшая</ins>
из ее идей.</p>
```
<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/insdelex.png"></figure></div>
<div style="flex:1;" markdown>
``` html title="Код"
<p>Ноутбук Samsung:</p>
<p>Старая цена:<s>31 900 руб.</s></p>
<p>Новая цена:<ins>11 999 руб.</ins></p>
```
<figure><figcaption>Результат</figcaption><img src="/sitetest/assets/images/stextex.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/citedfn'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/sitetest/html/text/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
