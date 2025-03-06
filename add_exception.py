import subprocess

def add_exception():
    program_folder ='''
    Add-MpPreference -ExclusionPath 'C:\\Program Files\\PHSV Helper'
    '''
    subprocess.run(['powershell', f'{program_folder}'])