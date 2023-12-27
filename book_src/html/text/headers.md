# Заголовки

<h2>&lt;h1&gt; &lt;h2&gt; &lt;h3&gt; &lt;h4&gt; &lt;h5&gt; &lt;h6&gt;</h2>

<div style="display: flex;" markdown>
<div style="flex: 1;" markdown>
В языке **HTML** существует шесть уровней заголовков:

* `<h1>` используется для основных заголовков

* c `<h2>` по `<h6>` для подзаголовков

Если текст разделен на фрагменты более глубокого уровня, то для них используются заголовки `<h3>` и ниже.

Браузеры отображают содержимое элементов- заголовков шрифтом разного размера.

Текст заголовка `<h1>` выводится самым крупным шрифтом, текст заголовка `<h6>` - самым мелким.
</div>
<div class="code-example" style="flex: 1;" markdown>
``` html title="Заголовки"
<h1>Основной заголовок</h1>
<h2>Заголовок 2-го уровня</h2>
<h3>Заголовок 3-го уровня</h3>
<h4>Заголовок 4-го уровня</h4>
<h5>Заголовок 5-го уровня</h5>
<h6>Заголовок 6-го уровня</h6>
```
<figure><figcaption>Результат</figcaption><img width="380" height="212" src="/html-css-manual/assets/images/headerexample.png"></figure></div></div>

Размер шрифта, используемый разными браузерами для отображения заголовков разного уровня, незначительно отличается. Кроме того, пользователи также могут отрегулировать размер шрифта отображаемого текста. 

Вы узнаете, как устанавливать размер, цвет и гарнитуру текста, когда мы перейдем к изучению каскадных таблиц стилей (**CSS**).

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/bolditalic'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
