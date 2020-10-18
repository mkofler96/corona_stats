import requests, json, pandas
    
    
def get_most_infected_countries(number_of_countries):
        
    url = {"summary":        "https://api.covid19api.com/summary",
           "dayone_italy":   "https://api.covid19api.com/total/dayone/country/italy/"}
    
    
    data = requests.get(url["summary"]).json()
    
    glob = data["Global"];
    ctris = data["Countries"];
    
    
    # slugs
    # USA: united-states
    # italien: italy
    
    ctris = sorted(ctris, key = lambda k: k["TotalConfirmed"], reverse = 1)
    ctris_new_infected = sorted(ctris, key = lambda k: k["NewConfirmed"], reverse = 1)
    
    print("current confirmed Covid19 cases")
    print("Total:", glob["TotalConfirmed"]);
    
    country_names = []
    total_confirmed = []
    new_confirmed = []
    
    
    idx = 0
    for i in range(number_of_countries):
        current = ctris[i];
        country_names.append(current["Country"])
        total_confirmed.append(current["TotalConfirmed"])
        new_confirmed.append(current["NewConfirmed"])
        idx = idx+1;
    
    data_total = {'Position': list(range(1,number_of_countries+1)),
            'Country': country_names,
            'Total Cases': total_confirmed,
            'New Cases': new_confirmed}
    
    country_names = []
    total_confirmed = []
    new_confirmed = []
    
    idx = 0
    for i in range(number_of_countries):
        current = ctris_new_infected[i];
        country_names.append(current["Country"])
        total_confirmed.append(current["TotalConfirmed"])
        new_confirmed.append(current["NewConfirmed"])
        idx = idx+1;
    
    data_new_infected = {'Position': list(range(1,number_of_countries+1)),
            'Country': country_names,
            'Total Cases': total_confirmed,
            'New Cases': new_confirmed}
    
     
    # Create DataFrame
    df_total = pandas.DataFrame(data_total)
    
    df_new_infected = pandas.DataFrame(data_new_infected)
    countries = [df_total, df_new_infected]
    return countries