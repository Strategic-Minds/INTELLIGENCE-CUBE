import { workbook } from '../../../lib/workbook';

export async function GET() {
  return Response.json({
    route: 'workbooks',
    status: 'ready',
    workbook,
  });
}
