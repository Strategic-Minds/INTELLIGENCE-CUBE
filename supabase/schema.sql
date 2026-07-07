create table if not exists task_queue (id uuid primary key default gen_random_uuid(), status text not null default 'draft', payload jsonb not null default '{}'::jsonb, created_at timestamptz default now());
create table if not exists approval_queue (id uuid primary key default gen_random_uuid(), action_type text, status text default 'approval_required', payload jsonb default '{}'::jsonb, created_at timestamptz default now());
create table if not exists receipt_queue (id uuid primary key default gen_random_uuid(), receipt_type text, payload jsonb default '{}'::jsonb, created_at timestamptz default now());
create table if not exists blocker_queue (id uuid primary key default gen_random_uuid(), blocker text, workaround text, created_at timestamptz default now());
create table if not exists connector_runs (id uuid primary key default gen_random_uuid(), connector text, action text, status text, receipt_path text, created_at timestamptz default now());
