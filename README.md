# Простой парсер данных с DDNet Master Servers и DDStats

Данный парсер упрощает получение данных с [мастера серверов дднета](https://master1.ddnet.org/ddnet/15/servers.json), а также предоставляет парсер [статистики игрока](https://ddstats.tw/)

## Установка библиотек:
```
pip install requests
```

Существуют 3 фабричные функции:

## GetServers(address=None)
*  Получает объект для парсинга информации о серверах

Пример:
```python
from ddnet_parser import GetServers

servers = GetServers()
print(servers.get_count())
```
## GetClients(address=None)
*  Получает объект для парсинга информации о клиентах
*  Args: address(bool, optional): адрес сервера, для которого нужно получить информацию о клиентах

Пример:
```python
from ddnet_parser import GetClients

servers = GetClients()
print(servers.get_())
```
 ## GetPlayerStats(name)
*  Получает объект для парсинга статистики игрока

Пример:
```python
from ddnet_parser import GetServers

servers = GetServers()
print(servers.get_count())
```

## Подробная документация с примерами:
*  Подробная документация: [🙂](docs/docs.md)

## Связь со мной
tg main: @neyxezz, tg twink: @neyxezz_twink
