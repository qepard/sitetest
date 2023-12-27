# Переключатели

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" class="annotate" markdown>
## `type="radio"`
Переключатели позволяют посетителям сайта выбрать только один вариант из предложенных.

## `name`
Атрибут `name` отправляется серверу вместе со значением выбранного переключателя. Когда ответ на вопрос подразумевает выбор одного из нескольких вариантов, все переключатели, формирующие список ответов, должны иметь одинаковое значение атрибута `name`.
</div>

<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.primer.ru/profile.php">
    <p>Пожалуйста, выберите любимый жанр музыки: 
    <br />
        <input type="radio" name="genre" 
        value="rock" checked="checked" />Рок
        <input type="radio" name="genre" 
        value="pop" />Поп
        <input type="radio" name="genre" 
        value="techno" />Электроника
    </p>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formswitch.png"></figure>

<div style="display:flex;" markdown>
<div style="flex:1;width:50%;" markdown>
Если переключатель был установлен, сбросить его уже нельзя.

Единственное, что может сделать пользователь — выбрать другой вариант ответа.
</div>
<div style="flex:1;width:50%;" markdown>
Если ваш вопрос содержит один-единственный ответ и вы хотите предоставить посетителю возможность сбросить переключатель, вместо переключателей используйте флажки<br>(следующая страница).
</div></div></div></div>

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
## `value`
Атрибут `value` устанавливает значение выбранного переключателя, отправляемое серверу.

Значение каждого переключателя должно быть уникальным внутри группы (чтобы сервер знал, какой вариант ответа выбрал посетитель).
</div>
<div style="flex:1;width:50%;" class="annotate" markdown>
## `checked`
Атрибут `checked` указывает, какой из предлагаемых вариантов должен быть выбран по умолчанию при загрузке страницы (если это необходимо).

Атрибут принимает единственное значение - `checked`(1).

Данный атрибут должен быть установлен только у одного переключателя из группы.
</div>

1.  `Checked` (*англ.*) - установлен.
</div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/text'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/flags'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
