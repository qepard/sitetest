# Ввод URL-адреса и адреса электронной почты

В спецификации **HTML5** также появились специальные элементы формы, позволяющие посетителям сайта вводить адреса электронной почты и URL.

Браузеры, не поддерживающие эти элементы формы, отобразят их как обычные однострочные поля ввода текста.

<div style="display:flex;margin-top:20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="email"`

Для запроса адреса электронной почты вы можете воспользоваться специализированным полем ввода. Браузеры, поддерживающие язык **HTML5**, проверят, соответствует ли введенный посетителем адрес принятому стандарту для данного типа адресов. Экранная клавиатура некоторых смартфонов также будет оптимизирована для отображения символов, наиболее часто встречающихся в адресах электронной почты (например, символа @).

## `type="url"`

Поле ввода URL-адресов может быть использовано для запроса ввода адреса какой-либо страницы во Всемирной паутине. Браузеры, поддерживающие валидацию данных **HTML5**, удостоверятся в том, что введенный текст соответствует стандарту для URL-адресов, прежде чем отправить форму на сервер. Экранная клавиатура некоторых смартфонов также будет оптимизирована для отображения символов, наиболее часто встречающихся в URL-адресах.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.example.com/profile.php" 
method="post">
    <p>
    Пожалуйста введите адрес электронной почты:
    </p>
    <input type="email" name="email" />
    <input type="submit" value="Отправить">
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formmail.png"></figure>

``` html title="Код"
<form action="https://www.example.com/profile.php" 
method="post">
    <p>Пожалуйста введите адрес вашего сайта:</p>
    <input type="url" name="sait" />
    <input type="submit" value="Отправить">
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formurl.png"></figure></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/validation'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/search'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>


