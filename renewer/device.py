class DeviceInfo:
    def __init__(self):
        self.hostname = None
        self.ssh_port = None
        self.ssh_id = None
        self.ssh_pwd = None
        self.enable = None

    def set_host(self, hostname):
        self.hostname = hostname

    def get_host(self):
        return self.hostname

    def set_port(self, port):
        self.ssh_port = port

    def get_port(self):
        return self.ssh_port

    def set_id(self, id):
        self.ssh_id = id

    def get_id(self):
        return self.ssh_id

    def set_pwd(self, pwd):
        self.ssh_pwd = pwd

    def get_pwd(self):
        return self.ssh_pwd

    def set_enable(self, enable):
        self.enable = enable

    def get_enable(self):
        return self.enable
