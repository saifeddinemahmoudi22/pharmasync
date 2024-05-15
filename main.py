import pickle
complaints_list = [
    {'num': 1, 'complaint_about': 'robbery', 'date': '10/Jan/2022', 'victim_age': 35, 'victim_sex': 'male',
     'region': 'Bronx'},
    {'num': 2, 'complaint_about': 'murder', 'date': '15/Mar/2022', 'victim_age': 45, 'victim_sex': 'female',
     'region': 'Manhattan'},
    {'num': 3, 'complaint_about': 'rape', 'date': '20/Aug/2022', 'victim_age': 25, 'victim_sex': 'female',
     'region': 'Brooklyn'},
    {'num': 4, 'complaint_about': 'insult', 'date': '25/Oct/2022', 'victim_age': 28, 'victim_sex': 'male',
     'region': 'Bronx'},
    {'num': 5, 'complaint_about': 'road accident', 'date': '30/Dec/2022', 'victim_age': 32, 'victim_sex': 'female',
     'region': 'Manhattan'},
    {'num': 6, 'complaint_about': 'driving while intoxicated', 'date': '5/Feb/2023', 'victim_age': 40,
     'victim_sex': 'male', 'region': 'Brooklyn'},
    {'num': 7, 'complaint_about': 'robbery', 'date': '10/Apr/2023', 'victim_age': 55, 'victim_sex': 'female',
     'region': 'Bronx'},
    {'num': 8, 'complaint_about': 'murder', 'date': '15/Jun/2023', 'victim_age': 30, 'victim_sex': 'male',
     'region': 'Manhattan'},
    {'num': 9, 'complaint_about': 'rape', 'date': '20/Sep/2023', 'victim_age': 22, 'victim_sex': 'female',
     'region': 'Brooklyn'},
    {'num': 10, 'complaint_about': 'insult', 'date': '25/Nov/2023', 'victim_age': 38, 'victim_sex': 'male',
     'region': 'Bronx'},
    {'num': 11, 'complaint_about': 'road accident', 'date': '1/Jan/2024', 'victim_age': 20, 'victim_sex': 'female',
     'region': 'Manhattan'},
    {'num': 12, 'complaint_about': 'driving while intoxicated', 'date': '5/Mar/2024', 'victim_age': 45,
     'victim_sex': 'male', 'region': 'Brooklyn'},
    {'num': 13, 'complaint_about': 'robbery', 'date': '10/May/2024', 'victim_age': 50, 'victim_sex': 'female',
     'region': 'Bronx'},
    {'num': 14, 'complaint_about': 'murder', 'date': '15/Jul/2024', 'victim_age': 35, 'victim_sex': 'male',
     'region': 'Manhattan'},
    {'num': 15, 'complaint_about': 'rape', 'date': '20/Sep/2024', 'victim_age': 28, 'victim_sex': 'female',
     'region': 'Brooklyn'},
    {'num': 16, 'complaint_about': 'insult', 'date': '25/Nov/2024', 'victim_age': 42, 'victim_sex': 'male',
     'region': 'Bronx'},
    {'num': 17, 'complaint_about': 'road accident', 'date': '1/Jan/2022', 'victim_age': 18, 'victim_sex': 'female',
     'region': 'Manhattan'},
    {'num': 18, 'complaint_about': 'driving while intoxicated', 'date': '5/Mar/2022', 'victim_age': 55,
     'victim_sex': 'male', 'region': 'Brooklyn'},
    {'num': 19, 'complaint_about': 'robbery', 'date': '10/May/2022', 'victim_age': 42, 'victim_sex': 'female',
     'region': 'Bronx'},
    {'num': 20, 'complaint_about': 'murder', 'date': '15/Jul/2022', 'victim_age': 33, 'victim_sex': 'male',
     'region': 'Manhattan'}
]


# question 1
def complaints_change_date(complaints_list):
    complaints_list_with_datetime = liste(
        map(lambda x: {**x, 'date': datetime.strptime(x['date'], '%d/%b/%Y')}, complaints_list))
    return (complaints_list_with_datetime)



# question 2

def complaint_type():
    f = open(complaint_type.pkl, "rb")
    list_p = pickle.load(f)
    f.close()
    return list_p





# question 3
def search(complaints_list):
    def filter_by_offense(offense):
        def filter_by_sex(sex):
            return list(filter(lambda x: x['complaint_about'] == offense and x['victim_sex'] == sex, complaints_list))

        def filter_by_age(age):
            return list(filter(lambda x: x['complaint_about'] == offense and x['victim_age'] == age, complaints_list))

        return {'filter_by_sex': filter_by_sex, 'filter_by_age': filter_by_age}

    return filter_by_offense





    def calcul_statistiques():
        for sex in complaints_list :
            sex  = complaint['female']
            if female not in statistics:
                statistics[sex] = {}
                statistics[sex][female] = 1
            else:
                statistics[sex][female] += 1

        for complaint in complaints_list:
            region = complaint['region']
            offense = complaint['complaint_about']
            if region not in statistics:
                statistics[region] = {}
            if offense not in statistics[region]:
                statistics[region][offense] = 1
            else:
                statistics[region][offense] += 1

        with open('statistique.txt', 'w') as file:
            for sex, region, offenses in statistics.items():
                file.write(f"Region:{region}\n")
                for offense, count in offenses.items():
                    file.write(f"\tOffense:{offense},Count:{count}\n")
                    for sex, count in vectim_sex():
                        file.write(f"\sex:{female},Count:{count}\n")

    begin_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 1, 1)
    print(complaints_change_date(complaints_list))
    print(complaint_by_period(begin_date, end_date))

    complaint_type_list = [
        {'num': 1, 'complaint_type': 'felony'},
        {'num': 2, 'complaint_type': 'felony'},
        {'num': 3, 'complaint_type': 'felony'},
        {'num': 4, 'complaint_type': 'violation'},
        {'num': 5, 'complaint_type': 'misdemeanor'},
        {'num': 6, 'complaint_type': 'misdemeanor'},
        {'num': 7, 'complaint_type': 'felony'},
        {'num': 8, 'complaint_type': 'felony'},
        {'num': 9, 'complaint_type': 'felony'},
        {'num': 10, 'complaint_type': 'violation'},
        {'num': 11, 'complaint_type': 'misdemeanor'},
        {'num': 12, 'complaint_type': 'misdemeanor'},
        {'num': 13, 'complaint_type': 'felony'},
        {'num': 14, 'complaint_type': 'felony'},
        {'num': 15, 'complaint_type': 'felony'},
        {'num': 16, 'complaint_type': 'violation'},
        {'num': 17, 'complaint_type': 'misdemeanor'},
        {'num': 18, 'complaint_type': 'misdemeanor'},
        {'num': 19, 'complaint_type': 'felony'},
        {'num': 20, 'complaint_type': 'felony'}
    ]

