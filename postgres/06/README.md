# 많은 데이터셋에서 테스트

1. GROUP BY recap!

```sql
select
    paid,
    count(*)
from orders
group by paid
```

이러면 T/F에 대해서만 따로 쿼리가 가능하다.

2. INNER JOIN recap!

```sql
select
    first_name,
    last_name,
    paid
from
    users
    join orders on orders.user_id = users.id

```
