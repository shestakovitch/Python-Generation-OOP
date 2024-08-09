"""Класс OrderStatus
Реализуйте класс OrderStatus, описывающий флаг с состояниями интернет-заказов. Флаг должен иметь три элемента:

ORDER_PLACED
PAYMENT_RECEIVED
SHIPPING_COMPLETE
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс
используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса OrderStatus нет, она может быть произвольной."""


from enum import Flag


class OrderStatus(Flag):
    ORDER_PLACED = 1
    PAYMENT_RECEIVED = 2
    SHIPPING_COMPLETE = 4


# Sample
# Input:
#
# order_status = OrderStatus(0)
# order_status |= OrderStatus.ORDER_PLACED
#
# if OrderStatus.ORDER_PLACED in order_status:
#     print('Заказ оформлен!')
#
# order_status |= OrderStatus.PAYMENT_RECEIVED
#
# if OrderStatus.PAYMENT_RECEIVED in order_status:
#     print('Оплата получена!')
#
# order_status |= OrderStatus.SHIPPING_COMPLETE
#
# if OrderStatus.SHIPPING_COMPLETE in order_status:
#     print('Доставка завершена!')
# Sample
# Output:
#
# Заказ
# оформлен!
# Оплата
# получена!
# Доставка
# завершена!