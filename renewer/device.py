class DeviceInfo:
    def __init__(self, hostname, ssh_port, ssh_id, ssh_pwd, enable):
        self.hostname = hostname
        self.ssh_port = ssh_port
        self.ssh_id = ssh_id
        self.ssh_pwd = ssh_pwd
        self.enable = enable

    def set_host(self, hostname):
        self.hostname = hostname

    def set_port(self, port):
        self.ssh_port = port

    def set_id(self, id):
        self.ssh_id = id

    def set_pwd(self, pwd):
        self.ssh_pwd = pwd

    def set_enable(self, enable):
        self.enable = enable

