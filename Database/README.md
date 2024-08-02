
# Adlists

## SELECT

List Adlists

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist"
```

Get Address by Domain Entries (number=0)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number=0"
```

Get Address by Domain Entries (number < 100)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number<=100"
```

Fetch by Status - (4 - List Unavailable)

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.status=4"
```

Count Output Lines

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number<=100"  | wc -l
```

## DELETE

Delete Empty (exact domains = 0)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number=0"
```

Delete Small (less than 100 domains long)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number<100"
```

# Domains

# SELECT

Fetch Blacklist Regex

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT domain FROM domainlist WHERE type=3"
```

