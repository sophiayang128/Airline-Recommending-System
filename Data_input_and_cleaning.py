
# coding: utf-8

# In[ ]:

def file_in(file_name):  
    '''
    First stage of data input, this function takes the raw data from the BTS website, removes invalid (empty)
    inputs and splits each row of data into lists.
    https://www.transtats.bts.gov/OT_Delay/ot_delaycause1.asp?display=chart&pn=1
    :param: file_name
    :type: str
    '''
    assert isinstance(file_name,str)
    f = open(file_name,'r')
    data = f.readlines()
    data = data[1:] # get rid of first row (headers)
    data_new = []
    for i in data: 
        data_line = i.split(',') # split rows into lists
        if '' not in data_line: # remove invalid entries
            data_new.append(data_line)
    return data_new

def data_clean(x): #data_new
    '''
    This function takes the output list from the previous function and cleans up the data. It removes unwanted columns
    and format the entries. The output of the function is a list of lists in the form of the following:
    [0.year, 1.month, 2.airline code, 3.airport code, 4.total number of flight, 5.total number of delayed flight*,
    6.total delayed minutes*, 7.percentage of delayed flight, 8.average delay minutes per delayed flight]
    *our interest of delayed flights does not include weather/nas/security delay, since it is not caused by the airline.
    '''
    assert isinstance (x,list)
    clean_data = []
    for i in x:
        new_line = []
        new_line.append(int(i[0])) #year, convert to integers
        new_line.append(int(i[1])) #month, convert to integers
        new_line.append(i[2][1:-1]) #Airline, convert from '"x"' to 'x'
        new_line.append(i[4][1:-1]) #Airport, convert from '"x"' to 'x'
        new_line.append(float(i[7])) #total number of flights
        new_line.append(round(float(i[9])+float(i[13]),2)) #total number of delayed flights
        new_line.append(float(i[16])+float(i[17])+float(i[21])) #total delayed minutes 
        new_line.append(round(new_line[5]/new_line[4]*100,2)) #percentage of delayed flight in %
        new_line.append(round(new_line[6]/(new_line[5]+0.00001),2)) #average delayed minutes per delayed flight
        clean_data.append(new_line)            
    return clean_data

