from algorithms import SecretAlgorithm
import argparse


attached_algorithm = None


def arrangement() -> tuple:
    return attached_algorithm.optimized_result()


def read_drivers(path: str) -> list:
    drivers = []
    with open(path, "r") as file:
        drivers = file.read().strip().split("\n")
    return drivers


def read_destinations(path) -> list:
    destinations = []
    with open(path, "r") as file:
        destinations = file.read().strip().split("\n")
    return destinations


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--drivers", help="the path of drivers data file", metavar="<drivers data file path>", required=True)
    argument_parser.add_argument(
        "--destinations", help="the path of destinations data file", metavar="<destinations data file path>", required=True)
    arguments = argument_parser.parse_args()

    attached_algorithm = SecretAlgorithm()
    attached_algorithm.set_drivers(read_drivers(arguments.drivers))
    attached_algorithm.set_destinations(
        read_destinations(arguments.destinations))

    total_score, matching = arrangement()
    print(f"The optimized total score is {total_score}")
    print(
        f"The outcome of the match is a list of tuples presented in the format of (<driver's name>, <destination>)\n{matching}")
