import pandas as pd


def parse_CSV(csv_file_path, metric, desired_vehicles=[], merge=False):
    '''
    metric: desired metric, e.g. busyTime(CBR), distance, ..
    desired_vehicles = all or specific vehicles?  e.g. [], [ '146' ,'151' ,'155' ,'159', '6', '10']
    merge: combine metric data for all vehicles or not?
    '''
  
    data = pd.read_csv(csv_file_path, low_memory=False)
    # Specify the columns of interest
    # type     = vector, param, etc
    # module   = network.node...    
    # name     = name of metric or statistic
    # vecvalue = value of the metric
    columns_of_interest = ['type', 'module', 'name', 'vecvalue'] 
    
    filtered_data = data[columns_of_interest]
    vector_data = filtered_data[filtered_data['type'] == 'vector']
    
    # getting name=metric , only data about the metric that we're interested in
    vector_data = vector_data[vector_data['name'].isin([metric])]

    # --- a row of vector data has values separated by space, we separate them by commas
    # ensure that 'vecvalue' is a string type
    vector_data['vecvalue'] = vector_data['vecvalue'].astype(str)
    # split the string to list of values    vecvalue_list is added
    vector_data['vecvalue_list'] = vector_data['vecvalue'].apply(lambda x: [float(i) for i in x.split()])

    # making module name better, creating vehicle_number column outof module column
    # We need only node number (as a string) and not the whole name of the module 
    vector_data['vehicle_number'] = vector_data['module'].str.extract(r'\[(\d+)\]').astype(str)

    # removing all unwanted columns except vehicle number and vecvalue_list
    vector_data.drop(columns=['module', 'type', 'vecvalue', 'name'], inplace=True)


    # list not empty means only some vehicles are kept
    if len(desired_vehicles) != 0:
        vector_data = vector_data[vector_data['vehicle_number'].isin(desired_vehicles)]

    if merge: # merged list (not a DataFrame) of the metric of all vehicles
        vector_data = vector_data['vecvalue_list'].sum()

    return vector_data



def get_filtered_minimums(dataframe):
    """
    take a DataFrame with a column 'vecvalue_list' containing lists of numbers.
    Then filters each list to keep only values between 0 and 20, and then returns a list of the 
    minimum value from each filtered list.
    """
    def filter_and_min(values):
        # keep only nums between 0 and 20
        filtered_values = [v for v in values if 0 <= v <= 20]    
        return min(filtered_values) if filtered_values else None
    
    return dataframe['vecvalue_list'].apply(filter_and_min).tolist()
