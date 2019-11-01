# Process, Thread

## Thread

Python 프로그램은 기본적으로 하나의 thread에서 실행된다. 하나의 메인 thread가 python 코드를 순차적으로 실행한다. 

### GIL(Global Interpreter Lock)

* 파이썬에서는 하나의 프로세스안에 모든 자원의 lock을 global하게 관리함으로써 한번에 하나의 쓰레드만 자원을 컨트롤하여 동작하도록 한다.
* GIL이 적용되는 것은 cpu 동작에서이고 쓰레드가 cpu 동작을 마치고 I/O 작업을 실행하는 동안에는 다른 쓰레드가 cpu 동작을 동시에 실행할 수 있다.

### Threading module

#### daemon

* 메인 쓰레드가 종료되도 자신의 작업이 끝날 때까지 계속 실행된다.(기본적으로 daemon 속성이 False)
* 부모 종료되면 즉시 끝나게 하려면 True를 설정한다.

## Process

* 복잡하고 시간이 걸리는 작업을 별도의 프로세스로 병렬처리할 수 있다.
* 멀티 프로세싱을 활용하여 멀티코어의 CPU의 장점을 극대화하고 빠른 처리를 지원할 수 있다.

### process pool

process 병렬처리의 편리한 수단을 제공한다.

### process간 통신

* queue: 여러 producer와 consummer로 통신할 수 있다.
* pipe: 오직 2개의 endpoint만으로 통신한다.(queue보다 빠르다.)

## Thread vs Process

* 쓰레드는 GIL로 인해 계산 처리를 하는 작업은 한번에 하나의 쓰레드에서만 작동하여 cpu 작업이 적고 I/O 작업이 많은 병렬 처리 프로그램에서 효과를 볼 수 있다.
* 프로세스는 각자가 고유한 메모리 영역을 가지기 때문에 더 많은 메모리를 필요로 하지만, 각각 프로세스에서 병렬로 cpu 작업을 할 수 있다.

## Reference

* [Python 파이썬 멀티 쓰레드(thread)와 멀티 프로세스(process)](https://monkey3199.github.io/develop/python/2018/12/04/python-pararrel.html)
* [multiprocessing — 프로세스 기반 병렬 처리 — Python 3.8.0 문서](https://docs.python.org/ko/3/library/multiprocessing.html)
