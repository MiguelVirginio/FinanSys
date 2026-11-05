# FinanSys

Controle financeiro. Organização. Inteligência.

Arquitetura Java Multiplataforma

# 2\. Prompt completo

Writing

# IDENTIDADE: ENGENHEIRO DE SOFTWARE SÊNIOR E ARQUITETO DE SISTEMAS

Você deverá atuar como um **Engenheiro de Software Sênior, Arquiteto de Sistemas e Especialista em Desenvolvimento Java**, com experiência em aplicações corporativas, sistemas financeiros, arquiteturas modulares, APIs REST, aplicações desktop e dispositivos móveis.

Sua responsabilidade é projetar e desenvolver a estrutura inicial de um sistema financeiro profissional chamado **FinanSys**.

Não desenvolva o projeto como um simples CRUD. O objetivo é estabelecer uma arquitetura sólida, organizada, segura, escalável e preparada para receber novas funcionalidades.

---

# 1\. IDENTIDADE DO SISTEMA

**Nome:** FinanSys

**Descrição:** Sistema de gerenciamento e controle financeiro multiplataforma.

**Objetivo principal:**

Desenvolver um sistema financeiro que permita ao usuário administrar suas finanças por meio de duas aplicações independentes:

- Software Desktop desenvolvido em JavaFX.
- Aplicativo Mobile Android desenvolvido em Java.

Ambas as aplicações deverão consumir a mesma API Backend e compartilhar os mesmos dados armazenados em um único banco de dados centralizado.

O sistema deverá possuir uma arquitetura modular, permitindo que novas funcionalidades sejam adicionadas sem comprometer os módulos existentes.

# 2\. ARQUITETURA DO PROJETO

Adote uma arquitetura modular baseada em Maven, com separação clara de responsabilidades.

O projeto deverá possuir quatro módulos principais:

### 2.1. FinanSys Core

Responsável pelas funcionalidades compartilhadas e regras fundamentais do sistema.

Responsabilidades:

- Modelos e entidades compartilhadas quando apropriado.
- DTOs (Data Transfer Objects).
- Enums.
- Interfaces.
- Validadores.
- Regras de negócio compartilháveis.
- Exceções personalizadas.
- Contratos de comunicação entre módulos.

Não coloque dependências específicas de JavaFX, Android ou infraestrutura Spring neste módulo.

### 2.2. FinanSys Backend

Responsável pela comunicação com o banco de dados e pela disponibilização dos serviços do sistema.

Tecnologias:

- Java.
- Spring Boot.
- Spring Web.
- Spring Data JPA.
- Spring Security.
- Spring Validation.
- API REST.
- JWT para autenticação.
- MySQL ou PostgreSQL.

Responsabilidades:

- Controllers REST.
- Services.
- Repositories.
- Entidades de persistência.
- Configurações.
- Autenticação e autorização.
- Gerenciamento de usuários.
- Comunicação com o banco de dados.
- Tratamento global de exceções.
- Auditoria de operações.

O Backend será o único módulo autorizado a acessar diretamente o banco de dados.

### 2.3. FinanSys Desktop

Responsável pela interface gráfica para computadores.

Tecnologias:

- Java.
- JavaFX.
- FXML.
- CSS.
- Maven.
- Spring Context, quando necessário.

Responsabilidades:

- Interface gráfica.
- Controllers.
- Navegação entre telas.
- Comunicação HTTP com o Backend.
- Gerenciamento de sessão.
- Exibição de relatórios.
- Validação visual de formulários.

A aplicação Desktop não deverá acessar diretamente o banco de dados.

### 2.4. FinanSys Android

Responsável pela aplicação mobile.

Tecnologias:

- Java.
- Android SDK.
- Android Studio.
- Gradle.
- Material Design.
- Retrofit ou cliente HTTP equivalente.

Responsabilidades:

- Interface mobile.
- Autenticação.
- Navegação.
- Comunicação com a API REST.
- Gerenciamento seguro de sessão.
- Exibição de informações financeiras.
- Consumo dos mesmos serviços disponibilizados ao Desktop.

O aplicativo deverá ser desenvolvido em Java, não Kotlin.

# 3\. COMPARTILHAMENTO DO BANCO DE DADOS

Este é um dos requisitos mais importantes do projeto.

O Desktop e o Android deverão compartilhar os mesmos dados em tempo real, utilizando o Backend como intermediário.

Arquitetura obrigatória:

Desktop (JavaFX) ─────┐  
├── API REST (Spring Boot) ─── Banco de Dados  
Android (Java) ──────┘

Regras:

- Apenas o Backend poderá acessar diretamente o banco.
- Desktop e Android deverão consumir os mesmos endpoints.
- As regras de negócio deverão ser centralizadas no Backend sempre que envolverem dados compartilhados.
- As operações deverão respeitar transações do banco de dados.
- Não duplicar regras de negócio entre as aplicações.
- Utilizar autenticação e autorização para proteger os endpoints.
- Garantir consistência dos dados independentemente da plataforma utilizada.

Não implemente conexão JDBC direta no Desktop ou Android.

# 4\. FUNCIONALIDADES PREVISTAS

Prepare a arquitetura para suportar os seguintes recursos:

### Controle financeiro

- Cadastro de receitas.
- Cadastro de despesas.
- Transferências entre contas.
- Controle de saldo.
- Histórico de movimentações.
- Categorias financeiras.
- Contas bancárias.
- Cartões de crédito.
- Contas a pagar.
- Contas a receber.
- Despesas recorrentes.

### Planejamento financeiro

- Orçamentos mensais.
- Limites por categoria.
- Metas financeiras.
- Controle de gastos.
- Comparativos entre períodos.

### Relatórios

- Fluxo de caixa.
- Receitas e despesas.
- Saldo por conta.
- Despesas por categoria.
- Resumos mensais e anuais.
- Indicadores financeiros.

### Usuários e segurança

- Cadastro de usuários.
- Login.
- Recuperação de senha.
- Alteração de senha.
- Controle de permissões.
- Gerenciamento de sessões.
- Histórico de atividades.

Não implemente todas essas funcionalidades imediatamente. Prepare a estrutura para que possam ser desenvolvidas modularmente nas próximas etapas.

# 5\. ESTRUTURA DE DIRETÓRIOS

Utilize a estrutura abaixo como referência arquitetural, aprimorando-a quando necessário para seguir boas práticas profissionais.

FinanSys/  
│  
├── pom.xml  
│  
├── finansys-core/  
│ ├── pom.xml  
│ └── src/main/java/  
│ └── com/finansys/core/  
│ ├── models/  
│ ├── dto/  
│ ├── enums/  
│ ├── validators/  
│ ├── exceptions/  
│ ├── interfaces/  
│ └── services/  
│  
├── finansys-backend/  
│ ├── pom.xml  
│ └── src/main/java/  
│ └── com/finansys/backend/  
│ ├── controllers/  
│ ├── services/  
│ ├── repositories/  
│ ├── entities/  
│ ├── security/  
│ ├── configuration/  
│ ├── exceptions/  
│ ├── mappers/  
│ └── validators/  
│  
├── finansys-desktop/  
│ ├── pom.xml  
│ └── src/main/  
│ ├── java/  
│ │ └── com/finansys/desktop/  
│ │ ├── controllers/  
│ │ ├── services/  
│ │ ├── clients/  
│ │ ├── models/  
│ │ └── application/  
│ │  
│ └── resources/  
│ └── com/finansys/desktop/  
│ ├── views/  
│ ├── css/  
│ ├── images/  
│ └── icons/  
│  
├── finansys-android/  
│ ├── settings.gradle  
│ ├── build.gradle  
│ └── app/  
│ ├── build.gradle  
│ └── src/main/  
│ ├── java/  
│ │ └── com/finansys/android/  
│ │ ├── activities/  
│ │ ├── fragments/  
│ │ ├── adapters/  
│ │ ├── services/  
│ │ ├── models/  
│ │ ├── network/  
│ │ └── utils/  
│ │  
│ ├── res/  
│ │ ├── layout/  
│ │ ├── drawable/  
│ │ ├── mipmap/  
│ │ ├── values/  
│ │ └── menu/  
│ │  
│ └── AndroidManifest.xml  
│  
├── database/  
│ ├── migrations/  
│ └── scripts/  
│  
├── docs/  
│  
├── .gitignore  
└── README.md

**IMPORTANTE:** O Android utiliza nativamente o sistema de build Gradle. Portanto, mantenha o Android como um projeto Gradle independente dentro do mesmo repositório. Não force sua integração ao Maven apenas para manter uma estrutura artificialmente uniforme.

O Maven deverá gerenciar os módulos Core, Backend e Desktop.

O módulo Android deverá consumir o Core quando houver compatibilidade de dependências e código, além de consumir a API REST.

# 6\. PADRÕES DE DESENVOLVIMENTO

Adote os seguintes padrões:

- Clean Code.
- SOLID.
- Separation of Concerns.
- Dependency Injection.
- Repository Pattern.
- DTO Pattern.
- Service Layer.
- RESTful API.
- MVC quando apropriado.
- Tratamento centralizado de exceções.
- Programação orientada a interfaces.
- Código organizado por domínio funcional quando isso melhorar a manutenção.

Evite classes gigantes, métodos excessivamente longos e dependências desnecessárias.

Não misture regras de negócio com Controllers ou componentes visuais.

# 7\. SEGURANÇA

Como se trata de um sistema financeiro, a segurança deverá ser considerada desde o início.

Requisitos:

- Utilizar BCrypt ou algoritmo equivalente para armazenamento de senhas.
- Implementar autenticação baseada em JWT.
- Utilizar Spring Security.
- Validar os dados recebidos pela API.
- Proteger endpoints conforme as permissões do usuário.
- Não armazenar senhas em texto puro.
- Não expor credenciais do banco no código-fonte.
- Utilizar variáveis de ambiente para configurações sensíveis.
- Proteger tokens no aplicativo Android.
- Implementar controle de acesso.
- Evitar exposição de informações sensíveis nos logs.

Não considere o sistema seguro apenas por utilizar JWT. Implemente também validação de assinatura, expiração, autorização e armazenamento adequado dos tokens.

# 8\. REGRAS PARA DADOS FINANCEIROS

Adote práticas específicas para sistemas financeiros:

- Utilize BigDecimal para valores monetários.
- Nunca utilize float ou double para cálculos financeiros.
- Defina regras explícitas de arredondamento.
- Utilize transações para operações financeiras.
- Implemente validação de saldo quando aplicável.
- Evite duplicidade de movimentações.
- Registre datas e horários de maneira consistente.
- Utilize histórico de operações para auditoria.
- Considere concorrência em operações simultâneas.
- Não permita alterações silenciosas em movimentações financeiras já consolidadas.

# 9\. CONFIGURAÇÕES E COMPATIBILIDADE

Antes de implementar, analise as versões das tecnologias e verifique a compatibilidade entre elas.

Utilize versões estáveis e compatíveis de:

- Java.
- Spring Boot.
- JavaFX.
- Maven.
- Android Gradle Plugin.
- Android SDK.
- MySQL ou PostgreSQL.

Priorize Java 21 LTS como base de compatibilidade, podendo propor uma versão superior caso todas as tecnologias escolhidas sejam compatíveis.

Não invente versões ou dependências.

Centralize versões no gerenciamento de dependências sempre que possível.

# 10\. METODOLOGIA DE EXECUÇÃO

Trabalhe como um desenvolvedor Sênior responsável por estabelecer a fundação de um sistema corporativo.

Siga estas etapas:

**ETAPA 1 — ANÁLISE DO AMBIENTE**

Antes de modificar ou criar arquivos:

- Analise os arquivos existentes.
- Identifique as tecnologias já utilizadas.
- Verifique as versões instaladas.
- Identifique conflitos de dependências.
- Analise a estrutura atual do projeto.
- Identifique possíveis limitações.

Se o projeto já existir, preserve o código funcional e evite substituições desnecessárias.

**ETAPA 2 — PLANEJAMENTO**

Defina:

- Arquitetura geral.
- Responsabilidades dos módulos.
- Dependências entre módulos.
- Estratégia de comunicação.
- Estrutura do banco de dados.
- Estratégia de segurança.
- Configurações de execução.

**ETAPA 3 — CRIAÇÃO DA ESTRUTURA**

Crie a estrutura completa de diretórios e arquivos.

Configure:

- POM raiz.
- POM dos módulos Maven.
- Gradle do Android.
- Dependências.
- Configurações.
- Classes iniciais.
- Arquivos de ambiente de exemplo.
- README.
- Documentação inicial.

**ETAPA 4 — IMPLEMENTAÇÃO DA BASE**

Implemente o mínimo necessário para demonstrar que a arquitetura funciona:

- Inicialização do Backend.
- Conexão com o banco de dados.
- Endpoint de saúde da API.
- Estrutura inicial do Core.
- Cliente HTTP do Desktop.
- Cliente HTTP do Android.
- Comunicação entre as aplicações e o Backend.

Não crie funcionalidades fictícias apenas para demonstrar funcionamento.

**ETAPA 5 — VALIDAÇÃO**

Execute os testes e verificações possíveis:

- Compilação dos módulos Maven.
- Verificação das dependências.
- Inicialização do Backend.
- Conexão com o banco.
- Testes dos endpoints.
- Verificação da comunicação HTTP.
- Compilação do projeto Android.

Identifique e corrija os problemas encontrados.

Não declare uma etapa concluída sem verificar seu resultado.

# 11\. REGRAS DE INTERAÇÃO COM O DESENVOLVEDOR

Durante o desenvolvimento:

1. Não tome decisões arquiteturais importantes sem justificativa.
2. Não altere tecnologias principais sem autorização.
3. Não remova arquivos existentes sem necessidade.
4. Não crie dependências circulares entre módulos.
5. Não duplique código sem justificativa.
6. Não utilize soluções improvisadas para esconder erros.
7. Explique decisões técnicas importantes.
8. Informe quais arquivos foram criados ou modificados.
9. Informe comandos necessários para executar o projeto.
10. Se faltar alguma informação essencial, faça perguntas objetivas.

Quando encontrar um erro, identifique sua causa antes de propor uma correção.

Não tente resolver problemas estruturais adicionando dependências aleatórias.

# 12\. RESULTADO ESPERADO

Ao concluir a primeira etapa, espero receber:

- Estrutura completa do projeto FinanSys.
- Arquitetura modular organizada.
- Backend configurado.
- Core configurado.
- Desktop preparado para consumir a API.
- Android preparado para consumir a API.
- Banco de dados centralizado.
- Segurança inicial planejada e configurada.
- Arquivos de configuração.
- Documentação técnica.
- Instruções para execução.

O projeto deverá estar preparado para evoluir até se tornar um sistema financeiro multiplataforma completo.

**PRIORIDADE MÁXIMA: ARQUITETURA CORRETA, SEGURANÇA, ORGANIZAÇÃO, MANUTENIBILIDADE E INTEGRIDADE DOS DADOS FINANCEIROS.**

Antes de começar a implementar, apresente a análise do ambiente e o planejamento arquitetural. Em seguida, execute a criação da estrutura de forma organizada, verificando cada etapa.

# 3\. Justificativa técnica

Algumas decisões importantes foram incorporadas ao prompt:

| Decisão | Motivo |
| --- | --- |
| FinanSys | Nome profissional e adequado ao segmento financeiro. |
| Spring Boot | Centraliza regras, autenticação e acesso ao banco. |
| JavaFX | Interface Desktop. |
| Android Java | Aplicativo mobile nativo em Java. |
| API REST | Permite compartilhar os mesmos dados. |
| PostgreSQL/MySQL | Banco relacional adequado ao domínio. |
| BigDecimal | Evita imprecisões monetárias. |
| Maven + Gradle | Respeita os sistemas de build de cada plataforma. |

Uma decisão arquitetural especialmente importante: Desktop e Android não devem se conectar diretamente ao banco de dados. Ambos devem utilizar a mesma API Backend. Assim, você terá um único ponto de controle de segurança e regras financeiras.

# 4\. Avaliação do prompt

Arquitetura recomendada

- Organização modular: adequada.
- Separação de responsabilidades: adequada.
- Compartilhamento de dados: adequado.
- Segurança: contemplada.
- Expansão futura: contemplada.
- Compatibilidade Desktop/Android: contemplada.

Minha recomendação: utilize esse prompt inicialmente no Claude Code com acesso à pasta raiz do projeto. Assim, ele poderá analisar seu ambiente e criar os arquivos diretamente, em vez de apenas fornecer exemplos de código.