from typing import List, Dict, Set, Union


def filter_selection() -> List[str]:
    """
    The user inputs which of the filters they would like to use by inputing the numbers matching the filters
    """

    print("Select filters you want to apply (comma-separated): ")
    print("1. Genre Filter")
    print("2. Spoken Languages")
    print("3. Runtime Filter")
    print("4. Score Filter")
    print("5. Release Date Filter")

    user_filter_choices = input("Enter the numbers of the filters you want to apply (e.g., 1,2,3): ")
    filters_to_apply = [filter.strip() for filter in user_filter_choices.split(",")]

    return filters_to_apply