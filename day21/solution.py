INGREDIENTS = 0
ALLERGENS = 1

def get_data(data):
    foods = {}
    for i, line in enumerate(data):
        line = line.strip()
        ingrs, allerg = line.split('(')
        ingrs = ingrs.strip().split(' ')
        # remove 'contains' and ending )
        allerg = allerg[8:-1]
        allerg = allerg.split(',')
        allerg = [a.strip() for a in allerg]
        foods[i] = (ingrs, allerg)
    return foods


# PART 1
def find_no_allergen(data):
    foods = get_data(data)

    # Set of allergens
    allergens = set()
    for line in foods.values():
        allergens.update(line[ALLERGENS])

    # appearances of allergen per line
    allergen_data = {}
    for al in allergens:
        allergen_data[al] = []
        for k, line in foods.items():
            if al in line[ALLERGENS]:
                allergen_data[al].append(k)

    # find ingredient correlations/intersection per allergen appearance
    allergen_results = {}
    for k, lines in allergen_data.items():
        options = [foods[line][0] for line in lines]
        result = set(options[0])
        for opt in options[1:]:
            result = result & set(opt)
        allergen_results[k] = result

    # TODO:  duplicated code with day 16
    # identify single allergen per ingredient
    while sum([len(ings) for ings in allergen_results.values()]) > len(allergen_results):
        singles = [rl for rl in allergen_results.values() if len(rl) == 1]
        not_singles = [k for k, rl in allergen_results.items() if len(rl) > 1]
        for ing in singles:
            for k in not_singles:
                allergen_results[k] -= ing

    # sets of ingredients with/without allergen
    ingr_with_allergen = set()
    for ingrs in allergen_results.values():
        ingr_with_allergen = ingr_with_allergen | ingrs
    ingr_without_allergen = set()
    for ingrs in foods.values():
        ingr_without_allergen = ingr_without_allergen | set(ingrs[0]) - ingr_with_allergen

    # count occurrances of without-allergen ingredients
    count = 0
    for line in foods.values():
        count += sum([line[INGREDIENTS].count(ing) for ing in ingr_without_allergen])

    return count, allergen_results


# PART 2
def get_alphabetical(allergens):
    ordered_ings = []
    for key in sorted(allergens.keys()):
        (ingr,) = allergens[key]
        ordered_ings.append(ingr)
    return ','.join(ordered_ings)


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    no_allergen_count, allergens = find_no_allergen(data)
    print(f'{no_allergen_count}')
    print('Part TWO')
    print(f'{get_alphabetical(allergens)}')


if __name__ == "__main__":
    main()
