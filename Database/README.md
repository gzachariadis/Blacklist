<br>

<h1 align="center">Helpful SQLite3 Commands</h1>

<br>

<h2 align="center">Adlists Table</h2>

<br>

Select Adlists

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist"
```

Select Addresses by Domain Entries (number=0)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number=0"
```

Select Addresses by Domain Entries (number <= 100)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number<=100"
```

Select by Status (4 - Unavailable)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.status=4"
```

<h3 align="center">⚠️ <b>CAUTION DELETE</b> ⚠️</h3>

Delete Empty (exact domains = 0)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number=0"
```

Delete Small (less than 100 domains long)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number<100"
```

Delete by Status (Unavailabe Lists)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.status=4"
```

## Domains

### SELECT

Fetch Blacklist Regex

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM domainlist WHERE type=3"
```

