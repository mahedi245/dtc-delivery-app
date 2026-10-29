import urllib.request
import urllib.error
import os

username = 'DTCmahedi'
token = 'aab8794a30cbbaec1baeb51115ab7babcea15ff9'
domain = 'DTCmahedi.pythonanywhere.com'

files_to_upload = [
    ('D:/Zahir/DeliveryApp/app.py', f'/home/{username}/mysite/app.py'),
    ('D:/Zahir/DeliveryApp/templates/index.html', f'/home/{username}/mysite/templates/index.html'),
    ('D:/Zahir/DeliveryApp/templates/edit.html', f'/home/{username}/mysite/templates/edit.html'),
]

def upload_file(local_path, remote_path):
    url = f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{remote_path}'
    boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
    with open(local_path, 'rb') as f:
        file_content = f.read()
    filename = os.path.basename(local_path)
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="content"; filename="{filename}"\r\n'
        f'Content-Type: application/octet-stream\r\n\r\n'
    ).encode('utf-8') + file_content + f'\r\n--{boundary}--\r\n'.encode('utf-8')

    req = urllib.request.Request(url, data=body, method='POST')
    req.add_header('Authorization', f'Token {token}')
    req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
    try:
        with urllib.request.urlopen(req) as resp:
            print(f'Uploaded: {remote_path} (Status: {resp.status})')
    except Exception as e:
        print(f'Error uploading {remote_path}: {e}')

for local, remote in files_to_upload:
    upload_file(local, remote)

# Reload Web App
reload_url = f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'
req_reload = urllib.request.Request(reload_url, data=b'', method='POST')
req_reload.add_header('Authorization', f'Token {token}')
try:
    with urllib.request.urlopen(req_reload) as resp:
        print(f'Webapp Reloaded Successfully! Status: {resp.status}')
except Exception as e:
    print(f'Reload Error: {e}')

# Automatically deploy to Vercel production (updating production.dhakatimbercomplex.com & vercel app)
import subprocess
print("\nDeploying to Vercel production...")
try:
    subprocess.run(['npx.cmd', 'vercel', '--prod', '--yes'], cwd='D:/Zahir/DeliveryApp', check=True)
    print("Vercel & Custom Subdomain Deployment Successful!")
except Exception as e:
    print(f"Vercel Deployment Error: {e}")
