from collections import defaultdict
from math import gcd


class SecretAlgorithm:
    __drivers = []
    __destinations = []

    def set_drivers(self, drivers: list) -> None:
        self.__drivers = drivers

    def set_destinations(self, destinations: list) -> None:
        self.__destinations = destinations

    def __vowel_and_consonant_count(self, string: str) -> dict:
        result = defaultdict(int)
        vowels = "aeiou"
        for c in string.lower():
            if c in vowels:
                result["vowel"] += 1
            else:
                result["consonant"] += 1
        return result

    def calculate_suitability_score(self, *, driver: str, destination: str) -> float:
        if driver == None or destination == None:
            raise Exception("please validate your inputs")

        vowel_and_consonant_count = self.__vowel_and_consonant_count(driver)
        result = 0
        if len(destination) % 2 == 0:
            result = float(vowel_and_consonant_count["vowel"]) * 1.5
        result = float(vowel_and_consonant_count["consonant"])

        if gcd(len(driver), len(destination)) > 1:
            result *= 1.5

        return result

    def optimized_result(self) -> tuple:
        score_list = []
        for driver in self.__drivers:
            for destination in self.__destinations:
                score_list.append((self.calculate_suitability_score(
                    driver=driver, destination=destination), driver, destination))

        score_list.sort(reverse=True)

        total_score = 0
        matching = []
        driver_assigned = set()
        destination_assigned = set()
        for candidate in score_list:
            score = candidate[0]
            driver = candidate[1]
            destination = candidate[2]

            if (driver in driver_assigned) or (destination in destination_assigned):
                continue

            total_score += score
            matching.append((driver, destination))
            driver_assigned.add(driver)
            destination_assigned.add(destination)

        return (total_score, matching)
