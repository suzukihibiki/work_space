import paramiko

class MakeSession:
    def __init__(
        self,
        host,
        port,
        user,
        key_file = None,
        passphrase = None
    ) -> None:
        
        self.host = host
        self.port = port
        self.user = user
        self.key_file = key_file
        self.passphrase = passphrase
        
    def session(self):
        rsa_key = paramiko.RSAKey.from_private_key_file(self.key_file)
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, self.port, self.user, pkey=rsa_key)
        try:
            sftp_connection = ssh.open_sftp()
        finally:
            ssh.close()
        return sftp_connection
