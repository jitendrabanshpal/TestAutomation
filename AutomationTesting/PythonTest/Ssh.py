'''
Created on 18 Mar 2019

@author: Jitendra Banshpal
'''
import paramiko
import socket

import psycopg2
class Point:
    def __init__(self,host,username,password,port):
        self.host = "IP"
        self.username = "User1"
        self.password = "Password"
        self.port = "22"

    def connect(self):
        try:
            # Paramiko.SSHClient can be used to make connections to the remote server and transfer files
            print("Establishing ssh connection")
            self.client = paramiko.SSHClient()
            # Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the server
            self.client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password,
                                timeout=100000, allow_agent=False, look_for_keys=False)
            print("Connected to the server", self.host)
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
            result_flag = False
        except socket.timeout as e:
            print("Connection timed out")
            print(e)
            result_flag = False
        except Exception as e:
            print("Exception in connecting to the server")
            print("PYTHON SAYS:", e)
            result_flag = False
            self.client.close()
        else:
            result_flag = True

        return result_flag

p= Point("IP", "User1", "Password", "22")
p.connect()
