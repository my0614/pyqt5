# 스케줄링
처리율과 CPU 이용률을 증가시키고, 응답시간, 반환시간, 대기시간등을 
   최소화 시키기 위한 기법입니다. 효율적인 계획을 잡아주는것이 스케줄링이다.

# RR스케줄링 (Round RoBin Scheduling)
라운드 로빈 스케줄링(Round Robin Scheduling, RR)은 시분할 시스템을 위해 설계된 선점형 스케줄링의 하나로서, 프로세스들 사이에 우선순위를 두지 않고, 순서대로 시간단위(Time Quantum/Slice)로 CPU를 할당하는 방식의 CPU 스케줄링 알고리즘입니다.
컴퓨터 자원을 사용할 수 있는 기회를 프로그램 프로세스들에게 공정하게 부여하기 위한    한 방법으로서, 각 프로세스에 일정시간을 할당하고, 할당된 시간이 지나면 그 프로세스는   잠시 보류한 뒤 다른 프로세스에게 기회를 주고, 또 그 다음 프로세스에게 하는 식으로,  돌아가며 기회를 부여하는 운영방식입니다.

# RR스케줄링 시간과장점
보통 시간 단위는 10 ms ~ 100 ms 정도로, 시간 단위동안 수행한 프로세스는 준비 큐의 끝으로 밀려나게 되고, 문맥 전환의 오버헤드가 큰 반면에 응답시간이 짧아지는 장점이 있어 실시간 시스템에 유리합니다.


## 비선점 스케줄링
비선점 스케줄링 은 이미 할당된 CPU를 다른 프로세스가 강제로 빼앗아 사용할 수 없는 스케줄링 기법입니다. 선점 방식보다 스케줄러 호출 빈도가 낮고 문맥 교환에 의한 오버헤드도 적습니다. 일괄처리 시스템에 적합하고, CPU 사용 시간이 긴 하나의 프로세스가 CPU 사용 시간이 짧은 여러 프로세스를 오랫동안 대기시킬 수 있으므로, 처리율이 떨어질 수 있다는 단점도 있습니다.

## 선점 스케줄링
선점 스케줄링 은 하나의 프로세스가 CPU를 할당 받아 실행하고 있을 때 우선 순위가 높은 다른 프로세스가 CPU를 강제로 빼앗아 사용할 수 있는 기법입니다. 모든 프로세스에게 CPU 사용 시간을 동일하게 부여할 수 있으며, 빠른 응답시간을 요하는 대화식 시분할   시스템에 적합하며 긴급한 프로세서를 제어할 수 있습니다.