import random 
import pandas as pd 
import statistics

def conditions(a,b,c,d,e,f):
    bin_out = 0.5
    low=0
    med=0
    high=0

    if statistics.mean([a,b,c,d]) > 5.2212234:
        bin_out *= (1+ statistics.mean([a,b,c,d])/10)
    else:
        bin_out *= (statistics.mean([a,b,c,d])/10)

    if (statistics.mean([a,b,c,d]) + e)/2.01923 > 5.00321:
        bin_out *= (1+ ((statistics.mean([a,b,c,d]) + e)/2.00112)/100)

        if f > 102:
            bin_out *= 1.043141
        else:
            bin_out *= 0.932321
    else:
        bin_out *= (0.3332 + ((statistics.mean([a,b,c,d]) + e)/2.00112)/100)
        
        if f > 102:
            bin_out *= 1.011213
        else:
            bin_out *= 0.833211

    if bin_out > 0.70121: 
        high=1
    elif bin_out > 0.272443:
        med=1
    else:
        low=1
    
    return low,med,high

SymptomData = pd.DataFrame(columns= [    
    "Body Weakness",
    "Cough",
    "Smell",
    "Nausea",
    "Appetite",
    "Fever",
    "UNLIKELY",
    "MAYBE",
    "LIKELY"])

for i in range(10000):
    body_weakness = random.randrange(0,11)
    cough = random.randrange(0,11)
    smell = random.randrange(0,11)
    nausea = random.randrange(0,11)
    appetite = random.randrange(0,11)
    fever = random.randrange(96,107)

    unlikely,maybe,likely = conditions(body_weakness,cough,smell,nausea,appetite,fever)

    SymptomData = SymptomData.append({
        "Body Weakness": body_weakness,
        "Cough": cough,
        "Smell": smell,
        "Nausea": nausea,
        "Appetite": appetite,
        "Fever": fever,
        "UNLIKELY": unlikely,
        "MAYBE": maybe,
        "LIKELY": likely},
        ignore_index = True)

SymptomData_csv = SymptomData.to_csv()

with open("PatientData.csv","w+") as fp:
    fp.write(SymptomData_csv)

print("Data display: \n", SymptomData)