# Ссылки на электронную почту

<div style="display:flex;" markdown>
<div style="flex:1;margin-right:10px;width:35%;" markdown>
## mailto:

Для создания ссылки, которая запускала бы программу электронной почты, установленную на компьютере посетителя, и позволяла бы отправить электронное письмо на указанный вами адрес, вам нужно будет воспользоваться элементом `<а>`.


</div><div style="flex:1;margin-right:10px;width:65%;" markdown>
``` html title="Код"
<a href="mailto:vasiliy@example.ru">Напишите Васе</a>
```

<figure><figcaption>Результат</figcaption><img src="/html-css-manual/assets/images/mailtoex.png"></figure></div></div>

Однако теперь значение атрибута `href` должно начинаться со слова `mailto:`, после которого необходимо указать адрес электронной почты, на который посетитель должен будет отправить свое письмо.

На рисунке сверху вы можете увидеть ссылку на электронную почту, которая выглядит как обычная ссылка.

Но при щелчке мышью по ней она запускает программу для отправки электронной почты и создает новое письмо, в адресной строке которого будет введен адрес, указанный вами при создании ссылки.

<div style="display: flex; justify-content: space-between; padding: 20px; margin-top:30px;"><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/structure'"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M15 18l-6-6 6-6" /></svg><span style="margin: 0 10px;">Предыдущая страница</span></button><button class="custom-button" style="background-color: rgb(0, 148, 133); color: white; font-family: 'Roboto', sans-serif; border: none; cursor: pointer; padding: 10px 20px; font-size: 16px; display: flex; align-items: center;" onclick="window.location.href='/html-css-manual/html/link/target'"><span style="margin: 0 10px;">Следующая страница</span><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="fill: white; width: 20px; height: 20px;"><path d="M9 18l6-6-6-6" /></svg></button></div>
