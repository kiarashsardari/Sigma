# Sigma.py

محاسبهٔ سیگما (جمع) یک تابع دلخواه روی بازه‌ای از اعداد صحیح.

## توابع

### `sigma(i, n, f)`

جمع `f(x)` را برای `x` از `i` تا `n` (شامل هر دو) حساب می‌کند.  
اگر `i > n` باشد، مقدار `0` برمی‌گرداند (جمع خالی).

```python
def sigma(i, n, f):
    total = 0
    while n >= i:
        total += f(i)
        i += 1
    return total
```

### `run(start, end, f)`

ابتدا بررسی می‌کند که `start` و `end` عدد صحیح باشند، سپس `sigma` را صدا می‌زند.  
در صورت غیرصحیح بودن، پیام خطا برمی‌گرداند.

```python
def run(start, end, f):
    if type(start) is int and type(end) is int:
        return sigma(start, end, f)
    else:
        return 'start and end must be integers and start <= end'
```

## مثال

```python
from Sigma import run

result = run(1, 3, lambda x: 2 * x + 1)
print(result)  # 15
```

محاسبه:

```
(2*1+1) + (2*2+1) + (2*3+1) = 3 + 5 + 7 = 15
```

## نکات

- برای اعداد صحیح طراحی شده است.
- اگر `start > end` باشد، مقدار `0` برگردانده می‌شود.
- در صورت غیرصحیح بودن `start` یا `end`، پیام خطا برگردانده می‌شود.
- `bool` به‌عنوان عدد صحیح پذیرفته نمی‌شود (چون از `type(...) is int` استفاده شده).

## نصب

فایل `Sigma.py` را در پروژهٔ خود کپی کنید و از آن import بگیرید.
