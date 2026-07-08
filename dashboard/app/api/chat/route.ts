import { chatTranscript } from '../../../lib/shell-data';

export async function GET() {
  return Response.json({
    route: 'chat',
    status: 'ready',
    transcript: chatTranscript,
  });
}
