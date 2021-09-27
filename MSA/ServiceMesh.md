# Service Mesh Architecture를 알아보자

### Overview
- - -

<img src="../img/monolithic_vs_microservices.jpg">

이전 TIL에서 `MicroService Architecture`의 장단점에 대해서 알아봤습니다.

기존 `Monolithic Architecture`의 단점을 극복하고 Cloud환경에서 시스템 운영을 최적화 시키기 위해 많이 사용되고 있습니다.

이번 포스팅에서는 단점을 극복하기 위한 Architecture중 `Service Mesh Architecture`에 대해서 알아보겠습니다.

## Service Mesh Architecture

### MicroService Architecture의 단점
기존 `Monolithic Architecture`의 단점을 극복하고 작은 서비스들로 하나의 서비스를 이루는 것은 각각의 서비스들을 독립적으로 관리할 수 있다는 점에서 유연하게 운용할 수 있었지만,

거대해진 MSA시스템을 보면 수십개의 MicroService가 분리되어있고 운영환경에는 수천개의 서비스 인스턴스가 동작하고 있습니다.

물론 **관리자는 수백, 수천개의 인스턴스들을 모니터링하고 로깅해야하며 관리해야하는 책임**이 주어지게 됩니다.(부담....)

또한 서비스간의 통신도 매우 복잡해질수밖에 없습니다.

이와 같은 관리 및 프로그래밍 오버헤드를 낮추기 위해 나온 아키텍처가 `Service Mesh`입니다.

### Service Mesh
`Service Mesh`는 쉽게 말해 마이크로서비스간의 통신(네트워크)을 담당하는 요소입니다. 즉, 통신 및 네트워크 기능을 비즈니스 로직과 분리한 네트워크 통신 인프라입니다.

모든 서비스의 인프라 레이어로서 서비스들 간의 통신을 처리하며, 위의 언급된 많은 기능들을 포함하고 있습니다.

마이크로서비스 구성 요소간 상호 통신을 위해서는 
**Service Discovery**  
**서비스 라우팅**  
**Failure recovery**  
**load balancing(트래픽 관리)**  
**보안** 등의 문제를 처리할 수 있는 메커니즘이 필요합니다.

그래서 `Service Mesh` 아키텍처를 사용하여 다양한 메커니즘을 처리하곤 합니다.

<img src="../img/service-mesh-generic-topology.png">

기존의 서비스 아키텍처에서의 호출이 직접 호출방식이었다면,
<img src="../img/last-architecture.png">

`Service Mesh`에서의 호출은 서비스에 딸린 proxy끼리 이뤄지게 됩니다.
<img src="../img/now-architecture.png">



