-- Run this in the Supabase SQL Editor (Project -> SQL Editor -> New query)
-- before starting the backend. This creates the two tables the app needs.

create extension if not exists "pgcrypto";

create table if not exists users (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    email text not null unique,
    password text not null,
    created_at timestamptz not null default now()
);

create table if not exists expenses (
    id uuid primary key default gen_random_uuid(),
    user_id uuid not null references users(id) on delete cascade,
    title text not null,
    amount numeric(12, 2) not null,
    category text not null,
    expense_date date not null,
    created_at timestamptz not null default now()
);

create index if not exists idx_expenses_user_id on expenses(user_id);

-- NOTE: This app uses its own JWT auth (not Supabase Auth), and the backend
-- talks to Supabase using the service/anon key directly, so Row Level
-- Security is left off here. If you later switch to Supabase Auth, enable
-- RLS and add policies scoping rows to auth.uid().
