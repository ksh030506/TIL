# AWS kinds

## Compute
- **EC2(Elastic Compute Cloud)**
  - 클라우드 환경에서 서버를 할당 받아 사용할 수 있는 서비스, 서버 호스팅과 비슷한 개념이지만, 실제 물리적인 서버를 할당 받는 것이 아니라 클라우드 환경에서 가상으로 서버를 할당 받는 것

- **Auto Scaling**
  - 수요에 따라 EC2의 규모를 자동으로 조절 할 수 있는 서비스입니다
    ex) web server의 cpu load가 50%가 넘어가면 새로운 web server를 추가하도록 세팅가능

## Networking
- **DirectConnect**
  - AWS와 직접 연결된 전용 네트워크 서비스

- **Route 53**
  - DNS 서비스


- **VPC (Virtual Private Cloud**
  - 사설 네트워크 서비스

- **Elastic Load Balancing**
  - Load Balancing 서비스


## Storage & Content Delivery
- **Glacier**
  - 저비용 데이터 보관 및 백업 서비스
  - 자주 사용되지 않는 데이터를 보관 및 백업하는데 유용한 서비스

- **S3(Simple Storage Service)**
  - 인터넷 스토리지 서비스
  - 웹에서 바로 접근 가능
  - EC2에서도 mount해서 사용 가능

  - EC2 인스턴스에서 사용할 수 있는 블럭 레벨 스토리지
  - S3는 네트워크 스토리지
  - EBS는 서버에 추가할 수 있는 하드웨어 스토리지 (SATA)
  
  
- **CloudFront**
  - 콘텐츠 전송용 웹 서비스
  - CDN과 비슷한 서비스
  - EC2나 S3같은 서비스에서 사용시 가장 가까운 엣지로 자동 라우팅되어 콘텐츠 전송 속도를 향상


- **Storage Gateway**
  - aws의 스토리지와 로컬 스토리지를 연동해주는 서비스
  - 로컬에 있는 DAS, NAS, SAN과 같은 장비와 S3를 연동해서 메인 데이터는 S3에두고 접근빈도가 높은 데이터는 로컬 스토리지에 캐싱
  - 모든 데이터는 로컬 스토리지를 두고 일정 시간에 따라 주시적으로 데이터의 스냅샷을 S3에 저장

- Import/Exprot
  - 대용량 데이터를 이동식 디바이스에 직접 import/export 해 주는 서비스
  - 외장 하드같은 디바이스를 Amazon에 우편으로 보낸 다음, 데이터를 Import 또는 Exprot 후 다시 돌려받는 방식


