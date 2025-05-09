from ddnet_parser import GetPlayerStats

nick = "neyxezz"
player = GetPlayerStats(nick)
print("Начало игры — %s" % player.get_start_of_playtime())
print("Среднее время игры (в день) — %s часов" % str(round(player.get_total_seconds_played()/3600, 2)))
print("Наиграно — %s часов" % str(round(player.get_average_seconds_played()/3600, 2)))
print("Наиболее играемые типы игры:")
for gt in player.get_most_played_gametypes():
    print("- %s — %s часов" % (gt["key"], str(round(gt["seconds_played"]/3600, 2))))
print("Наиболее играемые категории:")
for ct in player.get_most_played_categories():
    print("- %s — %s часов" % (ct["key"], str(round(ct["seconds_played"]/3600, 2))))
print("Наиболее играемые локации:")
for lc in player.get_most_played_locations():
    print("- %s — %s часов" % (lc["key"], str(round(lc["seconds_played"]/3600, 2))))
print("Активность:")
for pl in player.get_playtime()[::-1]:
    print("- %s — %s часов" % (pl["year_month"], str(round(pl["seconds_played"]/3600, 2))))