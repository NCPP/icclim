# set the attributs "long_name" and "units" of indice variable in output meta data
# (for indices with user defined thrshold)

def SU_setvarattr(var_nc, threshold):
    long_name_str = 'Number of days with daily maximum temperature > {0} degrees)'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

def CSU_setvarattr(var_nc, threshold):
    long_name_str = 'Maximum number of consecutive days with daily maximum temperature > {0} degrees)'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

def TR_setvarattr(var_nc, threshold):
    long_name_str = 'Number of days with daily minimum temperature > {0} degrees'.format(threshold)
    var_nc.setncattr('long_name', long_name_str)
    var_nc.setncattr('units', 'days')

