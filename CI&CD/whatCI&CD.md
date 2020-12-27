# CI/CD

- Continuous Integration ⇒ 통합(Code)
    - 여러 개발자들이 코드베이스를 계속 통합하는 것
        - continuous ingegration (CI) is practice of merging all developers' working copies to a shared mainline serveral imes a day
- Continuous Delivery ⇒ 배달(서비스)
    - 사용자에게 제품을 서비스를 지속적으로 배달한다.
    - 코드베이스가 항상 배포 가능한 상태를 유지하는 것
- Continuous Deployment
    - 코드베이스를 사용자가 사용가능한 환경에 배포하는 것을 자동화함

즉, CI/CD란 각각의 개발들이 개발을 하는 개발 환경을 사용자가 사용 가능한 서비스로 전달하는 모든 과정을 지속 가능한 형태로 또 가능하다면 자동으로 개발자와 사용자 사이의 격차를 없애는 것이다

이러한 과정은 코드를 빌드하고 테스트하고 배포하는 과정이 존재한다.

![/img/img1.png](/img/img1.png)

# CI가 왜 필요한가요?

- 10명의 개발자가 열심히 개발
- Merge Hell, Commit Hell

> 모든 개발자들이 안심하고 개발하기 위해 또, 내 코드와 멘탈의 평안을 위해....

# CD가 왜 필요한가요?

- 백엔드 코드 개발
- 프론트와 협업애야하니 배포 해야징
- 앗.. 버그 다시 배포
- 데브 서버 누가 배포했어? 나 안됨
- 앗 죄송 다시 배포
- 열심히 배포스크립트 수정 및 AWS 만지작...