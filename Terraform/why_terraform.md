
## 👺 테라폼 도입을 고민해야 하는 이유

Terraform 이름은 너무 멋졌다...

막 행성이름 같이 생겨서..

어쨋든... 전 회사에서 Terraform을 사용하길래...

이번 기회에 고민해보기로 하였다..

## 코드로서의 인프라스트럭처를 지향한다
테라폼은 하시코프에서 만든 관리 도구이다. 몰라 그냥 대충 정리할래...
인프라를 만들고 버전 관리하고...
안전하고... 효율적으로 하기 위한 툴... (이라고 배웠다)

그니까 인프라 구축을 도와주는 것 -> 왜 필요할까?

AWS나 AZURE, CloudFlare 등 클라우드 서비스...
Iac 주목..
**애플리케이션 처럼 인프라를 버전관리 할 수 있다면??**

##### 여담 : 테라폼을 배우게 된 계기
- 전 회사에서 정말 중요한 Admin ECS를 삭제...
- terraform apply 하나로 끗 🤭
- 원익님이랑 VPC 삭제 문제 30분?...

#### <u>사람은 실수 할 수 있다</u>
- 모르고 이상한 것을 지웠다면?
- 모르고 이상한 것을 만들었다면?
- 모르고 이상한 것을 수정하였다면?
- 이건 뭐고 저건 뭐지? 지워도 되나? 안되나? 씨부엉.... 모르겠다....

모두 매출에 큰 손실이 갈 수 도 있다...

#### <u>인수인계 및 개발 작업</u>
- 전 회사에서는 도움이 많이 되었다...
- 개발자 : 저 여기까지 했는데... 다음은 어떻게 하면 될까요?
- 개발자2 : 저 여기 코드 리뷰 좀 해주세요
- DevOps 신입 사원 : 저 처음 왔는데 인프라는 어떻게 설계되어 있나요?
- 개발자3 : 이거 뭐지? 삭제해도 되는 건가? 2019년도에 만들었는데 어디에 사용되는거지?

#### <u>코드를 빠르게 😵‍💫 그리고 효과적으로</u>
- terraform plan 으로 적용할 리소드들을 확인하고 빠르게 만들어낼 수 있습니다.
- 빨리 효과적으로 소프트웨어 딜리버리
- 인프라를 빠르게 프로비저닝하고 Iac를 활용해 효율적으로 자동화
  - 프로비저닝 : 시스템을 즉시 사용할 수 있는 상태로 준비

#### <u>정교한 멀티클라우드 지원</u>
- 트레바리 DevOps : AWS, CloudFlare
- 다양한 프로바이더를 지원한다.

#### 리소스 추적
- VPC 삭제하기 전에 라우팅 먼저 지우고... EIP 지우고... 내가 뭘 했지??

#### 똑똑한 Terraform
1. 전체 add (16개)
2. 그 중 2개를 바꿈
3. 중요한 옵션 삭제 시 리소스 삭제 -> add
4. 별로 중요하지 않아 -> update
5. terraform plan 시 -> add 1, change 1, delete 1

#### 단점
- 기존 인프라 가져오기... 너무 많거나 복잡하면 어려움...
- HCL 언어 공부
- 높은 러닝커브...
  - 클라우드 내의 의존도
- 더 어렵고 더 복잡한 리소스가 무조건 존재

## 그래도...
- 내가 만든 리소스를 추적한다는 점에서 사용, 빠르게 딜리버리 할 수 있다. (모듈 사용)

#### 극단적인 예시
오늘 라이언은 RDS 인스턴스 1개, 클러스터 1개를 만들고 새로만들 서브넷 들을 db_subnet_parameter로 만들어서 사용할 예정입니다. master_db_user와 master_pw는 임의로 정하고 2주마다 한번씩 KMS와 SecretManager로 변경하게 할 예정입니다. 그리고 새로운 RDS를 사용할 보안그룹들을 ingress 허용그룹에 넣어줄 예정입니다.

- 콘솔 : 내가 어디까지 했지? 이제 뭐해야하지?...
- Terraform : 버전 관리 및 리소스 모듈 사용

지금 트레바리 DevOps 리소스는 많지 않지만, 더더욱 많아지고 점점 GUI로 기억/문서화 할 수 없기 때문에...

#### AWS 프로바이더 레퍼런스
- [Terraform 프로바이더](https://registry.terraform.io/browse/providers)
- [CloudFlare 프로바이더](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [AWS 프로바이더: aws](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS 리소스: aws_key_pair](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/key_pair)
- [AWS 데이터 소스: aws_security_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/security_group)
- [AWS 리소스: aws_security_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group)
- [AWS 리소스: aws_instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)
- [AWS 리소스: aws_db_instance](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/db_instance)