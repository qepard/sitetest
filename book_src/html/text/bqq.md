# Цитаты

Для создания цитат в языке **HTML** используются два элемента:

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;" markdown>
<h2>&lt;blockquote&gt;</h2>

Элемент `<blockquote>` используется для отображения длинных цитат, занимающих целый абзац.

Обратите внимание, что внутри элемента `<blockquote>` необходимо использовать и элемент `<p>`.

В большинстве своем браузеры склонны к выделению содержимого элемента `<blockquote>` отступами.

Однако этот элемент не стоит использовать только лишь для того, чтобы создать фрагмент текста с отступом: лучше реализовать такое с помощью каскадных таблиц стилей (**CSS**).
</div><div style="flex:1;" markdown>
<h2>&lt;q&gt;</h2>

Элемент `<q>` принято использовать для более коротких цитат, помещающихся внутри абзаца текста.

Для обоих элементов может быть указан атрибут `cite`, указывающий, с какого сайта позаимствована та или иная цитата.

Значение этого атрибута - URL-адрес сайта, содержащего более подробную информацию об источнике цитирования.

</div></div>

``` html title="Код"
<blockquote cite="http://ru.wikipedia.org/wiki/Винни-Пух">
<p>- Интересно, что это так бумкнуло?
Не мог же я один наделать столько шума.
И где, интересно знать, мой воздушный шарик?
И откуда, интересно, взялась эта тряпочка?
</p>
</blockquote>
<p>Как сказал A. A. Милн, 
<q>некоторые люди говорят с животными.
И лишь немногие слушают.
Вот в чем проблема</q>.
</p>
```
<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/bqq.png"></figure>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/supsub'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/abbr'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
