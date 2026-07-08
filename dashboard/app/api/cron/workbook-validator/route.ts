import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    ok: true,
    job: 'workbook-validator',
    status: 'queued',
    source: 'vercel-cron',
  });
}
