from synology_drive_api.drive import SynologyDrive

NAS_IP = '192.168.1.65'
NAS_PORT= '5001'

NAS_USER = 'SharedAccount'
NAS_PASS = 'pQS3s6BPPn7u'

prod_sheet = 'Production_Record_Testbench.osheet'
file_path = '/cjupp/Projects/Serial Number Tool'
# Use specified port
with SynologyDrive(NAS_USER, NAS_PASS, NAS_IP, NAS_PORT) as synd:
    print(synd.get_teamfolder_info())

    print()
    print()
    print()
    print()

    bio = synd.download_file(f'/mydrive/{prod_sheet}')
    with open(prod_sheet, 'wb') as f:
        f.write(bio)
    pass


# get single label info
#synd.get_labels('your_label_name')
# get all labels info


