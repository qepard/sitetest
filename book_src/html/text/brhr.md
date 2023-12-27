# Перевод строк и горизонтальные линии

<div style="display:flex;" markdown>
<div style="flex:1;margin-top:-20px;" markdown>
## &lt;br /&gt;

Как вы уже видели раньше, браузер автоматически начинает каждый абзац с новой строки.

Однако если вы хотите добавить перевод строки в пределах какого-либо абзаца, то вам понадобится вставить специальный тег — `&lt;br /&gt;`.
</div>
<div style="flex:1;margin-left:10px" markdown>

``` html title="Код"
<p>Земля<br />становится тяжелее 
день ото дня<br />из-за падающей на нее
космической пыли</p>
```
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/html-css-manual/assets/images/brex.png"></figure></div></div>
<hr>
<div style="display:flex;" markdown>
<div style="flex:1;margin-top:-10px" markdown>
## &lt;hr /&gt;

Чтобы визуально разделить темы книги или сцены пьесы, с помощью тега `&lt;hr /&gt;` вы можете добавить в текст горизонтальную линию.

В языке **HTML** существует несколько элементов, не содержащих текста между открывающим и закрывающим тегами.<br>Их принято называть пустыми элементами. 

Написание таких тегов отличается от стандартного. Обычно пустой элемент состоит только из одного тега, перед правой, закрывающей скобкой которого вставляются пробел и слеш. 

</div>
<div style="flex:1;margin-left:10px;margin-top:10px;" markdown>

``` html title="Код"
<p>Венера - единственная планета, 
    вращающаяся по часовой стрелке</p>
<hr />
<p>Юпитер больше,
    чем все остальные планеты
    вместе взятые</p>
```
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/html-css-manual/assets/images/hrex.png"></figure></div></div>

Некоторые верстальщики веб-страниц опускают пробел и слеш, хотя их указание рекомендуется для следования спецификации.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/supsub'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/strongem'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
