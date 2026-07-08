import { blockerRows } from '../../../lib/shell-data';

export async function GET() {
  return Response.json({
    route: 'blockers',
    status: 'ready',
    blockers: blockerRows,
  });
}
