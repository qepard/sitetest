# Иллюстрации и подписи

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:30%;" markdown>
## `<figure>`

Зачастую изображения сопровождаются подписями.

В спецификации **HTML5** есть элемент `<figure>`, объединяющий изображение и подпись к нему, таким образом текст и рисунок оказываются связанными друг с другом.

В один элемент `<figure>` можно включить несколько изображений, в случае если для них используется одна подпись.

</div>
<div style="flex:1;width:70%;" markdown>
``` html title="Код"
<figure>
    <img src="images/otters.jpg" 
        alt="Фотография двух выдр, держащихся за лапки">
        <img />
    <br />
        <figcaption>Во время сна выдры держат друг
        друга за лапки, чтобы их не разнесло
        течением.</figcaption>
</figure>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/figureex.png"></figure></div></div>

## `<figcaption>`

Элемент `<figcaption>` был включен в язык **HTML5**, чтобы позволить веб-дизайнерам добавлять подписи к публикуемым изображениям.

До введения этих двух элементов связать изображение `<img>` с текстом было невозможно.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/placing'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/media/images/example'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
