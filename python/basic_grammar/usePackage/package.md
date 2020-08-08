패키지: 모듈들을 모아 놓은 집합, 하나의 디렉토리에 여러 모듈들을 가져다 놓은 것

신규 여행사의 프로젝트를 담당하게 되었다. 이 여행사는 태국과 베트남에 패키지 여행 상품을 판매한다.  
그 내용을 만들어서 누구나 사용할 수 있게 만들어 보자.  
먼저 새로운 폴더를 만들고 그 안에 thailand.py와 vietnam.py 파일을 생성한다.  
그리고 새로운 폴더에 **init**.py 파일을 생성한다.

각각의 내용을 작성한 뒤 사용할 때에는

```py
import usePackage.thailand
tirp_to = usePackage.thailand.ThailandPackage()
tirp_to.detail()
```

로 사용할 수가 있다. 주의 해야할 점은 import usePackage.thailand 에서  
import 구문을 사용할 때 thailand.py에 정의된 클래스를 바로 가져다 쓸 수 없다.  
import usePackage.thailand.ThailandPackage 처럼의 내용은 쓸 수 없다.  
대신 from/import 를 사용하면 정의한 클래스를 바로 사용 가능하다.

```py
from usePackage.thailand import ThailandPackage
tirp_to = ThailandPackage()
tirp_to.detail()
```

패키지의 모든 내용을 사용 할 때에는 from usePackage import \* 과 같이 사용하면 된다.  
그러기 위해서는 우선 개발자가 정의한 내용들의 공개 범위를 먼저 설정을 해주어야 한다.  
만약 **init**.py 에서

```py
__all__ = ["vietnam"]
```

을 설정해 두었다면

```py
from usePackage import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
```

과 같이 사용할 수가 있다.

현재 사용하고 있는 모듈의 위치 경로를 알고 싶다면 inspect를 사용하면 된다.

```py
from usePackage import *
import inspect
print(inspect.getfile(thailand))
```
