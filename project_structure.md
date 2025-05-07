# Vehicle Maintenance Shop Project Structure

## 1. Django Apps Required
- `clients` - Client management
- `vehiculess` - Vehicle management
- `chatbot` - Chatbot functionality
- `reparation` - Repair management
- `planning` - Appointment scheduling
- `authentication` (Django built-in)

## 2. Database Models

### clients/models.py
```python
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    adresse = models.TextField()
    date_inscription = models.DateTimeField(auto_now_add=True)
```

### vehiculess/models.py
```python
class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    plaque = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    derniere_maintenance = models.DateTimeField(null=True, blank=True)
```

### reparation/models.py
```python
class Reparation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    etat = models.CharField(max_length=50)  # En cours, Terminé, En attente
    mecanicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
```

### planning/models.py
```python
class RendezVous(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()
    status = models.CharField(max_length=50)  # Confirmé, En attente, Annulé
    description = models.TextField()
```

## 3. Views Structure

### Client Views (clients/views.py)
```python
# Authentication
def inscription(request)
def connexion(request)
def deconnexion(request)

# Profile Management
def profil(request)
def modifier_profil(request)

# Vehicle Management
def mes_vehicules(request)
def ajouter_vehicule(request)
def details_vehicule(request, pk)

# Appointments
def prendre_rendez_vous(request)
def mes_rendez_vous(request)
def annuler_rendez_vous(request, pk)
```

### Mechanic Views (reparation/views.py)
```python
def liste_vehicules(request)
def mettre_a_jour_reparation(request, pk)
def consulter_planning(request)
def details_reparation(request, pk)
```

### Admin Views (admin/)
```python
def dashboard(request)
def gerer_clients(request)
def gerer_menanicien(request)
def gerer_planning(request)
def gerer_vehicules(request)
```

## 4. URLs Structure

### Main URLs (urls.py)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clients.urls')),
    path('vehicules/', include('vehiculess.urls')),
    path('reparations/', include('reparation.urls')),
    path('rendez-vous/', include('planning.urls')),
    path('chatbot/', include('chatbot.urls')),
]
```

### Client URLs (clients/urls.py)
```python
urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path('profil/modifier/', views.modifier_profil, name='modifier_profil'),
]
```

### Vehicle URLs (vehiculess/urls.py)
```python
urlpatterns = [
    path('mes-vehicules/', views.mes_vehicules, name='mes_vehicules'),
    path('ajouter/', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('<int:pk>/', views.details_vehicule, name='details_vehicule'),
    path('<int:pk>/maintenance/', views.historique_maintenance, name='historique_maintenance'),
]
```

## 5. Templates Structure
```
templates/
├── base.html
├── home.html
├── clients/
│   ├── inscription.html
│   ├── connexion.html
│   ├── profil.html
│   └── modifier_profil.html
├── vehicules/
│   ├── liste.html
│   ├── ajouter.html
│   ├── details.html
│   └── maintenance.html
├── reparations/
│   ├── liste.html
│   ├── details.html
│   └── modifier.html
├── rendez_vous/
│   ├── nouveau.html
│   ├── liste.html
│   └── details.html
└── admin/
    ├── dashboard.html
    ├── clients.html
    ├── menanicien.html
    └── planning.html
```

## 6. User Roles and Permissions
- **Client**
  - Create/modify account
  - Register vehicles
  - Book appointments
  - View maintenance history
  - Chat with bot

- **Mécanicien**
  - View assigned vehicles
  - Update repair status
  - View work schedule
  - Access maintenance history

- **Admin**
  - Manage all users
  - Manage mechanics
  - View/modify all appointments
  - Access all vehicle data
  - Generate reports

## 7. Key Features
1. **Authentication System**
   - Registration
   - Login/Logout
   - Password reset

2. **Appointment System**
   - Book appointments
   - Cancel/modify appointments
   - Automatic confirmation

3. **Vehicle Management**
   - Add/modify vehicles
   - Maintenance history
   - Service records

4. **Repair Tracking**
   - Status updates
   - Cost tracking
   - Completion estimates

5. **Planning System**
   - Schedule management
   - Mechanic assignment
   - Availability tracking

6. **Chatbot Integration**
   - FAQ responses
   - Basic support
   - Appointment inquiries

## 8. Security Considerations
1. **Authentication**
   - Secure password storage
   - Session management
   - Password reset security

2. **Authorization**
   - Role-based access
   - Permission checking
   - Secure views

3. **Data Protection**
   - Client data privacy
   - Secure communications
   - Data encryption

4. **Input Validation**
   - Form validation
   - Data sanitization
   - CSRF protection 




   dashboad 
   {% extends 'base.html' %}

{% block content %}
<div class="container-fluid">
    <div class="row">
        <!-- Sidebar -->
        <nav class="col-md-2 d-none d-md-block bg-dark sidebar min-vh-100">
            <div class="sidebar-sticky pt-3">
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link active text-white" href="{% url 'admin_dashboard' %}">
                            <i class="fas fa-home"></i> Dashboard
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#">
                            <i class="fas fa-users"></i> Clients
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#">
                            <i class="fas fa-tools"></i> Mécaniciens
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#">
                            <i class="fas fa-car"></i> Véhicules
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#">
                            <i class="fas fa-calendar"></i> Rendez-vous
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-white" href="#">
                            <i class="fas fa-wrench"></i> Réparations
                        </a>
                    </li>
                </ul>
            </div>
        </nav>

        <!-- Main content -->
        <main role="main" class="col-md-10 ml-sm-auto px-4">
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 class="h2">Tableau de bord</h1>
                <div class="btn-toolbar mb-2 mb-md-0">
                    <div class="btn-group mr-2">
                        <button type="button" class="btn btn-sm btn-outline-secondary">Exporter</button>
                    </div>
                </div>
            </div>

            <!-- Statistics Cards -->
            <div class="row">
                <div class="col-xl-3 col-md-6 mb-4">
                    <div class="card border-left-primary shadow h-100 py-2">
                        <div class="card-body">
                            <div class="row no-gutters align-items-center">
                                <div class="col mr-2">
                                    <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                        Clients</div>
                                    <div class="h5 mb-0 font-weight-bold text-gray-800">{{ total_clients }}</div>
                                </div>
                                <div class="col-auto">
                                    <i class="fas fa-users fa-2x text-gray-300"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-xl-3 col-md-6 mb-4">
                    <div class="card border-left-success shadow h-100 py-2">
                        <div class="card-body">
                            <div class="row no-gutters align-items-center">
                                <div class="col mr-2">
                                    <div class="text-xs font-weight-bold text-success text-uppercase mb-1">
                                        Réparations en cours</div>
                                    <div class="h5 mb-0 font-weight-bold text-gray-800">{{ reparations_en_cours }}</div>
                                </div>
                                <div class="col-auto">
                                    <i class="fas fa-wrench fa-2x text-gray-300"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-xl-3 col-md-6 mb-4">
                    <div class="card border-left-info shadow h-100 py-2">
                        <div class="card-body">
                            <div class="row no-gutters align-items-center">
                                <div class="col mr-2">
                                    <div class="text-xs font-weight-bold text-info text-uppercase mb-1">
                                        Rendez-vous aujourd'hui</div>
                                    <div class="h5 mb-0 font-weight-bold text-gray-800">{{ rendez_vous_aujourdhui }}</div>
                                </div>
                                <div class="col-auto">
                                    <i class="fas fa-calendar fa-2x text-gray-300"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-xl-3 col-md-6 mb-4">
                    <div class="card border-left-warning shadow h-100 py-2">
                        <div class="card-body">
                            <div class="row no-gutters align-items-center">
                                <div class="col mr-2">
                                    <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">
                                        Mécaniciens</div>
                                    <div class="h5 mb-0 font-weight-bold text-gray-800">{{ total_mecaniciens }}</div>
                                </div>
                                <div class="col-auto">
                                    <i class="fas fa-tools fa-2x text-gray-300"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Recent Activity -->
            <div class="row mt-4">
                <div class="col-12">
                    <div class="card shadow mb-4">
                        <div class="card-header py-3">
                            <h6 class="m-0 font-weight-bold text-primary">Activité récente</h6>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-bordered" width="100%" cellspacing="0">
                                    <thead>
                                        <tr>
                                            <th>Date</th>
                                            <th>Client</th>
                                            <th>Véhicule</th>
                                            <th>Type</th>
                                            <th>Statut</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {% for activity in recent_activities %}
                                        <tr>
                                            <td>{{ activity.date }}</td>
                                            <td>{{ activity.client }}</td>
                                            <td>{{ activity.vehicule }}</td>
                                            <td>{{ activity.type }}</td>
                                            <td>{{ activity.statut }}</td>
                                        </tr>
                                        {% endfor %}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</div>

<!-- Add Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<!-- Add custom CSS -->
<style>
    .sidebar {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        z-index: 100;
        padding: 48px 0 0;
        box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
    }
    
    .sidebar-sticky {
        position: relative;
        top: 0;
        height: calc(100vh - 48px);
        padding-top: .5rem;
        overflow-x: hidden;
        overflow-y: auto;
    }
    
    .nav-link {
        font-weight: 500;
        color: #333;
    }
    
    .nav-link:hover {
        color: #007bff;
    }
    
    .border-left-primary {
        border-left: .25rem solid #4e73df !important;
    }
    
    .border-left-success {
        border-left: .25rem solid #1cc88a !important;
    }
    
    .border-left-info {
        border-left: .25rem solid #36b9cc !important;
    }
    
    .border-left-warning {
        border-left: .25rem solid #f6c23e !important;
    }
</style>
{% endblock %}
