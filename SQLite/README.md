
Addresses of all adlists with an exactly 0 domains

```sh
sqlite3 "/etc/pihole/gravity.db" "SELECT address FROM adlist WHERE adlist.number=0"
```

Empty

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number=0"
```

Small

```sh
sqlite3 "/etc/pihole/gravity.db" "DELETE FROM adlist WHERE adlist.number<50"
```

