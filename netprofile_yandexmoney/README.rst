About this module
=================

После инсталляции модуля необходимо:
- Активировать модуль: `npctl module enable yandexmoney` или Управление -> Ядро -> Модули
- Активировать модуль и настроить авторизацию: Управление -> Внешние операторы -> Провайдеры -> Yandex.Money
- Настроить "секретное слово", выдаваемое сервисом Яндекс.Деньги, для верификации: Управление -> Ядро -> Настройки -> Общие настройки -> ym_sharedsecret
- Перезапустить vhost 'xop'


Деньги: https://tech.yandex.ru/money/doc/dg/reference/notification-p2p-incoming-docpage/
Касса/магазин: https://money.yandex.ru/doc.xml?id=526537 - больше не так, теперь все лежит по другому адресу - 
https://tech.yandex.ru/money/doc/payment-solution/About-docpage/ 
https://tech.yandex.ru/money/doc/payment-solution/examples/examples-test-data-docpage/
https://tech.yandex.ru/money/doc/payment-solution/payment-form/payment-form-http-docpage/
https://tech.yandex.ru/money/doc/payment-solution/examples/examples-about-docpage/

что и как надо делать?
1. в ЛК вводим сумму, нажимаем оплатить черех YM
2. редирект на YM для проведения платежа
3. выбор способа платежа и пр пр пр
3.5 Перед тем, как пользователь увидит страницу подтверждения платежа, 
    Яндекс.Деньги отправляют запрос Проверка заказа (checkOrder) по адресу, 
    который указан в технической анкете.
4. подтверждение оплаты на YM
5. редирект обратно в ЛК
6. проверка статуса платежа в ЛК
7. при успешном платеже зачисление средств на счет ЛК

-> ждем тестовых параметров, см. email
   надо добавить обработчик post-запросов от yandex.money, который будет обрабатывать статус платежа и вносить данные в базу и пр
