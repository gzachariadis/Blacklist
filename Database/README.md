
## SELECT

Get Address by Domain entries

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number=0"
```

## DELETE

Delete Empty (exact domains = 0)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number=0"
```

Delete Small (less than 50 domains long)

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number<50"
```

