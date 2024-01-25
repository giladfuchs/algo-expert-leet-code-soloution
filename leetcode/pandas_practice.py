import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def calculate_bonus(row):
        if row['name'][0] != 'M' and row['employee_id'] % 2 == 1:
            return 1
        else:
            return 0

    employees['bonus'] = employees.apply(calculate_bonus, axis=1)
    employees['bonus'] = employees['bonus'] * employees['salary']
    filtered = employees.drop(['name', 'salary'], axis=1).sort_values(by='employee_id')
    return filtered

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    filtered = (tweets[(tweets['content'].str.len() > 15)]).drop(['content'],
                                                                 axis=1)

    return filtered


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered = (products[(products['low_fats'] == 'Y') | (products['recyclable'] == 'Y')]).drop(
        ['low_fats', 'recyclable'],
        axis=1)
    return filtered


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    filtered = (world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]).drop(['continent', 'gdp'],
                                                                                            axis=1)
    return filtered


if __name__ == '__main__':
    # data = {
    #     'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
    #     'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
    #     'area': [652230, 28748, 2381741, 468, 1246700],
    #     'population': [25500100, 2831741, 37100000, 78115, 20609294],
    #     'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
    # }
    #
    # df = pd.DataFrame(data)
    # big_countries(world=df)
    #
    # data = {
    #     'name': ['Afghanistan', 'Albania', ],
    #     'content': ['Vote for Biden ', 'Let us make America great again', ],
    #
    # }
    # tweets = pd.DataFrame(data)
    # invalid_tweets(tweets=tweets)

    data = {
        'employee_id': [2, 3, 7, 8, 9],
        'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'],
        'salary': [3000, 3800, 7400, 6100, 7700]
    }
    employees = pd.DataFrame(data)
    calculate_special_bonus(employees=employees)
