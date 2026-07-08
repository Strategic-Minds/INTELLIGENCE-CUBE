import { NextResponse } from 'next/server';
import { agentProfile, agentTasks } from '../../../lib/shell-data';
import { scrapePublicPage } from '../../../lib/browser-scraper';

export async function GET() {
  return NextResponse.json({
    route: 'agent',
    status: 'ready',
    profile: agentProfile,
    tasks: agentTasks,
  });
}

export async function POST(request: Request) {
  const payload = (await request.json().catch(() => ({}))) as { action?: string; url?: string };

  if (payload.action === 'scrape') {
    if (!payload.url) {
      return NextResponse.json({ ok: false, error: 'Missing url' }, { status: 400 });
    }

    const result = await scrapePublicPage(payload.url);
    return NextResponse.json({
      route: 'agent',
      action: 'scrape',
      result,
      profile: agentProfile,
    });
  }

  return NextResponse.json({
    route: 'agent',
    status: 'ready',
    profile: agentProfile,
    tasks: agentTasks,
  });
}
