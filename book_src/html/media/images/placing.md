# Размещение изображений в коде

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:30%;" markdown>
Расположение изображения в коде влияет на то, как оно будет выведено на экран.

Ниже приведено три примера размещения изображения, приводящих к разным результатам.

</div>
<div style="flex:1;width:70%;" markdown>
``` html title="Код"
<img src="images/bird.gif" alt="Птица" width="100" height="100" />
<p>В мире насчитывается более 10 тысяч видов птиц, 
обитающих в различных экосистемах от Арктики до Антарктики. 
Многие виды ежегодно совершают перелеты на длинные расстояния, 
гораздо большее количество совершают более короткие спонтанные путешествия.</p>
<hr />
<p><img src="images/bird.gif" alt="Птица" width="100" height="100" />
В мире насчитывается более 10 тысяч видов птиц, 
обитающих в различных экосистемах от Арктики до Антарктики. 
Многие виды ежегодно совершают перелеты на длинные расстояния, 
гораздо большее количество совершают более короткие спонтанные путешествия.</р>
<hr />
<p>В мире насчитывается более 10 тысяч видов птиц, 
обитающих в различных экосистемах от Арктики до Антарктики. 
<img src="images/bird.gif" alt="Птица" width="100" height="100" />
Многие виды ежегодно совершают перелеты на длинные расстояния, 
гораздо большее количество совершают более короткие спонтанные путешествия.</p>
```
</div></div>

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:10px;width:33%;" markdown>
## ПЕРЕД АБЗАЦЕМ
Абзац начинается с новой строки после изображения.
</div>
<div style="flex:1;margin-right:10px;width:33%;" markdown>
## В НАЧАЛЕ АБЗАЦА
Первая строка текста выравнивается относительно нижнего края изображения.
</div>
<div style="flex:1;width:33%;" markdown>
## В СЕРЕДИНЕ АБЗАЦА
Изображение помещается в текст абзаца, в котором говорится о нем.
</div></div>

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/placingex.png"></figure>

<div style="display:flex;margin-top:10px;" markdown>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
То, как вы размещаете изображение в коде, крайне важно, поскольку браузеры отображают HTML-элементы двумя следующими способами.
**Блочные элементы выводятся с новой строки.**

Примерами блочных элементов могут служить `<h1>` и `<р>`.
</div>
<div style="flex:1;margin-right:20px;width:33%;" markdown>
Если после элемента `<img>` следует блочный элемент (такой, как новый абзац), то он будет перенесен на новую строку после изображения, как показано в первом примере на этой странице.
</div>
<div style="flex:1;width:33%;" markdown>
**Встроенные элементы помещаются внутри блочного элемента и не начинают новую строку.**

Примерами таких элементов могут служить `<b>`, `<em>` и `<img>`.
</div></div>

Если элемент `<img>` находится внутри блочного элемента, то текст или другой встроенный элемент будет обтекать изображение, как показано во втором и третьем примере. 

Блочные и встроенные элементы более подробно обсуждаются в главе *Допополнительная разметка*.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/widthheight'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/figure'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
