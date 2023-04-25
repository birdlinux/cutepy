# cutepy
A package that allows you to have simplicity and effectiveness in your projects


## Spiner

![image](https://user-images.githubusercontent.com/123122904/234284220-2953eff5-9213-4c1a-bd23-963da659e549.png)

```py
from cutepy import Loader

spinners = ["|", "/", "-", "\\"]
Loader.spinner("Loading", 4, spinners)
```

## RGB Printing

![image](https://user-images.githubusercontent.com/123122904/234284609-44688659-b1cf-4e98-ad3e-fecd72f91b23.png)

```py
from cutepy import RGB

x = RGB.print(103, 252, 125)
print(f"Hello {x}RGB{RGB.reset} test {x}aa{RGB.reset} ")
```

## HEX Printing

![image](https://user-images.githubusercontent.com/123122904/234285095-a18f1329-6ca0-4405-b237-a0a5a1311881.png)

```py
from cutepy import HEX

x = HEX.print("6771fc")
print(f"Hello {x}RGB{RGB.reset} test {x}aa{RGB.reset}")
```

## System Detection

![image](https://user-images.githubusercontent.com/123122904/234285304-16d2ba46-af42-40df-8362-6ffe22bcd447.png)

```py
from cutepy import System

x = System.detect()
print(x)
```

## Terminal Clear

![image](https://user-images.githubusercontent.com/123122904/234285579-2baccc66-e3e5-4ae8-976f-888f06f1c22d.png)

```py
from cutepy import Clear

Clear.sys()
```

## Hash Identifier

![image](https://user-images.githubusercontent.com/123122904/234285702-521d7f57-d548-4e96-972a-5cd05447f001.png)

```py
from cutepy import Identify

x = Identify.hash("a875e3b9476d5d976160b308ace6b62e")
print(x)
```

## Color Palette

![image](https://user-images.githubusercontent.com/123122904/234285853-d837186b-194b-4339-a386-0acb26066c9a.png)

```py
from cutepy import Color

Color.palette()
```
