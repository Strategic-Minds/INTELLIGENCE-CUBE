import { approvalRows } from '../../../lib/shell-data';

export async function GET() {
  return Response.json({
    route: 'approvals',
    status: 'ready',
    approvals: approvalRows,
  });
}
