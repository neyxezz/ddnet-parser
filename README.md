# Простой парсер данных с DDNet Master Servers и DDStats

Данный парсер упрощает получение данных с [мастера серверов дднета](https://master1.ddnet.org/ddnet/15/servers.json), а также предоставляет парсер [статистики игрока](https://ddstats.tw/)

## Установка библиотек:
```
pip install requests
```
## Установка парсера:
```
git clone https://github.com/neyxezz/ddnet-parser.git ddnet_parser
```
Важно понимать, что у меня пока что нет возможности выложить данный модуль на pypi (у меня не получилось), поэтому помещайте вручную эту папку в директорию выполнения вашего скрипта, либо можно сделать так:

```python
import sys
sys.path.append("ВАША_ДИРЕКТОРИЯ_ГДЕ_НАХОДИТСЯ_ПАПКА")
```
Теперь, вы сможете в полной мере пользоваться данной библиотекой.

## GetServers(address=None)
*  Получает объект для парсинга информации о серверах
*  Args: address(bool, optional): адрес сервера, для которого нужно получить информацию

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

clients = GetClients()
print(clients.get_clients(count=True))
```
## GetPlayerStats(name)
*  Получает объект для парсинга статистики игрока
*  Args: name(str): ник, для которого нужно получить статистику

Пример:
```python
from ddnet_parser import GetPlayerStats

player = GetPlayerStats("neyxezz")
print(player.get_total_seconds_played())
```

## GetMap(_map)
* Получает объект для парсинга данных карты
*  Args: address(str): карта, для которой нужно получить данные

Пример:
```python
from ddnet_parser import GetMap

map = GetMap("Linear")
print(map.get_mapper())
```

## Подробная документация с примерами:
*  Подробная документация: [🙂](docs/docs.md)
*  Примеры: [🙂](examples/examples.py)

## Связь со мной
tg main: @neyxezz, tg twink: @neyxezz_twink
