# 🏭 Implementação do Padrão Factory nos Controllers

## 📌 FEITO
Refatoramento dos controllers `ContactController` e `LeadController` utilizando o **Padrão Factory** para:
- Centralizar a criação de objetos
- Encapsular regras de validação
- Promover código mais limpo e manutenível

## 🧩 O que foi Implementado

### 🏗️ Factories Criadas
| Arquivo               | Classe          | Responsabilidade                          |
|-----------------------|-----------------|------------------------------------------|
| `factories/contact_factory.py` | `ContactFactory` | Cria e valida objetos `Contact`          |
| `factories/lead_factory.py`    | `LeadFactory`    | Cria e valida objetos `Lead`             |

### 🔄 Métodos Refatorados
| Controller           | Método Refatorado | Mudança Principal                        |
|----------------------|-------------------|------------------------------------------|
| `ContactController`  | `add_contact()`   | Usa `ContactFactory.create_contact()`    |
| `LeadController`     | `add_lead()`      | Usa `LeadFactory.create_lead()`          |

## 💎 Benefícios


+ ✅ Desacoplamento: Controllers não conhecem detalhes de criação de objetos
+ ✅ Single Responsibility: Validações centralizadas nas factories
+ ✅ Flexibilidade: Fácil adição de novos tipos de objetos
+ ✅ Manutenção: Mudanças afetam apenas um ponto do código


.........
# 🎛️ Implementação do Padrão Command nos Controllers

## 📌 Status: **Concluído**

Refatoramos o `SalesPipelineController` utilizando o **Padrão Command** com os seguintes objetivos:

- ✅ Desacoplar ações da interface  
- ✅ Flexibilizar a execução de operações  
- ✅ Permitir extensão sem modificar o controlador principal  

---

## 🧩 O que foi Implementado

### ⚙️ Comandos Criados

| Arquivo                          | Classe                   | Responsabilidade                                |
|----------------------------------|---------------------------|-------------------------------------------------|
| `commands/add_opportunity.py`    | `AddOpportunityCommand`   | Encapsula lógica de adição de oportunidades     |
| `commands/list_opportunities.py` | `ListOpportunitiesCommand`| Gerencia listagem de oportunidades              |
| `commands/update_stage.py`       | `UpdateStageCommand`      | Controla atualização de estágios                |
| `commands/remove_opportunity.py` | `RemoveOpportunityCommand`| Trata remoção de oportunidades                  |

---

### 🔄 Controller Refatorado

| Arquivo                      | Mudança Principal                          |
|------------------------------|--------------------------------------------|
| `sales_pipeline_controller.py` | Transformado em **invocador de comandos** |

---

## 💎 Benefícios

- 🚀 **Desacoplamento**: A camada de view não conhece a implementação das ações  
- 🧩 **Extensibilidade**: Novos comandos podem ser adicionados sem modificar o controller  
- 🔄 **Reusabilidade**: Comandos reutilizáveis em diferentes contextos  
- 🧪 **Testabilidade**: Cada comando pode ser testado isoladamente  
- ⏱️ **Flexibilidade**: Suporte futuro para filas, undo/redo e operações assíncronas  

---

## 🛠️ Como Usar

python
controller.execute_command('add')  # Executa AddOpportunityCommand

...........................................................

# MVC CRM System - Customer Relationship Management


## 📋 Description
A comprehensive CRM (Customer Relationship Management) system developed in Python using the MVC (Model-View-Controller) architecture. This system offers complete functionality for managing customer relationships, sales opportunities, marketing campaigns, and business analytics.

## 🚀 Implemented Features
1. **Contact Management** - Store and manage customer contact information
2. **Sales Pipeline Management** - Track and manage sales opportunities through different stages
3. **Activity Tracking** - Record interactions with customers (calls, meetings, emails)
4. **Task & Appointment Scheduling** - Organize tasks and appointments with customers
5. **Email Template & Campaign Management** - Create and manage email campaigns
6. **Lead Management** - Track potential leads and their conversion journey
7. **Customizable Dashboards** - Create personalized views of important metrics
8. **Reporting & Analytics** - Generate insights on sales, leads, and pipeline
9. **Document Management** - Store and organize sales and marketing documents
10. **Mobile Access** - Access the CRM via terminal on mobile devices

## 🏗️ Architecture
This project follows the Model-View-Controller (MVC) architectural pattern:

### Models
Models represent the data structures and business logic of the application:
- Entity classes (Contact, Lead, SalesOpportunity, etc.)
- Repository classes that manage collections of entities

### Views
Views handle all user interactions:
- Display menus and data
- Collect user input
- Present results and messages

### Controllers
Controllers coordinate between models and views:
- Process user input from views
- Manipulate data through models
- Return results to views

## 📦 Project Structure
crm_system/
│
├── models/          # Data structures and repositories
│   ├── init.py
│   ├── contact.py
│   ├── contact_repository.py
│   └── ...
│
├── views/           # User interface components
│   ├── init.py
│   ├── main_view.py
│   ├── contact_view.py
│   └── ...
│
├── controllers/     # Business logic
│   ├── init.py
│   ├── contact_controller.py
│   └── ...
│
├── utils/           # Utilities and helpers
│   ├── init.py
│   ├── validators.py
│   └── ...
│
└── app.py           # Application entry point

## 🔧 Core Components

### Contact Management
- Create, view, update, and delete contact information
- Track contact history and interactions

### Sales Pipeline
- Create sales opportunities linked to contacts
- Track deals through customizable stages
- Calculate sales metrics and forecasts

### Activity Tracking
- Record all customer interactions
- Track call logs, meeting notes, and email exchanges

### Appointment Scheduling
- Create and manage appointments with customers
- Track appointment status (Scheduled, Completed, Cancelled)

### Email Marketing
- Create reusable email templates with variables
- Build targeted email campaigns
- Track campaign performance metrics

### Lead Management
- Capture and qualify leads
- Track lead progress through the sales funnel
- Record notes and score lead potential

### Dashboard System
- Create customizable dashboards
- Add/remove widgets based on user preferences
- Real-time updates of key metrics

### Reporting & Analytics
- Generate comprehensive reports on sales performance
- Analyze lead conversion rates
- Track pipeline health metrics

### Document Management
- Store important documents related to contacts and opportunities
- Manage document versions
- Categorize documents by type (proposals, contracts, etc.)

## 🛠️ Technologies
- Python 3.x
- Object-Oriented Programming
- MVC Architecture
- Repository Pattern
- Data Structures (Dictionaries, Lists)
- Terminal-based User Interface
- Mobile Accessibility (iSH on iOS)

## 🚀 How to Run
1. Clone the repository
2. Navigate to the project directory
3. Run `python app.py`
4. Follow the on-screen menu options to navigate the system

## 🏆 Project Highlights
- Clean code organization with MVC architecture
- Strong separation of concerns
- Extensible design that can be easily enhanced
- Terminal-based interface works on both desktop and mobile devices
- Comprehensive CRM functionality in a single application
