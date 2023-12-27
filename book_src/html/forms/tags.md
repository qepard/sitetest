# Метки элементов формы

<div style="display:flex;margin-top:-20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
## `<label>`
При рассказе об элементах формы мы намеренно упрощали код, поясняя назначение каждого элемента формы с помощью помещаемого рядом текста.

Однако у каждого элемента формы должна быть своя надпись, или метка, создаваемая при помощи элемента `<label>` и упрощающая пользование сайтом людям с нарушениями зрения.

Элемент `<label>` можно использовать двумя способами.

Окружить им и метку и сам элемент формы, как показано справа на примере поля ввода текста.

Указать отдельно от элемента формы, но при этом использовать атрибут `for` для соотнесения с нужным элементом, как показано на примере переключателей.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<label>
    Возраст: <input type="text" name="age" />
</label>
<br />
Пол:
<input id="female" type="radio" 
name="gender" value="f">
<label for="female">Женский</label>
<input id="male" type="radio" 
name="gender" value="m">
<label for="male">Мужской</label>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formtags.png"></figure>

## `for`
Данный атрибут устанавливает связь между `<label>` и элементом формы.

Обратите внимание, что для группы переключателей указан атрибут `id`.
</div></div>


<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/hidden'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/group'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
