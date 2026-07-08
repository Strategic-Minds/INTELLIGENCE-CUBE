export type ConnectorStatus = 'approved' | 'queued' | 'blocked';

export type ConnectorRecord = {
  name: string;
  state: ConnectorStatus;
  scope: string;
};

export const connectors: {
  status: 'ready';
  items: ConnectorRecord[];
} = {
  status: 'ready',
  items: [
    { name: 'ChatGPT', state: 'approved', scope: 'Draft, review, and response synthesis' },
    { name: 'Codex', state: 'approved', scope: 'Branch-safe implementation and repair' },
    { name: 'Supabase', state: 'queued', scope: 'Schema and runtime queue support' },
    { name: 'Vercel', state: 'queued', scope: 'Preview and cron surface' },
  ],
};
