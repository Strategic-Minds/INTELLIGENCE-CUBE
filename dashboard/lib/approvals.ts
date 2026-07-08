export type ApprovalStatus = 'needs-approval' | 'ready' | 'approved' | 'blocked';

export type ApprovalRecord = {
  id: string;
  title: string;
  status: ApprovalStatus;
  detail: string;
};

export const approvals: {
  status: 'ready';
  items: ApprovalRecord[];
} = {
  status: 'ready',
  items: [
    {
      id: 'APP-001',
      title: 'Connector-aware chat draft',
      status: 'needs-approval',
      detail: 'Safe draft ready for approval gate',
    },
    {
      id: 'APP-002',
      title: 'Branch-safe repo repair',
      status: 'approved',
      detail: 'Validation completed locally',
    },
  ],
};
