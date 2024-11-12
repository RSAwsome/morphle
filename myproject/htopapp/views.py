from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    name = "Ramsai Achanta"
    # Use an alternative way to get the username, handling cases where "USER" is not set
    username = os.environ.get("USER", "default_user")
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.check_output("top -bn1", shell=True).decode('utf-8')
    
    response = f"<h1>{name}</h1><p>Username: {username}</p><p>Server Time: {server_time}</p><pre>{top_output}</pre>"
    return HttpResponse(response)