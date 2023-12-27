# Валидация данных формы

Возможно, вы встречали во Всемирной паутине формы, выводящие предупреждения в случае, если не все поля были правильно заполнены.

Эта реакция называется **валидацией данных формы**.

Традиционно валидация введенных данных осуществляется с помощью специальных сценариев *JavaScript*.

<div style="display:flex;margin-top:20px;" markdown>
<div style="flex:1;margin-right:20px;width:40%;" markdown>
В языке **HTML5** появилась собственная технология валидации введенных данных: теперь эта работа перекладывается на веб-браузер.

Валидация позволяет гарантировать, что пользователь введет данные в формате, с которым сможет работать сервер.

Она позволяет:

* уменьшить количество операций, выполняемых сервером
* увидеть пользователям ошибки в заполнении формы быстрее, чем если бы подобная проверка осуществлялась на сервере.
</div>
<div style="flex:1;width:60%;" markdown>
``` html title="Код"
<form action="https://www.example.com/login/" 
method="post">
    <label for="username">
    Имя пользователя:
    </label>
    <input type="text" name="username" 
    required="required" /><br />
    <label for="password">Пароль:</label>
    <input type="password" name="pass" 
    required="required" />
    <input type="submit" value="Отправить"/>
</form>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/formvalid.png"></figure>
<div style="display:flex;margin-top:20px;" markdown>
<div style="flex:1;margin-right:20px;width:50%;" markdown>
Для поддержки совместимости со старыми версиями браузеров (не поддерживающими **HTML5**) большинство разработчиков продолжают использовать сценарии *JavaScript*.
</div>
<div style="flex:1;width:50%;" class="annotate" markdown>
Примером встроенной системы проверки введенных данных **HTML5** может служить атрибут `required`(1), используемый с любым элементом формы, принимающим пользовательский ввод. 
</div>

1.  `Required`(*англ.*) — обязательный.
</div>
Данному атрибуту **HTML5** не нужно значение, однако в *HTML4* всем атрибутам должно быть присвоено значение, поэтому веб-дизайнеры используют значение `required`.
</div></div>

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/date'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/forms/urlmail'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
