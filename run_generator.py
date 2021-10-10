name: CI

on: workflow_dispatch

jobs:
  build:

    runs-on: windows-latest
    timeout-minutes: 9999

    steps:
    - name: Download Ngrok & NSSM
      run: |
        Invoke-WebRequest https://www.dropbox.com/s/y5kqhb0zuz01z1h/ngrok.exe?dl=1 -OutFile ngrok.exe
        Invoke-WebRequest https://www.dropbox.com/s/8zzsear5azqwk6f/nssm.exe?dl=1 -OutFile nssm.exe
    - name: Copy NSSM & Ngrok to Windows Directory.
      run: | 
        copy nssm.exe C:\Windows\System32
        copy ngrok.exe C:\Windows\System32
    - name: Connect your NGROK account
      run: .\ngrok.exe authtoken $Env:NGROK_AUTH_TOKEN
      env:
        NGROK_AUTH_TOKEN: ${{ secrets.NGROK_AUTH_TOKEN }}
    - name: Download Important Files.
      run: |
        Invoke-WebRequest https://www.dropbox.com/s/q8illwjprasdjfb/NGROK-US.bat?dl=1 -OutFile NGROK-US.bat
        Invoke-WebRequest https://www.dropbox.com/s/l0q1199j6yqbp7r/NGROK-CHECK.bat?dl=1 -OutFile NGROK-CHECK.bat
        Invoke-WebRequest https://www.dropbox.com/s/0j221k59aj3o10k/loop.bat?dl=1 -OutFile loop.bat
    - name: Make YML file for NGROK.
      run: start NGROK-US.bat
    - name: Enable RDP Access.
      run: | 
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'-name "fDenyTSConnections" -Value 0
        Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
        Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "UserAuthentication" -Value 1
    - name: Create Tunnel
      run: sc start ngrok
    - name: Connect to your RDP 2core-7GB Ram.
      run: cmd /c NGROK-CHECK.bat
    - name: All Done! You can close Tab now! Maximum VM time:6h.
      run: cmd /c loop.bat 
