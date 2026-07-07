import { receipts } from '../../../lib/receipts';

export async function GET() {
  return Response.json({
    route: 'receipts',
    status: 'ready',
    receipts,
  });
}
