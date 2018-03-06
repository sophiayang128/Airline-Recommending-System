def plot_airport(airport_name):
    '''
    Input an airport code, such as 'LAX'
    '''
    x = file_in('902103314_112017_5253_airline_delay_causes.csv')
    clean_data = data_clean(x)
    data = find_delay_flight(clean_data,month = 3,airport = airport_name)
    info_dict = airline_info_avg(data)
    import matplotlib.pyplot as plt
    sort_dict =sorted(info_dict.items(), key=lambda x: x[1])
    name_list = [item[0] for item in sort_dict]
    plt.bar(range(len(info_dict)),[item[1] for item in sort_dict],tick_label=name_list)
    plt.ylabel('min of delay per flight')
    plt.title('Minutes of Delay per Flight in Airport %s in March'%airport_name);
    plt.show()
