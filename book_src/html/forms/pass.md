# Ввод пароля

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="password"`
Когда атрибуту `type` присваивается значение `password`, на странице создается однострочное поле ввода текста, которое функционирует как обычное поле ввода текста с той лишь разницей, что вводимые в него символы маскируются.

Это сделано, чтобы не допустить утечки таких важных данных, как пароль, в случае, если кто-то подглядывает из-за спины посетителя сайта.
## `name`
Атрибут `name` устанавливает имя поля ввода пароля, отправляемое на сервер вместе с паролем, введенным пользователем.

## `size`, `maxlength`
Аналогично однострочному полю ввода текста, для поля ввода пароля также можно указать атрибуты `size` и `maxlength`.
</div>
<div style="flex:1;margin-right:20px;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/login.php">
    <p>Имя пользователя:
        <input type="text" name="username" 
        size="15" maxlength="30" />
    </p>
    <p>Пароль:
        <input type="password" name="password" 
        size="15" maxlength="30" />
    </p>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formpass.png"></figure>

<div style="display:flex;" markdown>
<div style="flex:1;width:40%;" markdown>
Несмотря на то, что вводимый пароль скрыт от чужих глаз на экране, это вовсе не означает, что он будет безопасно передан на сервер.

Никогда не используйте данный элемент формы для отправки таких конфиденциальных данных, как номера банковских карт.
</div>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
Для обеспечения полной безопасности сервер должен быть настроен таким образом, чтобы обмениваться данными с пользовательскими компьютерами по криптографическому протоколу *SSL*(1).

Обсуждение протокола *SSL* выходит за рамки этой книги.
</div>

1.  Secure Sockets Layer(*англ.*) — Уровень защищенных сокетов.
</div></div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/input'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/text'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
