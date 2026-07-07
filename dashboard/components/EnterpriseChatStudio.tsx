'use client';

import { useEffect, useMemo, useState } from 'react';

type Theme = 'light' | 'dark';

type Message = {
  id: number;
  role: 'system' | 'user' | 'assistant';
  title: string;
  body: string;
  tone?: 'neutral' | 'positive' | 'warning';
};

const starterMessages: Message[] = [
  {
    id: 1,
    role: 'system',
    title: 'Command rail',
    body: 'Workbook-first operation is active. Draft requests, approval gates, and receipt tracking stay visible at all times.',
  },
  {
    id: 2,
    role: 'assistant',
    title: 'Swarm briefing',
    body: 'This studio is ready for connector-aware chats, branch-safe actions, and reviewable operational output.',
  },
];

const prompts = [
  'Summarize the active workbook state',
  'List blocker receipts needing attention',
  'Prepare a connector approval request',
  'Draft the next branch-safe action',
];

const paletteItems = [
  { label: 'Focus chat', action: 'Focus chat composer' },
  { label: 'Review blockers', action: 'Open blocker board' },
  { label: 'Inspect receipts', action: 'Review receipt timeline' },
  { label: 'Switch theme', action: 'Toggle light or dark mode' },
];

export default function EnterpriseChatStudio() {
  const [theme, setTheme] = useState<Theme>('dark');
  const [draft, setDraft] = useState('');
  const [messages, setMessages] = useState(starterMessages);
  const [paletteOpen, setPaletteOpen] = useState(false);
  const [animatedCount, setAnimatedCount] = useState(0);

  useEffect(() => {
    const saved = window.localStorage.getItem('cube-theme') as Theme | null;
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const nextTheme = saved ?? (prefersDark ? 'dark' : 'light');
    setTheme(nextTheme);
  }, []);

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    window.localStorage.setItem('cube-theme', theme);
  }, [theme]);

  useEffect(() => {
    setAnimatedCount(0);
    const timer = window.setInterval(() => {
      setAnimatedCount((current) => {
        const next = current + 1;
        return next >= messages.length ? messages.length : next;
      });
    }, 120);
    return () => window.clearInterval(timer);
  }, [messages.length, theme]);

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault();
        setPaletteOpen((current) => !current);
      }
      if (event.key === 'Escape') {
        setPaletteOpen(false);
      }
    };
    window.addEventListener('keydown', onKeyDown);
    return () => window.removeEventListener('keydown', onKeyDown);
  }, []);

  const transcriptCount = useMemo(() => messages.length, [messages.length]);

  const sendMessage = (text: string) => {
    const clean = text.trim();
    if (!clean) return;
    const now = Date.now();
    setMessages((current) => [
      ...current,
      { id: now, role: 'user', title: 'Operator', body: clean, tone: 'positive' },
      {
        id: now + 1,
        role: 'assistant',
        title: 'Intelligence Cube',
        body: 'Acknowledged. I can route this through the workbook, connector registry, and receipt path before action.',
        tone: 'neutral',
      },
    ]);
    setDraft('');
  };

  return (
    <div className="shell-grid">
      <aside className="sidebar">
        <div className="pill">Enterprise PWA Chat</div>
        <div style={{ marginTop: 18 }}>
          <h1 style={{ margin: 0, fontSize: 32, lineHeight: 1.05 }}>Intelligence Cube</h1>
          <p style={{ color: 'var(--muted)', marginTop: 12, lineHeight: 1.6 }}>
            Workbook-governed chat, approvals, receipts, and connector routing in one installable surface.
          </p>
        </div>

        <div className="sidebar-links">
          {['Chat', 'Workbooks', 'Connectors', 'Approvals', 'Receipts', 'Blockers'].map((item, index) => (
            <a key={item} className={`sidebar-link ${index === 0 ? 'active' : ''}`} href={`/${item.toLowerCase()}`}>
              {item}
            </a>
          ))}
        </div>

        <div className="card" style={{ padding: 18, marginTop: 24 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', gap: 12, alignItems: 'center' }}>
            <div>
              <div style={{ fontSize: 12, color: 'var(--muted)', textTransform: 'uppercase', letterSpacing: '.08em' }}>Theme</div>
              <strong>{theme === 'dark' ? 'Dark mode' : 'Light mode'}</strong>
            </div>
            <button className="button" onClick={() => setTheme((current) => (current === 'dark' ? 'light' : 'dark'))}>
              Toggle
            </button>
          </div>
          <p style={{ color: 'var(--muted)', lineHeight: 1.6, marginBottom: 0 }}>
            Persistent theme state, install-ready shell, and high-contrast controls for enterprise use.
          </p>
        </div>

        <div className="card" style={{ padding: 18, marginTop: 18 }}>
          <div style={{ fontSize: 12, color: 'var(--muted)', textTransform: 'uppercase', letterSpacing: '.08em' }}>
            Live posture
          </div>
          <strong>Workbook-first safe mode</strong>
          <p style={{ color: 'var(--muted)', lineHeight: 1.6, marginBottom: 0 }}>
            {transcriptCount} transcript entries, branch-safe actions, and reviewable output.
          </p>
        </div>
      </aside>

      <main className="main">
        <div className="toolbar">
          <div>
            <div className="pill">Chat workspace</div>
            <h2 style={{ margin: '14px 0 6px', fontSize: 28 }}>Operational conversation hub</h2>
            <p style={{ margin: 0, color: 'var(--muted)', lineHeight: 1.6, maxWidth: 760 }}>
              Use this PWA to draft actions, review connector state, and keep every sensitive step behind the workbook gate.
            </p>
          </div>
          <div className="button-row">
            <button className="button" onClick={() => setPaletteOpen((current) => !current)}>
              Command palette
            </button>
            <button className="button primary">Install app</button>
          </div>
        </div>

        {paletteOpen && (
          <section className="card palette">
            <div style={{ display: 'flex', justifyContent: 'space-between', gap: 12, alignItems: 'center' }}>
              <strong>Command palette</strong>
              <span style={{ color: 'var(--muted)', fontSize: 12 }}>Ctrl/Cmd + K</span>
            </div>
            <div className="palette-grid">
              {paletteItems.map((item) => (
                <button
                  key={item.label}
                  className="button palette-button"
                  onClick={() => {
                    if (item.label === 'Switch theme') {
                      setTheme((current) => (current === 'dark' ? 'light' : 'dark'));
                    }
                    if (item.label === 'Focus chat') {
                      document.querySelector<HTMLTextAreaElement>('.chat-input')?.focus();
                    }
                    setPaletteOpen(false);
                  }}
                >
                  <strong>{item.label}</strong>
                  <span>{item.action}</span>
                </button>
              ))}
            </div>
          </section>
        )}

        <div className="grid dashboard-grid">
          <section className="card" style={{ padding: 24 }}>
            <div style={{ marginTop: 22 }} className="message-list">
              {messages.slice(0, animatedCount).map((message) => (
                <article key={message.id} className={`message ${message.role === 'user' ? 'user' : ''}`}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', gap: 12, alignItems: 'center' }}>
                    <strong>{message.title}</strong>
                    <span className={`message-role ${message.role}`}>{message.role}</span>
                  </div>
                  <div style={{ color: 'var(--muted)', lineHeight: 1.6 }}>{message.body}</div>
                </article>
              ))}
            </div>

            <div style={{ marginTop: 22 }}>
              <textarea
                className="chat-input"
                value={draft}
                onChange={(event) => setDraft(event.target.value)}
                placeholder="Ask the swarm to inspect, plan, or prepare a connector-safe action..."
              />
              <div className="button-row" style={{ marginTop: 14 }}>
                <button className="button primary" onClick={() => sendMessage(draft)}>
                  Send draft
                </button>
                <button className="button" onClick={() => setDraft('')}>
                  Clear
                </button>
              </div>
            </div>
          </section>

          <aside className="grid">
            <section className="card" style={{ padding: 20 }}>
              <div className="pill">Quick prompts</div>
              <div style={{ display: 'grid', gap: 10, marginTop: 16 }}>
                {prompts.map((prompt) => (
                  <button key={prompt} className="button prompt-button" onClick={() => sendMessage(prompt)}>
                    {prompt}
                  </button>
                ))}
              </div>
            </section>

            <section className="card" style={{ padding: 20 }}>
              <div className="pill">PWA profile</div>
              <div style={{ display: 'grid', gap: 12, marginTop: 16 }}>
                {[
                  ['Mode', 'Standalone install'],
                  ['Theme', theme],
                  ['Governance', 'Workbook-first'],
                  ['Branch', 'workbook-os/scaffold-v1'],
                ].map(([label, value]) => (
                  <div key={label} style={{ display: 'flex', justifyContent: 'space-between', gap: 16 }}>
                    <span style={{ color: 'var(--muted)' }}>{label}</span>
                    <strong>{value}</strong>
                  </div>
                ))}
              </div>
            </section>
          </aside>
        </div>
      </main>
    </div>
  );
}
