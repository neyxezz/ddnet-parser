# Класс ClientsParser

Пример использования:
```python
from ddnet_parser import GetClients

clients = GetClients()

online_players_list = clients.get_clients()
online_players_count = clients.get_clients(count=True)
print(onlint_players_count)
```
### Функции к объекту класса GetClients():
## update()
*   Описание: Обновляет данные, получая их из мастер-сервера.
*   Особенности: Данный атрибут может применяться к переменной, где определен объект класса
*   Аргументы: None
*   Возвращает: None
```python
from ddnet_parser import GetClients
import time

clients = GetClients()
print(clients.get_clients(count=True))
time.sleep(10)
clients.update()
print(clients.get_clients(count=True))
```
## get_raw_data(name)

*   Описание: Получает необработанные данные клиента по его имени.
*   Аргументы:
    *   name (str): Имя клиента
*   Особенности: Если адрес дан, возвращается клиент конкретно в этом адресе, в противном случае, первое вхождение.
*   Возвращает: dict или None: Возвращает словарь с данными клиента, если клиент найден, иначе None.
```python
clients = GetClients("ip:port")
print(clients.get_raw_data("nameless tee"))
```
## get_clients(count=False)

*   Описание: Получает список всех клиентов.
*   Особенности: Если адрес дан, возвращает все клиенты сервера, иначе все клиенты всех серверов
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество клиентов. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией о клиентах или количество клиентов, если count=True.
```python
clients = GetClients("ip:port")
print(clients.get_clients())
```
## get_players(count=False)

*   Описание: Получает список всех игроков (клиентов, помеченных как игроки в мастере).
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество игроков. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией об игроках или количество игроков, если count=True.
```python
clients = GetClients("ip:port")
print(clients.get_players())
```
## get_bots(count=False)

*   Описание: Получает список всех ботов (клиентов, не помеченных как игроки).
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество ботов. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией о ботах или количество ботов, если count=True.
*   Замечание: Я точно не знаю, боты это или нет, но в мастере серверов они помечаются как `is_player: False`
```python
clients = GetClients("ip:port")
print(clients.get_bots())
```
## get_afk_clients(count=False)

*   Описание: Получает список всех AFK клиентов.
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество AFK клиентов. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией об AFK клиентах или количество AFK клиентов, если count=True.
```python
clients = GetClients("ip:port")
print(clients.get_afk_clients())
```
## get_afk_players(count=False)

*   Описание: Получает список всех AFK игроков.
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество AFK игроков. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией об AFK игроках или количество AFK игроков, если count=True.
```python
clients = GetClients("ip:port")
print(clients.get_afk_players())
```
## get_afk_bots(count=False)

*   Описание: Получает список всех AFK ботов.
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество AFK ботов. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с информацией об AFK ботах или количество AFK ботов, если count=True.
```python
clients = GetClients("ip:port")
print(clients.get_afk_bots())
```
## get_clan(name)

*   Описание: Получает клан клиента по его имени.
*   Аргументы:
    *   name (str): Имя клиента.
*   Возвращает: str или None: Возвращает название клана клиента, если клиент найден, иначе None.
```python
clients = GetClients("ip:port")
print(clients.get_clan("nameless tee"))
```
## get_team(name)

*   Описание: Получает команду клиента по его имени.
*   Аргументы:
    *   name (str): Имя клиента.
*   Возвращает: str или None: Возвращает название команды клиента, если клиент найден, иначе None.
```python
clients = GetClients("ip:port")
print(clients.get_team("nameless tee))
```
## is_client_online(name)

*   Описание: Проверяет, находится ли клиент онлайн по его имени.
*   Аргументы:
    *   name (str): Имя клиента.
*   Возвращает: bool: Возвращает True, если клиент онлайн, иначе False.
```python
clients = GetClients("ip:port")
print(clients.is_client_online("nameless tee"))
```
## is_player_online(name)

*   Описание: Проверяет, находится ли игрок онлайн по его имени.
*   Аргументы:# Класс ClientsParser

Пример использования:
```python
from ddnet_parser import GetClients

clients = GetClients()

online_players_list = clients.get_clients()
online_players_count = clients.get_clients(count=True)
print(onlint_players_count)
```


# Класс ServersParser

Пример использования:
```python
from ddnet_parser import ServersParser

servers = ServersParser("ip:port")

server_name = servers.get_name()
print(server_name)
```
### Функции к объекту класса ServersParser():
## update()
*   Описание: Обновляет данные, получая их из мастер-сервера.
*   Особенности: Данный атрибут может применяться к переменной, где определен объект класса.
*   Аргументы: None
*   Возвращает: None
```python
from ddnet_parser import GetServers
import time

servers = GetServers()
print(servers.get_count())
time.sleep(10)
servers.update()
print(servers.get_count())
```
## get_raw_data()

*   Описание: Получает необработанные данные сервера или всех серверов.
*   Аргументы: None
*   Возвращает: dict или list: Возвращает словарь с данными сервера, если указан адрес, иначе - список словарей со всеми серверами.
```python
servers = GetServers()
print(servers.get_raw_data())
```
## get_count()

*   Описание: Получает общее количество серверов.
*   Аргументы: None
*   Возвращает: int: Возвращает общее количество серверов.
```python
servers = GetServers()
print(servers.get_count())
```
## get_passworded_servers(count=False)

*   Описание: Получает список серверов с паролем или их количество.
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество серверов с паролем. По умолчанию False.
*   Возвращает: list или int: Возвращает список словарей с данными о серверах с паролем или их количество, если count=True.
```python
servers = GetServers()
print(servers.get_passworded_servers())
print(servers.get_passworded_servers(count=True))
```
## get_location()

*   Описание: Получает локацию сервера.
*   Аргументы: None
*   Возвращает: str: Возвращает локацию сервера.
```python
servers = GetServers()
print(servers.get_location())
```
## get_max_clients()

*   Описание: Получает максимальное количество клиентов на сервере.
*   Аргументы: None
*   Возвращает: int: Возвращает максимальное количество клиентов.
```python
servers = GetServers()
print(servers.get_max_clients())
```
## get_max_players()

*   Описание: Получает максимальное количество игроков на сервере.
*   Аргументы: None
*   Возвращает: int: Возвращает максимальное количество игроков.
```python
servers = GetServers()
print(servers.get_max_players())
```
## get_game_type()

*   Описание: Получает тип игры на сервере.
*   Аргументы: None
*   Возвращает: str: Возвращает тип игры.
```python
servers = GetServers()
print(servers.get_game_type())
```
## get_name()

*   Описание: Получает название сервера.
*   Аргументы: None
*   Возвращает: str: Возвращает название сервера.
```python
servers = GetServers()
print(servers.get_name())
```
## get_map()

*   Описание: Получает название карты на сервере.
*   Аргументы: None
*   Возвращает: str: Возвращает название карты.
```python
servers = GetServers()
print(servers.get_map())
```
## get_version()

*   Описание: Получает версию сервера.
*   Аргументы: None
*   Возвращает: str: Возвращает версию сервера.
```python
servers = GetServers()
print(servers.get_version())
```
## is_require_login()

*   Описание: Проверяет, требуется ли логин на сервере.
*   Аргументы: None
*   Возвращает: bool: Возвращает True, если требуется логин, иначе False.
```python
servers = GetServers()
print(servers.is_require_login())
```
## is_passworded()

*   Описание: Проверяет, запаролен ли сервер.
*   Аргументы: None
*   Возвращает: bool: Возвращает True, если сервер запаролен, иначе False.
```python
servers = GetServers()
print(servers.is_passworded())
```


# Класс PlayerStatsParser

Пример использования:
```python
from ddnet_parser import GetPlayerStats

player_stats = GetPlayerStats("nameless tee")

total_seconds = player_stats.get_total_seconds_played()
print(total_seconds)
```
### Функции к объекту класса PlayerStatsParser():
## update()
*   Описание: Обновляет данные, получая их из API.
*   Особенности: Данный атрибут может применяться к переменной, где определен объект класса
*   Аргументы: None
*   Возвращает: None
```python
from ddnet_parser import GetPlayerStats
import time

player = GetPlayerStats("nameless tee")
print(player_stats.get_total_seconds_played())
time.sleep(60)
player.update()
print(player.get_total_seconds_played())
```
## get_raw_data()

*   Описание: Получает необработанные данные об игроке.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь с данными об игроке.
```python
player = GetPlayerStats("nameless tee")
print(player.get_raw_data())
```
## get_total_seconds_played()

*   Описание: Получает общее количество секунд, проведенных в игре.
*   Аргументы: None
*   Возвращает: int: Возвращает общее количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_total_seconds_played())
```
## get_start_of_playtime()

*   Описание: Получает дату начала игрового времени.
*   Аргументы: None
*   Возвращает: str: Возвращает дату начала игрового времени.
```python
player = GetPlayerStats("nameless tee")
print(player.get_start_of_playtime())
```
## get_average_seconds_played()

*   Описание: Получает среднее количество секунд, проведенных в игре.
*   Аргументы: None
*   Возвращает: int: Возвращает среднее количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_average_seconds_played())
```
## get_playtime()

*   Описание: Получает данные об игровом времени по месяцам.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь, где ключ - год и месяц, значение - количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_playtime())
```
## get_most_played_locations()

*   Описание: Получает данные о самых популярных локациях.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь, где ключ - локация, значение - количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_locations())
```
## get_most_played_categories()

*   Описание: Получает данные о самых популярных категориях.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь, где ключ - категория, значение - количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_categories())
```
## get_most_played_gametypes()

*   Описание: Получает данные о самых популярных типах игр.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь, где ключ - тип игры, значение - количество секунд.
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_gametypes())
```
## get_favourite_teammates()

*   Описание: Получает данные о любимых тиммейтах.
*   Аргументы: None
*   Возвращает: dict: Возвращает словарь, где ключ - имя тиммейта, значение - количество совместных игр.
```python
player = GetPlayerStats("nameless tee")
print(player.get_favourite_teammates())
```
## get_recent_finishes()

*   Описание: Получает данные о последних завершенных играх.
*   Аргументы: None
*   Возвращает: list: Возвращает список с данными о последних завершенных играх.
```python
player = GetPlayerStats("nameless tee")
print(player.get_recent_finishes())
```

