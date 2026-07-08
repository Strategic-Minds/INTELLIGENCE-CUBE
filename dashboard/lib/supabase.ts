export type SupabaseRuntime = {
  status: 'configured' | 'pending';
  tables: string[];
  note: string;
};

export const supabase: SupabaseRuntime = {
  status: 'pending',
  tables: ['task_queue', 'approval_queue', 'receipt_queue', 'blocker_queue', 'connector_runs'],
  note: 'Environment keys and RLS hardening remain the next step before live persistence.',
};
