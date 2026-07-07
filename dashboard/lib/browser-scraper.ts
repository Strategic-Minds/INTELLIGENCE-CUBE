export type BrowserScrapeResult = {
  ok: boolean;
  url: string;
  title: string;
  description: string;
  links: number;
  error?: string;
};

function isPublicHttpUrl(input: string) {
  try {
    const url = new URL(input);
    return (url.protocol === 'https:' || url.protocol === 'http:') && !['localhost', '127.0.0.1', '::1'].includes(url.hostname);
  } catch {
    return false;
  }
}

export async function scrapePublicPage(input: string): Promise<BrowserScrapeResult> {
  if (!isPublicHttpUrl(input)) {
    return {
      ok: false,
      url: input,
      title: '',
      description: '',
      links: 0,
      error: 'Only public http(s) URLs are allowed.',
    };
  }

  const response = await fetch(input, {
    headers: {
      'user-agent': 'IntelligenceCube/1.0 (+workbook-first)',
      accept: 'text/html,application/xhtml+xml',
    },
  });

  const html = await response.text();
  const title = html.match(/<title[^>]*>(.*?)<\/title>/i)?.[1]?.trim() ?? '';
  const description =
    html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']+)["'][^>]*>/i)?.[1]?.trim() ?? '';
  const links = (html.match(/<a\b/gi) ?? []).length;

  return {
    ok: response.ok,
    url: input,
    title,
    description,
    links,
    error: response.ok ? undefined : `Request returned ${response.status}`,
  };
}
