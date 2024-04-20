from django.shortcuts import render, redirect
from django.views import View
import ftplib
import os
import schedule
import time
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from threading import Thread
import socket

class Integrations_View(View):
     
    template_name = 'pages/ADMIN/manage-integrations.html'

    def get(self, request):
         # Fetch the list of files from the FTP server
        ftp_files = self.get_ftp_files()
        context = {'ftp_files': ftp_files}
        return render(request, self.template_name, context)
        
    def get_ftp_files(self):
        ftp_files = []
        try:
            # Connect to the FTP server
            with ftplib.FTP() as ftp:
                ftp.connect(host="127.0.0.1", port=2121)
                ftp.login(user="testuser", passwd="testpassword")

                # Fetch the list of files from the server
                ftp_files = ftp.nlst()
        except (socket.timeout, ftplib.error_perm) as e:
            print("Error connecting to FTP server:", e)
        
        return ftp_files

   