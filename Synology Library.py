from synology_api import filestation, downloadstation

syn_ip = '192.168.1.65'
syn_port= '5001'

username = 'SharedAccount'
password = 'pQS3s6BPPn7u'


# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will log in automatically

fl = filestation.FileStation(syn_ip, syn_port, username, password, secure=False, cert_verify=False, dsm_version=6, debug=True, otp_code=None)

fl.get_info()

#dwn = downloadstation.DownloadStation(syn_ip, syn_port, username, password, secure=False, cert_verify=False, dsm_version=3, debug=True, otp_code=None)

#dwn.get_info()

