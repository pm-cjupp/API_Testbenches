from synology_drive_api.drive import SynologyDrive
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

NAS_IP = '192.168.1.65'
NAS_PORT= '5001'

NAS_USER = 'SharedAccount'
NAS_PASS = 'pQS3s6BPPn7u'

NAS_USER = 'cjupp'
NAS_PASS = 'ZJcj4GBSF9Frr9KCmGxy'

prod_sheet = 'Production_Record_Testbench.osheet'
file_path = '/team-folders/cjupp/Projects/Serial Number Tool'


# Use specified port
with SynologyDrive(NAS_USER, NAS_PASS, NAS_IP, NAS_PORT) as synd:
    print(synd.get_teamfolder_info())

    print(synd.list_folder('/team-folders/cjupp'))

    print(synd.get_file_or_folder_info('701208765814317115'))

    #print()
    #print()

    """bio = synd.download_file(f'/mydrive/{prod_sheet}')
    with open(prod_sheet, 'wb') as f:
        f.write(bio)
    pass"""


# get single label info
#synd.get_labels('your_label_name')
# get all labels info


