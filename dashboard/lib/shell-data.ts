export type ChatRole = 'system' | 'user' | 'assistant';

export type ChatMessage = {
  id: number;
  role: ChatRole;
  title: string;
  body: string;
  tone: 'neutral' | 'positive' | 'warning';
};

export type QueueItem = {
  id: string;
  title: string;
  status: 'ready' | 'needs-approval' | 'blocked' | 'complete';
  detail: string;
};

export const workbookStatus = [
  {
    name: 'Master workbook',
    value: 'Validated',
    detail: 'Connector-ready final workbook present in repo',
  },
  {
    name: 'Index workbook',
    value: 'Validated',
    detail: 'Workbook index uploaded and tracked',
  },
  {
    name: 'Connector registry',
    value: 'Ready',
    detail: 'Registry, contracts, run log, install map required',
  },
] as const;

export const connectorRows = [
  { name: 'ChatGPT', state: 'approved', scope: 'Draft, review, and response synthesis' },
  { name: 'Codex', state: 'approved', scope: 'Branch-safe implementation and repair' },
  { name: 'Supabase', state: 'queued', scope: 'Schema and runtime queue support' },
  { name: 'Vercel', state: 'queued', scope: 'Preview and cron surface' },
] as const;

export const approvalRows = [
  { id: 'APP-001', title: 'Connector-aware chat draft', status: 'needs-approval', detail: 'Safe draft ready for approval gate' },
  { id: 'APP-002', title: 'Branch-safe repo repair', status: 'ready', detail: 'Validation completed locally' },
] as const;

export const blockerRows = [
  { id: 'BLK-001', title: 'Binary upload verification', status: 'complete', detail: 'Workbook binary path present' },
  { id: 'BLK-002', title: 'Production deploy', status: 'blocked', detail: 'Deliberately out of scope' },
] as const;

export const receiptRows = [
  { id: 'RCT-001', title: 'Workbook upload receipt', status: 'complete', detail: 'Master and support workbooks tracked' },
  { id: 'RCT-002', title: 'PWA chat receipt', status: 'complete', detail: 'Theme, install metadata, and smoke tests passed' },
] as const;

export const chatTranscript: ChatMessage[] = [
  {
    id: 1,
    role: 'system',
    title: 'Command rail',
    body: 'Workbook-first operation is active. Draft requests, approval gates, and receipt tracking stay visible at all times.',
    tone: 'neutral',
  },
  {
    id: 2,
    role: 'assistant',
    title: 'Swarm briefing',
    body: 'This studio is ready for connector-aware chats, branch-safe actions, and reviewable operational output.',
    tone: 'positive',
  },
];

export const swarmQueues: QueueItem[] = [
  {
    id: 'Q-001',
    title: 'Planner swarm',
    status: 'ready',
    detail: 'Summarizes workbook state and decomposes tasks.',
  },
  {
    id: 'Q-002',
    title: 'Codex swarm',
    status: 'needs-approval',
    detail: 'Waits for approval before file mutation.',
  },
  {
    id: 'Q-003',
    title: 'Validation swarm',
    status: 'complete',
    detail: 'Runs build, smoke, and boundary checks.',
  },
];
