// Supabase connection details. Fill these in after running supabase/schema.sql — see docs/README.md.
//
// Both values are safe to commit and safe to serve publicly: the anon key is a *public* client key,
// and the row-level-security policies in supabase/schema.sql are what actually restrict access to
// your own rows. Never put the service_role key here — it bypasses RLS entirely and belongs only in
// the untracked .env the local Python scripts read.
//
// Left blank, the app still works: it keeps progress in this browser's localStorage and shows
// "local only" in the You tab. Filling them in turns on sync with the laptop.

export const SUPABASE_URL = 'https://kexplosmhqtrekzdqrvy.supabase.co';
export const SUPABASE_ANON_KEY = 'sb_publishable_ORzhLnR2rQDzwvTVZTTqng_rZykprPU';
