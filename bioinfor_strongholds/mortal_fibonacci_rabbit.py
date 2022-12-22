"""
Dynamic programming 개념을 이용하여 문제를 푼다.

토끼는 태어난 첫 달은 미성숙 상태 (i), 두번째 달부터 성체(m)가 되어 새끼를 낳을 수 있다.
토끼는 세 달(l) 뒤에 죽는다(d). 토끼 한 마리의 일생을 예시로 보면 i(1) - m(2) - m(3) - d(4) 이고, 
성체 기간인 t2, t3 에 새끼를 낳을 수 있다.

hyperparameter: 
    - l: 토끼의 수명

이 문제를 풀기 위해 [i, m, d] 3가지 값을 각 타임포인트 별로 저장해둔다.
    - i: 미성숙 토끼 수
    - m: 성체 토끼 수
    - d: 다음 타임포인트에 죽는 토끼 수
    
타임포인트 t에서 i, m, d 는 다음과 같은 규칙을 가진다.
    - i: t-1 에서 m + i - d
    - m: t-1 에서 m 의 개수
    - d: t-l+1 에서 i 의 개수, t-l+1 <= 0 인 경우 0 이 된다.
"""
import sys


def main():
    n_rabbits = dict()
    endpoint = int(sys.argv[1])
    lifetime = int(sys.argv[2])
    
    for timepoint in range(1, endpoint+1):
        if timepoint == 1:
            n_rabbits[1] = {
                "i": 1,
                "m": 0,
                "d": 0
            }
            continue
        
        i = n_rabbits[timepoint-1]["m"]
        m = n_rabbits[timepoint-1]["i"] + n_rabbits[timepoint-1]["m"] - n_rabbits[timepoint-1]["d"]
        d = 0 if timepoint-lifetime+1 <= 0 else n_rabbits[timepoint-lifetime+1]["i"]
        
        n_rabbits[timepoint] = {
            "i": i,
            "m": m,
            "d": d
        }

    rabbit_count = n_rabbits[endpoint]["i"] + n_rabbits[endpoint]["m"]
    sys.stdout.write(f"{rabbit_count}\n")
    sys.stdout.flush()
    
    return


if __name__ == "__main__":
    main()