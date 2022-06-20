import shutil
 
principal = "/home/jovyan/work/AI/mnist.ipynb"
 
destino = "/home/jovyan/work/mnist.ipynb"
 
try:
    shutil.copy(principal, destino)
    print("Arquivo copiado com sucesso.")
 
except shutil.SameFileError:
    print("Algum erro no caminho.")
 
except PermissionError:
    print("Permissão negada.")
 
except:
    print("Erro não conhecido.")