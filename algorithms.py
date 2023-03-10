from collections import defaultdict
from math import gcd

import numpy as np
from scipy.optimize import linear_sum_assignment


class SecretAlgorithm:
    __drivers = []
    __destinations = []

    def set_drivers(self, drivers: list[str]) -> None:
        if (not isinstance(drivers, list)):
            raise Exception("Please validate your drivers is a list.")
        self.__drivers = drivers

    def set_destinations(self, destinations: list[str]) -> None:
        if (not isinstance(destinations, list)):
            raise Exception("Please validate your destinations is a list.")
        self.__destinations = destinations

    def __vowel_and_consonant_count(self, string: str) -> dict:
        result = defaultdict(int)
        vowels = "aeiou"
        for c in string.lower():
            if not c.isalpha():
                continue

            if c in vowels:
                result["vowel"] += 1
            else:
                result["consonant"] += 1
        return result

    def calculate_suitability_score(self, *, driver: str, destination: str) -> float:
        if (not isinstance(driver, str)) or (not isinstance(destination, str)):
            raise Exception("Please validate your inputs are strings.")

        vowel_and_consonant_count = self.__vowel_and_consonant_count(driver)
        driver_name_length = len(driver)
        destination_name_length = len(destination)
        result = 0
        if (destination_name_length != 0) and (destination_name_length % 2 == 0):
            result = float(vowel_and_consonant_count["vowel"]) * 1.5
        else:
            result = float(vowel_and_consonant_count["consonant"])

        if gcd(driver_name_length, destination_name_length) > 1:
            result *= 1.5

        return result

    def optimized_result(self) -> tuple:
        drivers_list_length = len(self.__drivers)
        destinations_list_length = len(self.__destinations)

        if (drivers_list_length == 0) or (destinations_list_length == 0):
            raise Exception("Please make sure at least one input is in BOTH drivers and destinations list.")

        score_matrix = np.zeros((drivers_list_length, destinations_list_length))
        for i in range(drivers_list_length):
            for j in range(destinations_list_length):
                driver = self.__drivers[i]
                destination = self.__destinations[j]
                if (not isinstance(driver, str)) or (not isinstance(destination, str)):
                    raise Exception("Please validate your drivers and destinations are list of strings.")

                score_matrix[i][j] = self.calculate_suitability_score(driver=driver, destination=destination)

        rows_assigned, columns_assigned = linear_sum_assignment(score_matrix, maximize=True)
        total_score = score_matrix[rows_assigned, columns_assigned].sum()
        matching = list(map(lambda x, y: (self.__drivers[x], self.__destinations[y]), rows_assigned, columns_assigned))

        return (total_score, matching)
