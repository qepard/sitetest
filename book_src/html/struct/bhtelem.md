# Элементы BODY, HEAD и TITLE

## Код

<div style="overflow:auto" markdown>
<div style="float:left;margin-right:10px;">
``` html title="Код примера"
<html>
    <head>
        <title>Это заголовок страницы</title>
    </head>
    <body>
        <h1>Это "тело" страницы</h1>
        <p>Содержимое, помещенное в тело страницы,
            будет отображено в основном окне браузера.
        </p>
    </body>
</html>
```
</div>

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/browserbht.png" width="228" height="160"/><figcaption style="margin-top:-5px"><sub>на картинку можно нажать,<br>чтобы увеличить её</sub></figcaption><figure></div>

## &lt;body&gt;

С тегом `<body>` вы уже встречались в первом примере. Все, помещамое внутрь этого элемента, отображается в основном окне браузера.

## &lt;title&gt;

Содержимое элемента `<title>` выводится либо в заголовке окна браузера (выше текстового поля, в которое вы обычно вводите адрес сайта), либо в качестве названия вкладки страницы (если ваш браузер использует вкладки).

## &lt;head&gt;

Вам часто придется видеть элемент `<head>`, предшествующий элементу `<body>`. Он содержит информацию о *самой* странице, а не ту, которая будет выведена в основную часть окна браузера (выделенную голубым цветом на фото ниже). В элемент `<head>` всегда включается элемент `<title>`.(1)
{ .annotate }

1.  Он всегда есть, но он необязателен.(1)
{ .annotate }

    1.  Ведь у вкладки всегда есть название, верно?    

<hr><div style="text-align:center"><img src="/html-css-manual/assets/images/browserbhtHL.png"/></div>

<center><span style="color:#CE6E2C;">Оранжевым</span> выделен элемент `<title>`<br><span style="color:#5151F2;">Синим</span> — `<body>`


<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/struct/htmlex/meaning/'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/text/'"><span style="margin: 0 10px;">Следующая глава</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
