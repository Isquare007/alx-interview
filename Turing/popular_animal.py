from collections import Counter
from typing import List

def solution(animals: str, f: List[str]) -> str:
    """things to consider:
    animals str is case sensitive
    there is a non aphabetical letter in animals
    f can contain more than one animals

    Args:
        animals (str): a str of diffrent animals
        f (List[str]): a list of forbidden animals

    Returns:
        str: the popular animal that is not forbidden
    """
    symbols = "!?',:."
    animals = animals.lower()
    
    for letter in animals:
        if letter in symbols:
            animals = animals.replace(letter, "")
            
    animals = animals.split()
    
    for forb in f:
        animals = [animal for animal in animals if animal != forb]
    print(animals)
    animal_count = Counter(animals)
    popular_animal = animal_count.most_common(1)[0][0]
    
    # for animal in animals:
    #     if animal in animal_count:
    #         animal_count[animal] += 1
    #     else:
    #         animal_count[animal] = 1
    # max = 0
    # pupular_animal = None
    # for key, val in animal_count.items():
    #     if val > max:
    #         max = val
    #         popular_animal = key
    
    return popular_animal   

    
animals = "Dog horse donkey CAT donkey ? caT bird donkey gorilla, chicken? hen hen came'l hen. goRilla"
f = ["donkey", "cat"]

print(solution(animals, f))