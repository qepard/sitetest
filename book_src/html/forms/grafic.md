# Графическая кнопка

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="image"`
Если вы хотите использовать собственное изображение для кнопки подтверждения, то вам потребуется присвоить атрибуту `type` значение `image`.

При этом атрибуты `src, width, height` и `alt` будут работать точно так же, как и для элемента `<img>`.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.example.com.com/subscribe.php">
    <p>Подпишитесь на рассылку наших новостей</p>
    <input type="text" name="email" />
    <input type="image" src="images/subscribe.jpg"
    width="100" height="20">
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formgrafic.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/confirm'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/hidden'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
