## Навигация:
- [GetClients](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#%D0%BA%D0%BB%D0%B0%D1%81%D1%81-clientsparser)
- [GetServers](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#%D0%BA%D0%BB%D0%B0%D1%81%D1%81-serversparser)
- [GetPlayerStats](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#%D0%BA%D0%BB%D0%B0%D1%81%D1%81-playerstatsparser)
- [GetMap](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#%D0%BA%D0%BB%D0%B0%D1%81%D1%81-mapsparser)
- [GetProfile](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#%D0%BA%D0%BB%D0%B0%D1%81%D1%81-profileparser)

## Обновление данных с помощью update()
Для каждого объекта класса можно использовать функцию `update()`, которая обновляет данные

Пример:
```python
from ddnet_parser import GetClients
import time

clients = GetClients()
print(clients.get_clients(count=True))
time.sleep(10)
clients.update()
print(clients.get_clients(count=True))
```

# Класс ClientsParser
Пример использования:
```python
from ddnet_parser import GetClients

clients = GetClients()
print(clients.get_clients(count=True))
```
### Функции к объекту GetClients() класса ClientsParser:
## get_raw_data(name)

*   Описание: Получает необработанные данные клиента по его имени
*   Аргументы:
    *   name (str): Имя клиента
*   Особенности: Если адрес дан, возвращается клиент конкретно в этом адресе, в противном случае, первое вхождение
*   Возвращает: dict или None: словарь с данными клиента, если клиент найден, иначе None
```python
clients = GetClients("ip:port")
print(clients.get_raw_data("nameless tee"))
```
## get_clients(count=False, types="client")

*   Описание: Получает список всех клиентов по заданному типу.
*   Особенности: Если адрес дан в функции GetClients, возвращает все клиенты сервера, иначе все клиенты всех серверов. Основные типы клиентов для переменной types:
    - client (все клиенты);
    - player (обычные игроки);
    - spectators (наблюдатели)
Учтите, что подключающиеся клиенты тоже являются спектаторами и помечаются ником `(connecting)`
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество клиентов. По умолчанию False
    *   types (str, optional): Тип клиента
*   Возвращает: list или int: список словарей с информацией о клиентах или количество клиентов, если count=True
```python
clients = GetClients("ip:port")
print(clients.get_clients(types="spectator"))
```
## get_afk_clients(count=False, types="client")

*   Описание: Получает список всех AFK клиентов
*   Особенности: Если адрес дан в функции GetClients, возвращает все клиенты сервера, иначе все клиенты всех серверов. Основные типы клиентов для переменной types:
    - client (все клиенты);
    - player (обычные игроки);
    - spectators (наблюдатели)
Учтите, что подключающиеся клиенты тоже являются спектаторами и помечаются ником `(connecting)`
*   Аргументы:
    *   count (bool, optional): Если True, возвращает количество AFK клиентов. По умолчанию False
*   Возвращает: list или int: список словарей с информацией об AFK клиентах или количество AFK клиентов, если count=True
```python
clients = GetClients("ip:port")
print(clients.get_afk_clients(types="spectator"))
```
## get_clan(name)

*   Описание: Получает клан клиента по его имени
*   Аргументы:
    *   name (str): Имя клиента
*   Возвращает: str или None: название клана клиента, если клиент найден, иначе None
```python
clients = GetClients("ip:port")
print(clients.get_clan("nameless tee"))
```
## get_team(name)

*   Описание: Получает команду клиента по его имени
*   Аргументы:
    *   name (str): Имя клиента
*   Возвращает: str или None: название команды клиента, если клиент найден, иначе None
```python
clients = GetClients("ip:port")
print(clients.get_team("nameless tee"))
```
## get_score(name)

*   Описание: Получает очки клиента по его имени
*   Аргументы:
    *   name (str): Имя клиента
*   Возвращает: str или None: название команды клиента, если клиент найден, иначе None
```python
clients = GetClients("ip:port")
print(clients.get_team("nameless tee"))
```
## is_online(name, types="client")

*   Описание: Проверяет, находится ли клиент онлайн по его имени
*   Особенности: Если адрес дан в функции GetClients, возвращает все клиенты сервера, иначе все клиенты всех серверов. Основные типы клиентов для переменной types:
    - client (все клиенты);
    - player (обычные игроки);
    - spectators (наблюдатели)
Учтите, что подключающиеся клиенты тоже являются спектаторами и помечаются ником `(connecting)`
*   Аргументы:
    *   name (str): Имя клиента
*   Возвращает: bool: True, если клиент онлайн, иначе False
```python
clients = GetClients("ip:port")
print(clients.is_online("nameless tee", types="spectator"))
```
## get_clients_with_same_clan(clan)

*   Описание: Получает список клиентов с заданным кланом
*   Аргументы: str: клан

Пример использования:
```python
from ddnet_parser import GetClients

clients = GetClients()
print(clients.get_clients_with_same_clan("clan"))
```

# Класс ServersParser

Пример использования:
```python
from ddnet_parser import GetServers

servers = GetServers("ip:port")

server_name = servers.get_name()
print(server_name)
```
### Функции к объекту GetServers() класса ServersParser:
## get_raw_data()

*   Описание: Получает необработанные данные сервера или всех серверов
*   Особенности: Если адрес дан, возвращает данные по этому адресу, иначе данные всех серверов
*   Аргументы: None
*   Возвращает: dict или list: словарь с данными сервера, если указан адрес, иначе список словарей со всеми серверами
```python
servers = GetServers()
print(servers.get_raw_data())
```
## get_count()

*   Описание: Получает общее количество серверов.
*   Аргументы: None
*   Возвращает: int: общее количество серверов.
```python
servers = GetServers()
print(servers.get_count())
```
## get_passworded_servers(count=False)

*   Описание: Получает список серверов требующие пароль
*   Аргументы: count (bool, optional): Если True, возвращает количество серверов с паролем. По умолчанию False
*   Возвращает: list или int: список словарей с данными о серверах с паролем или их количество, если count=True
```python
servers = GetServers()
print(servers.get_passworded_servers())
print(servers.get_passworded_servers(count=True))
```
## get_require_login_servers(count=False)

*   Описание: Получает список серверов требующих логин
*   Аргументы: count (bool, optional): Если True, возвращает количество серверов с паролем. По умолчанию False
*   Возвращает: list или int: список словарей с данными о серверах с паролем или их количество, если count=True
```python
servers = GetServers()
print(servers.get_require_login_servers())
```
## get_location()

*   Описание: Получает расположение сервера
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: локация сервера
```python
servers = GetServers()
print(servers.get_location())
```
## get_max_clients()

*   Описание: Получает максимальное количество клиентов на сервере
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: int: максимальное количество клиентов
```python
servers = GetServers()
print(servers.get_max_clients())
```
## get_max_players()

*   Описание: Получает максимальное количество игроков на сервере
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: int: максимальное количество игроков
```python
servers = GetServers()
print(servers.get_max_players())
```
## get_game_type()

*   Описание: Получает тип игры на сервере
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: тип игры
```python
servers = GetServers()
print(servers.get_game_type())
```
## get_name()

*   Описание: Получает название сервера
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: название сервера
```python
servers = GetServers()
print(servers.get_name())
```
## get_map_name()

*   Описание: Получает название карты
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: название карты
```python
servers = GetServers()
print(servers.get_map_name())
```
## get_map_hash()

*   Описание: Получает SHA256 карты
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: SHA256
```python
servers = GetServers()
print(servers.get_map_hash())
```
## get_map_size()

*   Описание: Получает размер карты в байтах
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: размер карты
```python
servers = GetServers()
print(servers.get_map_size())
```
## get_version()

*   Описание: Получает версию сервера
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: str: версия сервера
```python
servers = GetServers()
print(servers.get_version())
```
## is_require_login()

*   Описание: Проверяет, требуется ли логин на сервере
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: bool: True, если требуется логин, иначе False
```python
servers = GetServers()
print(servers.is_require_login())
```
## is_passworded()

*   Описание: Проверяет, запаролен ли сервер
*   Особенность: Данная функция работает только тогда, когда адрес был определен в GetServers
*   Аргументы: None
*   Возвращает: bool: True, если сервер запаролен, иначе False
```python
servers = GetServers()
print(servers.is_passworded())
```
## get_server_by_client_name(name, all_servers=False)

*   Описание: Получает сервер по нику клиента
*   Аргументы: name (str): Ник клиента; all_servers (bool, optional): Если True, берутся все сервера с заданным ником клиента, иначе первое вхождение
*   Возвращает: list: сервер/серверы
```python
server = GetServers()
print(server.get_server_by_client_name("nameless tee", all_servers=True))
```
## get_servers_by_game_type(game_type, count=False)

*   Описание: Получает сервера с заданным типом игры
*   Аргументы: game_type (str): Тип игры
*   Возвращает: list: сервер/серверы
```python
server = GetServers()
print(server.get_servers_by_game_type("DDRaceNetwork"))
```

# Класс PlayerStatsParser

Пример использования:
```python
from ddnet_parser import GetPlayerStats

player_stats = GetPlayerStats("nameless tee")

total_seconds = player_stats.get_total_seconds_played()
print(total_seconds)
```
Важное замечание: не всегда вся статистика отслеживается сайтом ddstats.tw, особенно если у вас очень много данных. Так, например, для ника **nameless tee** в функциях `get_total_seconds_played`, `get_start_of_playtime`, `get_average_seconds_played`, `get_playtime` возвращается None или пустой список, всегда учитывайте это.
### Функции к объекту GetPlayerStats() класса PlayerStatsParser:
## get_raw_data()

*   Описание: Получает необработанные данные об игроке
*   Аргументы: None
*   Возвращает: dict: словарь с данными об игроке
```python
player = GetPlayerStats("nameless tee")
print(player.get_raw_data())
```
## get_total_seconds_played()

*   Описание: Получает общее количество секунд, проведенных в игре
*   Аргументы: None
*   Возвращает: int: общее количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_total_seconds_played())
```
## get_start_of_playtime()

*   Описание: Получает дату первого появления в игре
*   Аргументы: None
*   Возвращает: str: Возвращает дату начала игрового времени
```python
player = GetPlayerStats("nameless tee")
print(player.get_start_of_playtime())
```
## get_average_seconds_played()

*   Описание: Получает среднее количество секунд, проведенных в игре за день
*   Аргументы: None
*   Возвращает: int: среднее количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_average_seconds_played())
```
## get_playtime()

*   Описание: Получает данные об игровом времени по месяцам
*   Аргументы: None
*   Возвращает: dict: словарь, где ключ - год и месяц, значение - количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_playtime())
```
## get_most_played_locations()

*   Описание: Получает данные о наиболее часто играемых локациях серверов
*   Аргументы: None
*   Возвращает: dict: словарь, где ключ - локация, значение - количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_locations())
```
## get_most_played_categories()

*   Описание: Получает данные о наиболее часто играемых категориях карт
*   Аргументы: None
*   Возвращает: dict: словарь, где ключ - категория, значение - количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_categories())
```
## get_most_played_gametypes()

*   Описание: Получает данные о наиболее часто играемых типах игры
*   Аргументы: None
*   Возвращает: dict: словарь, где ключ - тип игры, значение - количество секунд
```python
player = GetPlayerStats("nameless tee")
print(player.get_most_played_gametypes())
```
## get_favourite_teammates()

*   Описание: Получает данные о тиммейтах, с которыми вместе забрали ранг на карте
*   Аргументы: None
*   Возвращает: dict: словарь, где ключ - имя тиммейта, значение - количество совместных игр
```python
player = GetPlayerStats("nameless tee")
print(player.get_favourite_teammates())
```
## get_recent_finishes()

*   Описание: Получает данные о последних завершенных мапах
*   Аргументы: None
*   Возвращает: list: список с данными о последних завершенных играх
```python
player = GetPlayerStats("nameless tee")
print(player.get_recent_finishes())
```

# Класс MapsParser

Пример использования:
```python
from ddnet_parser import GetMap

map = GetMap("Linear")
print(map.get_mapper())
```

### Функции к объекту GetMap() класса MapsParser:
## get_raw_data()

*   Описание: Получает необработанные данные об игроке
*   Аргументы: None
*   Возвращает: dict: словарь с данными об игроке
```python
map = GetMap("Linear")
print(player.get_raw_data())
```
## get_finishes()

*   Описание: Получает количество финишей карты
*   Аргументы: None
*   Возвращает: int: число финишей карты
```python
map = GetMap("Linear")
print(player.get_finishes())
```
## get_create_time()

*   Описание: Получает дату релиза карты
*   Аргументы: None
*   Возвращает: str: дата релиза карты
```python
map = GetMap("Linear")
print(player.get_create_time())
```
## get_type()

*   Описание: Получает тип сервера — `Novice`, `Moderate`, `Brutal`, `Insane`...
*   Аргументы: None
*   Возвращает: str: тип сервера
```python
map = GetMap("Linear")
print(player.get_type())
```
## get_points()

*   Описание: Получает количество получаемых очков при прохождении карты
*   Возвращает: int: количество очков
```python
map = GetMap("Linear")
print(player.get_points())
```
## get_stars()

*   Описание: Получает количество звезд карты
*   Аргументы: None
*   Возвращает: int: количество звезд
```python
map = GetMap("Linear")
print(player.get_stars())
```
## get_mapper()

*   Описание: Получает создателя карты
*   Аргументы: None
*   Возвращает: str: создатель карты
```python
map = GetMap("Linear")
print(player.get_mapper())
```
## get_median_time()

*   Описание: Получает среднее время рейса до финиша
*   Аргументы: None
*   Возвращает: int: среднее время финиша
```python
map = GetMap("Linear")
print(player.get_median_time())
```
## get_playtime()

*   Описание: Получает топ по наигранным секундам
*   Аргументы: None
*   Возвращает: list: список с топом наигранных секунд на карте
```python
map = GetMap("Linear")
print(player.get_playtime())
```

# Класс ProfileParser

Пример использования:
```python
from ddnet_parser import GetProfile

profile = GetProfile("neyxezz")
print(profile.get_skin_color_body())
```

### Функции к объекту GetProfile() класса ProfileParser:
## get_raw_data()

*   Описание: Получает необработанные данные о профиле игрока
*   Аргументы: None
*   Возвращает: dict: словарь с профилем игрока
```python
profile = GetProfile("neyxezz")
print(profile.get_raw_data())
```
## get_points()

*   Описание: Получает общее количество очков
*   Аргументы: None
*   Возвращает: int: количество очков
```python
profile = GetProfile("neyxezz")
print(profile.get_points())
```
## get_country()

*   Описание: Получает код страны
*   Аргументы: None
*   Возвращает: int: код страны
```python
profile = GetProfile("neyxezz")
print(profile.get_country())
```
## get_skin_name()

*   Описание: Получает название скина
*   Аргументы: None
*   Возвращает: str: название скина
```python
profile = GetProfile("neyxezz")
print(profile.get_skin_name())
```
## get_skin_color_body()

*   Описание: Получает код цвета тела в десятичном представлении
*   Аргументы: None
*   Возвращает: int: код цвета
```python
profile = GetProfile("neyxezz")
print(profile.get_skin_color_body())
```
## get_skin_color_feet()

*   Описание: Получает код цвета ног в десятичном представлении
*   Аргументы: None
*   Возвращает: int: код цвета
```python
profile = GetProfile("neyxezz")
print(profile.get_skin_color_feet())
```