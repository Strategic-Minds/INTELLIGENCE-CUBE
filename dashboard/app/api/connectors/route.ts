import { connectorRows } from '../../../lib/shell-data';

export async function GET() {
  return Response.json({
    route: 'connectors',
    status: 'ready',
    connectors: connectorRows,
  });
}
