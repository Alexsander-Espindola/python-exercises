# python-exercises
Comandos para começar um aplicação em Python
  - python3 para iniciar um terminal interativo em python


https://app.betrybe.com/course/real-life-engineer/python/

Pyenv (opcional)
  - “O Pyenv permite alternar facilmente entre várias versões do Python. É simples, discreto e segue a tradição UNIX de ferramentas de propósito único que fazem uma coisa bem.”

  1- Baixe e instale o pyenv:
      curl https://pyenv.run | bash

  2- Reinicie seu shell para que as mudanças tenham efeito:
      exec $SHELL

  3- Certifique-se de que as seguintes linhas estão no seu arquivo de configuração .bashrc, caso não estejam, faça a inclusão no final do arquivo:
      export PATH="$HOME/.pyenv/bin:$PATH"
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"

  Como usar
    1- Para listar tudo que se pode instalar com o pyenv , faça:
      pyenv install -l

    2- Instale uma versão do Python, por exemplo, 3.9.1
      pyenv install 3.9.1

    3- Faça com que a versão que você acabou de instalar, seja a versão global de seu sistema
      pyenv global 3.9.1

    4- Verifique se essa versão foi setada
      pyenv global

    5- Liste todas as versões que já foram baixadas
      pyenv versions

Venv
  Como instalar
    Versões atuais do Ubuntu já vem com python 3 instalado. Para as mais antigas utilize o comando:
    - sudo apt install python3-venv

  Vamos verificar se deu tudo certo?
    Em um terminal digite:
    - python3 -m venv -h

  A saída deverá ser similar a apresentada abaixo:
    usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
                [--upgrade] [--without-pip] [--prompt PROMPT]
                ENV_DIR [ENV_DIR ...]
    Creates virtual Python environments in one or more target directories.

    positional arguments:
      ENV_DIR               A directory to create the environment in.

    optional arguments:
    ...
  
  Iniciando o venv:
    python3 -m venv .venv
    source .venv/bin/activate
  Intalando dependências no venv:
    pip install flake8 black

Flake8
  Como instalar
  O pacote flake8 pode ser instalado utilizando utilizando a ferramenta pip vista anteriormente. Vamos utilizar sudo neste caso para garantir que ela esteja disponível para todos os usuários do sistema operacional. Digite o comando abaixo:
    - sudo python3 -m pip install flake8

  Vamos verificar se deu tudo certo?
  Digite o comando:
    - python3 -m flake8 --version
  A saída deverá ser similar a apresentada abaixo:
    - 3.8.4 (mccabe: 0.6.1, pycodestyle: 2.6.0, pyflakes: 2.2.0)

Black
  Como instalar
  O pacote black pode ser instalado utilizando utilizando a ferramenta pip vista anteriormente. Vamos utilizar sudo neste caso para garantir que ela esteja disponível para todos os usuários do sistema operacional. Digite o comando abaixo:
    - sudo python3 -m pip install black
  Vamos verificar se deu tudo certo?
    - python3 -m black --version
  A saída deverá ser similar a apresentada abaixo:
    - __main__.py, version 20.8b1

VSCode(Python)
  O que é?
    O VSCode é um editor de texto e possui uma excelente extensão para Python que pode ser instalada através da marketplace .

  Para que serve?
    O plugin de Python para VSCode fornece auto-complete , integração com os linters vistos anteriormente, também é uma ferramenta para depuração de código.

  Como instalar
    Abra o VS Code Quick Open (Ctrl+P) , cole o comando a seguir e pressione enter .
    - ext install ms-python.python

  Após instalar a extensão, digite ctrl + shift + p , vá em Preferences: Open Settings (JSON) e acrescente as seguintes configurações.
    // ...
        "python.linting.enabled": true,
        "python.linting.flake8Enabled": true,
        "python.formatting.blackArgs": [
            "-l 79"
        ],
        "python.formatting.provider": "black",
    // ...

  Vamos verificar se deu tudo certo?
    Abra um arquivo com extensão .py no VSCode e digite o código lista = [1,2,3] . Salve o arquivo e um aviso de erro deve acontecer.
    Passando o mouse sobre a linha veremos que o erro é: missing whitespace after ','flake8(E231) .
    Para corrigir e testar se o nosso formatador está funcionando corretamente, digite ctrl + shift + i . Após salvar novamente o erro deve ter desaparecido. Caso isto não aconteça certifique que tenha feitos os passos anteriormente para instalação do flake8 e black .