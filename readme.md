kodiAuto
Rental management System in Kenya

Landlords and property managers face different "headaches" daily. Moving from manual record-keeping to a digital system solves several high-friction problems, therefore making this app a vital tool.

These are the problems this system solves:
1. The "Paper Trail" Problem
Landlords often rely on physical notebooks or disparate WhatsApp chats to track who has paid. This leads to lost records, disputes over deposits, and difficulty tracking lease expiry dates.
Therefore, the system creates a Centralized Cloud Database where all tenant data, digital lease copies, and payment histories are stored in one place, accessible from a phone or laptop.

2. Rent Collection & Reconciliation
Manually checking bank statements or M-Pesa messages to see who paid and then manually updating a ledger is time-consuming and prone to human error.
Thus, Automated Payment Tracking will solve that. By integrating payment methods (like M-Pesa), the system can automatically mark a month as "Paid" and generate a digital receipt the moment the transaction clears.
When calculating the Total Balance due for a tenant, the system will be running a summation of all charges minus the payments:

B = \sum (Rent + Fees) - \sum (Payments)

Where:
B is the current balance.
Rent includes all recurring monthly charges.
Fees includes late fees or utility surcharges


3. Maintenance Chaos
Tenants call at odd hours for repairs. Landlords forget which plumber went to which house, or they lose track of whether a leaking tap was actually fixed.
Ticketing System will solve that by tenants submitting requests through the app. The landlord can assign a "Status" (Pending, In Progress, Resolved) to each task, creating a clear history of property upkeep.

4. Financial Blind Spots
At the end of the year, many landlords don't actually know their true profit because they haven't tracked expenses like garbage collection, security, and minor repairs against the gross rent.
Therefore, Automated Financial Reporting will help in the calculation of the Net Operating Income (NOI) as follows;

NOI = (Gross Potential Rent – Vacancy Losses) – Operating Expenses

This gives the landlord a professional view of their investment's health

5. Communication Gaps
Sending individual reminders for rent or notices for scheduled maintenance is tedious. 

Hence the Automated Notifications will come in handy where the system sends automated SMS or push notifications three days before rent is due and, on the day, when the rent is due.

Entity Relationship Diagram (ERD) structure.
Landlords (Users): landlord_id (PK), name, email, phone_number, password.
One-to-Many with Properties. One landlord can own many properties/buildings.

Properties: property_id (PK), landlord_id (FK), name, address, property_type (Residential/Commercial).
One-to-Many with Units. One building contains multiple units.

Units: unit_id (PK), property_id (FK), unit_number, rent_amount, status (Vacant/Occupied).
One-to-One with Leases. At any given time, one unit usually has one active lease.

Tenants: tenant_id (PK), first_name, last_name, email, phone_number, id_number.
One-to-Many with Leases. A tenant can rent multiple units or renew contract thus multiple leases.

Leases: lease_id (PK), unit_id (FK), tenant_id (FK), start_date, end_date, deposit_amount.
One-to-Many with Payments. One lease generates many monthly payment records.

Payments: payment_id (PK), lease_id (FK), amount, payment_date, payment_method (M-Pesa/Cash/Bank), transaction_id.
One-to-Many with Leases. One Contract can have multiple monthly installments.




