# 해시 명령이 때로는 의도치않은 결과를 리턴한다?

## `HGETALL`, `HSET`에 대하여

커맨드로 날렸을 때와 어떻게 결과물이 다른지 살펴보는 시간.

```typescript
await client.hSet("car", {
  color: "red",
  year: 1950,
  engine: { cylinders: 8 },
  owner: null,
  service: undefined,
});
```

이런 값을 넣는다고 생각해보자.

원래라면 `.toString()` 을 호출해서 문자열을 담을 수가 있지만, 객체인 `{ cylinders: 8}`은 아예 `[object Object]` 가 들어갔고, `null` 은 `.toString()` 의 결과가 없으니 에러가 난다.

ORM으로 DB에 `NULL`값을 넣거나 할 때, 파이썬이라면 `None` 을 넣어주는 식으로 처리가 가능했다. 그렇지만 레디스 관련은 그런 식으로 언어 자체의 요소를 바로 활용할 수가 없다. 값이 없는데 키를 남기고 싶거나 한다면, `""` 같은 식으로 처리를 해야한다.

## 존재하지 않는 키에 접근한다면?

- 예상
  - `None` 을 주지 않을까요?
- 결과
  - 아니었습니다! `{}` 값을 줌(!!)

자바스크립트에서...

```typescript
if (!car) {
  console.log("[404] car not found");
  return;
}
```

이런 식으로 접근하면 안됨. `{}` 값이 리턴되니까, `null` 이 아니기 때문!

아예 이렇게 해야함...

```typescript
if (Object.keys(car).length === 0) {
  console.log("[404] car not found");
  return;
}
```

## 이렇기 때문에...

실제로 어떤 결과가 리턴되는지 정확히 알아야 버그가 없다!
