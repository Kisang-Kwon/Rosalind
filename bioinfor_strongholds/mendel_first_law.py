import sys


def calc_probability_mating_individual(k: int, m: int, n: int):
    def init_individual_count():
        individual_count = {"dominant_homo": k, "heterozygous": m, "recessive_homo": n}
        sum_of_individuals = k + m + n

        return individual_count, sum_of_individuals

    individual_count, sum_of_individuals = init_individual_count()
    recessive_prob = 0
    for x in individual_count:
        individual_count, sum_of_individuals = init_individual_count()

        x_prob = individual_count[x] / sum_of_individuals
        individual_count[x] -= 1
        sum_of_individuals -= 1
        for y in individual_count:
            y_prob = individual_count[y] / sum_of_individuals
            if (
                (x == "recessive_homo" and y == "recessive_homo")
                or (x == "recessive_homo" and y == "heterozygous")
                or (x == "heterozygous" and y == "recessive_homo")
                or (x == "heterozygous" and y == "heterozygous")
            ):
                gt_prob = calc_probability_for_recessive(x, y)
                recessive_prob += gt_prob * x_prob * y_prob

    return 1 - recessive_prob


def calc_probability_for_recessive(ip1: str, ip2: str):

    prob_for_recessive = {
        ("recessive_homo", "recessive_homo"): 1,
        ("recessive_homo", "heterozygous"): 0.5,
        ("heterozygous", "recessive_homo"): 0.5,
        ("heterozygous", "heterozygous"): 0.25,
    }

    return prob_for_recessive[(ip1, ip2)]


if __name__ == "__main__":
    p = calc_probability_mating_individual(
        int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    )
    print(p)
