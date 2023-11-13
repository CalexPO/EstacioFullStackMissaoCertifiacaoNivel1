Sobre o Projeto a Ser Desenvolvido 

Desenvolver uma aplicação para gerenciamento da Matriz SoD (que em inglês quer dizer “Segregation of Duties”), 
que tem como objetivo indicar os perfis de acesso conflitantes e que possam representar risco de fraude. 

Contextualização do Projeto 

Qualquer grande empresa precisa gerenciar eficientemente os perfis de acesso dos seus principais sistemas. Auditorias externas se preocupam muito com este assunto pois é comprovadamente uma das principais vulnerabilidades que propiciam fraudes financeiras. 
Perfil de acesso é o nome dado a um conjunto de acessos que um determinado usuário pode ter à um sistema. Um acesso é basicamente uma função disponível para uso no sistema, ou seja, um programa combinado com o que pode ser feito utilizando-se este programa. Exemplo: Um programa que permite cadastrar os dados de um funcionário dentro de um sistema de Recursos Humanos. Ao utilizar este programa, o usuário pode incluir novo funcionário, alterar dados, excluir ou somente consultar. Cada uma destas opções é considerada como um acesso. 
Sistemas mais sofisticados podem chegar até mesmo a definir quais campos podem ser visualizados ou inseridos/alterados. Por exemplo se este programa de cadastro de funcionário tiver o campo “salário”, pode-se definir que somente quem inclui funcionário e altera os seus dados podem ter acesso ao campo “salário”. Usuários que somente consultam os dados não teriam acessos as informações de salário. 
Com a criação no Brasil da Lei Geral de Proteção de Dados (LGPD), muitas informações pessoas (CPF, Endereço, Religião, ...) passaram a ser tratadas de forma mais rígida, logo muitos sistemas precisaram se adequar rapidamente e hoje é mais comum encontrarmos sistemas com uma gestão de perfis de acessos muito sofisticada, como por exemplo, incluindo-se a opção de mascaramento dos dados, ou seja, os dados pessoais são embaralhados em algumas telas do sistema de forma que ninguém consiga fazer um “print da tela” e vazar uma informação pessoal. 
Um usuário pode ter mais de um perfil de acesso por sistema (prática mais comum), pois as empresas preferem construir os perfis com base nas funcionalidades do sistema, agrupando-as por afinidade. Outras empresas preferem organizar os perfis de acordo com os cargos (prática menos comum) e neste caso um usuário passa a ter somente o perfil associado ao seu cargo. 

⚙️Descrição do Processo 

Normalmente o departamento de Controles Internos de uma empresa é a área responsável por analisar os perfis de acessos existentes em um sistema e definir se a combinação de perfis, para um mesmo usuário, pode apresentar algum conflito de interesse. Um conflito de interesse é quando o usuário pode se aproveitar dos acessos que possui para praticar uma fraude. 
Exemplo: Um mesmo usuário possui acesso ao cadastro da conta bancária de fornecedores mas também possui acesso de autorização para envio de pagamento de fornecedor para o banco. Com estes dois acessos o usuário pode alterar a conta bancária do fornecedor, para a sua conta pessoal, e processar o pagamento de uma nota fiscal deste mesmo fornecedor, fazendo com que o dinheiro vá para a sua conta pessoal. 
Os conflitos de interesse precisam ser analisados também entre os sistemas, pois o perfil de acesso que um usuário possui no sistema “A” pode conflitar com o perfil de acesso que este mesmo usuário possui no sistema “B”. 
A Matriz de SoD é exatamente o local onde o time de Controles Internos declara estes conflitos, indiciando quais perfis de acesso NÃO podem ser combinados para o mesmo usuário. 
A forma de conceder um perfil de acesso a um determinado usuário varia muito de empresa para empresa, dependendo do grau de sofisticação dos sistemas e ferramentas disponíveis. 
Existem empresas em que este processo é completamente automatizado, ou seja, o processo é suportado por uma ferramenta de workflow que coleta as aprovações necessárias, verifica a existência de algum conflito de interesse através da Matriz SoD e concede o perfil de acesso ao usuário de forma automática nos sistemas. 
Porém existem empresas em que este processo é feito de forma manual, onde a equipe de Gestão de Acesso, buscas as aprovações por email e verifica manualmente na Matriz de SoD a existência de conflito de interesse antes de conceder os acessos. 

# Criar uma máquina virtual (Windows)
> virtualenv venv

# Ativar Máquina Virtual (Windows)
> venv/Scripts/Activate

# Para instalar as dependencias "bibliotecas"
pip install -r requirements.txt

# Recriar banco
Tela do Menu > Settings > recriar banco

# Inicia tela Login
SENHA_ACESSO = '123'
USUARIO = 'admin'

# SENHA PARA ACESSO TELAS PERFIL USUARIO E MATRIZ DE CONFLITO
SENHA = '123' 