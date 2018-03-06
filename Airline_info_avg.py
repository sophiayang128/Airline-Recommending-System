
# coding: utf-8

# In[ ]:

def airline_info_avg(data): #Input is the output of find_delay_flight
    #[0.total number of flight, 1.total number of delayed flight*,
    #2.total delayed minutes*, 3.percentage of delayed flight, 4.average delay minutes per delayed flight,
    #5.airline_name]
    airline_name = []
    for i in range(len(data)):
        if data[i][5] not in airline_name:
            airline_name.append(data[i][5])
            
    dic = {}
    for i in range(len(airline_name)):
        num_flight = 0
        total_min = 0
        airline_info = []
        
        #Find out the match airline and get the info as list
        for count in range(len(data)):
            if data[count][5]==airline_name[i]:
                airline_info.append(data[count])
        
        for j in range(len(airline_info)):
            num_flight += airline_info[j][0]
            total_min += airline_info[j][2]
        
        if num_flight>0:
            min_per_flight = total_min/num_flight
            dic[airline_name[i]] = min_per_flight
    return dic

