#  Кнопка подтверждения

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `type="submit"`
Кнопка подтверждения используется для отправки формы с данными на сервер.

## `name` 
Данному элементу формы может быть присвоен атрибут `name`, но его использование необязательно.

</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/podpiska.php">
    <p>Подпишитесь на рассылку наших новостей:</p>
    <input type="text" name="email" />
    <input type="submit" name="subscribe"
    value="Подписаться" />
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formconfirm.png"></figure></div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `value`
Атрибут `value` используется для указания текста надписи на кнопке.

</div>
<div style="flex:1;margin-top:80px;width:50%;" markdown>
В разных браузерах стили кнопок подтверждения могут отличаться, чаще всего соответствуя интерфейсу самого браузера.

</div></div>

Устанавливать текст надписи самостоятельно нужно потому, что по умолчанию в некоторых браузерах на кнопке пишется **Отправить** (Submit), что подходит не для всех форм.

Если вы хотите самостоятельно настроить стиль кнопки, вы можете воспользоваться средствами **CSS**, либо использовать графические кнопки.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/upload'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/grafic'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
