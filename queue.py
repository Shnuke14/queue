## Пример релизации очереди
import collections

q = collections.deque()

## Вывод пустой очереди
print(q)

## Добавление новых элементов в очередь
q.append(2)
q.append(5)
q.append(-7)

## Вывод первого элемента
print(q.popleft())
## Удаление первого элемента
q.popleft()

## Вывод очереди
print(q)