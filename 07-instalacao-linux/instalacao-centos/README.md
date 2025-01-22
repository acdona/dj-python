# Instalação do CentOS 10 Stream 2025 (22/01/2025)
## Download -> [CentOS 10 Stream](https://www.centos.org/download/)
### Escolher a versão w86_64
![Imagem1:](./images/1.png)

### A instação será feita em uma máquina virtual VMWare versão 17.6
### Para instalação direta em um computador dedicado:
- Dar o boot por um pendrive com a imagem .ISO baixada
- Executar os mesmos passos de instação

## Criando a máquina virtual no VMWare:
- Clique em Create a New Virtual Machine
- Ou File, New Virtual Machine... ou Ctrl+N

![Imagem3:](./images/2.png)


- Escolha a opção Typical e clique Next >

![Imagem3:](./images/3.png)

- Clique em 'Installer disc image file (iso):' 
- Clique no botão'Browse...' 
- Selecione a .ISO baixada
- Clique em Next >

![Imagem4:](./images/4.png)


- Escolha o nome e caminho para salvar a máquina virtual
- Clique em Next >

![Imagem5:](./images/5.png)

- Na tela seguinte mantenha as configurações por padrão
- Clique Next >


![Imagem6:](./images/6.png)

- Na tela seguinte clique em 'Customize Hardware'

![Imagem7:](./images/7.png)

- Em Memory, coloque 4 GB

![Imagem8:](./images/8.png)

- Em processors, coloque 2 para Number of processors

![Imagem9:](./images/9.png)

- Em 'Network Adapter' mude para 'Custom' e selecione a rede virtual
    - Isso fará que a máquina virtual tenha um IP próprio.
- Clique em close para finalizar

![Imagem10:](./images/10.png)

- Desmarque a opção Power on this...
- Confirme as informações e clique em 'Finish'
![Imagem11:](./images/11.png)

- Máquina Virtual criada com sucesso
- Clicar em 'Power on this virtual machine
![Imagem12:](./images/12.png)

### As informações a partir daqui, são iguais para instalação na máquina virtual ou em um computador comum

- Será dado o boot e escolha a primeira opção 'Instal CentOS Stream 10'

![Imagem13:](./images/13.png)

- Escolha o idioma e clique em 'Continuar'

![Imagem14:](./images/14.png)

## Abrirá a página de resumo da instalação

![Imagem15:](./images/15.png)

### Em SISTEMA clique em 'Destino da Instação'

![Imagem16:](./images/16.png)

- Clique para selecionar o disco padrão
- Clique em 'Pronto'

![Imagem17:](./images/17.png)

- Clique em 'Criação de usuário'

![Imagem18:](./images/18.png)

- Crie um novo usuário e senha
- Caso a senha senha fraca, precisará dar 2 cliques em 'Pronto'

![Imagem19:](./images/19.png)

- Clique em 'Seleção de programas'

![Imagem20:](./images/20.png)

- Clique na opção 'Server' (Apenas o server será instalado)
- Clique em 'Pronto'

![Imagem21:](./images/21.png)

- Clique em 'Iniciar instação'

![Imagem22:](./images/22.png)

- Clique em 'Reiniciar o sistema'

![Imagem23:](./images/23.png)

### O sistema será reinicializado

- Digite o login com o usuário cadastrado, no meu caso "acdona"
- Digite a senha '1234' (ela não aparece na tela)

![Imagem24:](./images/24.png)


### Digite na linha de comando:
```bash
systemctl enable --now cockpit.socket
```

### Para fechar o servidor, digite na linha de comando

```bash
sudo shutdown now
```

### Inicie novamente a máquina virtual e anote o IP mostrado na tela

### Agora abra o navegador e digite o IP mostrado no meu caso (https://192.168.15.6:9090/)

### Caso aparece a mensagem de 'Sua conexão não é particular' clique em "Avanaçdas"

![Imagem25:](./images/25.png)

#### Clique em "Ir para..."

![Imagem26:](./images/26.png)

### Digite usuário e senha: (meu caso, acdona 1234)

![Imagem27:](./images/27.png)

### Acesso ao Painel Administrativo do Servidor

![Imagem28:](./images/28.png)

## Processo de instação concluído com êxito.
### Para desligar o servidor, quando preciso, clicar em Reiniciar -> Desligar

