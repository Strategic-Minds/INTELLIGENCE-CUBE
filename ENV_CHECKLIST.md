# ENV_CHECKLIST

## Required env names only
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY` only in approved secret storage, never committed
- `CRON_SECRET`
- `VERCEL_TOKEN` only in approved secret storage, never committed

## Environment rules
- Commit env names, never values.
- Keep preview and production names separate.
- Document any new env variable before using it in code.

## Verification
- build must succeed without secrets in the repository
- API routes must fail safely when env values are missing
- scraper must not accept secret-bearing targets or private network URLs
