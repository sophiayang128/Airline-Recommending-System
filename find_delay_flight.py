
# coding: utf-8

# In[ ]:

def find_delay_flight(data, year=0,month=0,airline=0,airport=0):
    '''
    The function ask you to enter the year, month, airline and airport that you are interested in. It will return
    a list of flight delay information.
    
    :param param1: Input a data list that in the format of [0.year, 1.month, 2.airline code, 3.airport code,
    4.total number of flight, 5.total number of delayed flight*,
    6.total delayed minutes*, 7.percentage of delayed flight, 8.average delay minutes per delayed flight]
    
    :param param2: The year that is interested in
    :param param3: The month that is interested in
    :param param4: The airline that is interested in
    :param param5: The airport that is interested in
    
    :return: The list [total number of flight, total number of delayed flight*,
    total delayed minutes*, percentage of delayed flight, average delay minutes per delayed flight]
    '''
    #Find the row number that contain input year
    assert (year>=2012 and year<=2017) or year ==0
    assert (month>=1 and month<=12) or month ==0
    
    if year == 0:
        row_num = range(len(data))
    else:
        row_num = []
        for i in range(len(data)):
            if data[i][0] == year:
                row_num.append(i)
    
    #Find the row number that contain input month
    if month>0: #If the input of month is entered
        row_num_1 = []
        for i in row_num:
            if data[i][1] == month:
                row_num_1.append(i)
    else:
        row_num_1 = row_num
    
    #Find the row number that contain input carrier
    if airline == 0:
        row_num_2 = row_num_1
    else:
        row_num_2 = []
        for i in row_num_1:
            if data[i][2] == airline:
                row_num_2.append(i)
    
    #Find the row number that contain input airport
    if airport == 0:
        row_num_3 = row_num_2
    else:
        row_num_3 = []
        for i in row_num_2:
            if data[i][3] == airport:
                row_num_3.append(i)
                
    delay_info = []
    for i in row_num_3:
        arr_num = data[i][4]
        delay_num = data[i][5]
        total_delay_min = data[i][6]
        percent_delay_flight = data[i][7]
        avg_delay_min = data[i][8]
        airline0 = data[i][2]
        
        delay_info.append([arr_num,delay_num,total_delay_min,percent_delay_flight,avg_delay_min,airline0])
    return delay_info
    #return row_num_3

