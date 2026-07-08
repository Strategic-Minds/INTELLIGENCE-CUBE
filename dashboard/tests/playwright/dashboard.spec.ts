import { test, expect } from '@playwright/test';
test('dashboard', async ({ page }) => { await page.goto('/swarm'); await expect(page.locator('body')).toBeVisible(); });
