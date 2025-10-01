# 🚀 Odoo Subscription & Analytics Hub

Un módulo **personalizado para Odoo** que permite a las empresas gestionar **suscripciones recurrentes**, **pagos automáticos** y visualizar **dashboards analíticos** con KPIs de negocio.  

Este proyecto demuestra habilidades avanzadas en **Odoo Backend**, **ORM**, **flujos de negocio**, **dashboards analíticos**, **automatizaciones (cron jobs)** y **despliegue en Docker**.

---

## 📦 Características principales
- 📝 **Gestión de planes de suscripción** con precios, ciclos de facturación y beneficios.
- 🤝 **Contratos vinculados a clientes** con máquina de estados: `draft → active → suspended → canceled`.
- 💳 **Pagos recurrentes** con cálculo automático del total acumulado.
- 🔄 **Automatización con Cron Jobs** para:
  - Generar facturas periódicas.
  - Enviar recordatorios de vencimiento.
- 📊 **Dashboards y KPIs**:
  - Ingresos recurrentes mensuales (MRR).
  - Churn rate (% de contratos cancelados).
  - Suscripciones activas vs canceladas.
- 🔒 **Seguridad avanzada** con roles, permisos y reglas de registros.
- 🐳 **Despliegue con Docker Compose** (Odoo + PostgreSQL + Nginx).

---

## 📐 Modelos y Campos Clave

### 1. `subscription.plan`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | Char | Nombre del plan (Premium, Básico, etc.). |
| `price` | Float | Precio por ciclo de facturación. |
| `billing_cycle` | Selection | `monthly / quarterly / yearly`. |
| `currency_id` | Many2one | Moneda del plan. |
| `active` | Boolean | Activa o desactiva el plan. |
| `contract_count` | Integer (compute) | Total de contratos asociados. |

---

### 2. `subscription.contract`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | Char | Código/Número de contrato. |
| `customer_id` | Many2one | Cliente asociado (`res.partner`). |
| `plan_id` | Many2one | Plan elegido. |
| `start_date` | Date | Fecha de inicio. |
| `next_billing_date` | Date (compute) | Próxima fecha de facturación. |
| `state` | Selection | `draft / active / suspended / canceled`. |
| `total_amount` | Monetary (compute) | Total acumulado de pagos. |
| `auto_renew` | Boolean | Renovación automática. |
| `payment_ids` | One2many | Pagos vinculados al contrato. |

---

### 3. `subscription.payment`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `name` | Char | Código/Referencia del pago. |
| `contract_id` | Many2one | Contrato al que pertenece. |
| `payment_date` | Date | Fecha de pago. |
| `amount` | Monetary | Monto pagado. |
| `state` | Selection | `draft / paid / failed`. |
| `invoice_id` | Many2one | Factura generada (si aplica). |

---
