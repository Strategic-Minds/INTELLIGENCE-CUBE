import { test, expect } from '@playwright/test';
test('mobile', async ({ page }) => { await page.goto('/chat'); await expect(page.locator('body')).toBeVisible(); });
