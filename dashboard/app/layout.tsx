import './globals.css';

export const metadata = {
  title: 'Intelligence Cube',
  description: 'Workbook-first enterprise chat and control plane.',
  applicationName: 'Intelligence Cube',
  manifest: '/manifest.webmanifest',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
