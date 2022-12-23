"""
각 세대의 개체 수는 2^k
k 세대에서 적어도 N 명의 AaBb genotype 을 가진 개체가 존재할 확률 구하기

'각 세대의 개체는 항상 AaBb genotype 개체와 교배한다고 가정한다.' 는 조건으로 인해서
각 세대에서 AaBb genotype 이 발생할 확률은 항상 1/4 로 고정된다. (각 allele 독립적으로 유전되기 떄문이다.)
즉, B(2**k, 1/4) 인 이항분포를 따른다.

k 세대에서 적어도 N 명의 AaBb genotype 개체가 존재할 확률은 AaBb 가 0 ~ N-1 개 존재할 확률을 1에서 뺀 값이다.
"""
import math
import sys


def main(k, N):
    total_prob = 0
    for n in range(N):
        prob_success = (1/4)**n
        prob_fail = (3/4)**(2**k - n)
        
        total_prob += math.comb(2**k, n) * prob_success * prob_fail
    
    print(round(1 - total_prob, 3))
    return


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))