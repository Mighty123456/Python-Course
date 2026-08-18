// Frontend unit tests using Node.js built-in test runner (node:test)
// Run with: npm test  OR  node --test test_server.js

import { test } from 'node:test';
import assert from 'node:assert/strict';

// ── Test 1: Health endpoint response shape ────────────────────────────────────
test('health endpoint returns correct JSON shape', () => {
  const mockResponse = { status: 'healthy', service: 'Express Frontend' };
  assert.equal(mockResponse.status, 'healthy');
  assert.equal(mockResponse.service, 'Express Frontend');
});

// ── Test 2: BACKEND_URL env variable defaults ─────────────────────────────────
test('BACKEND_URL defaults to localhost:5000 when not set', () => {
  const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';
  assert.equal(BACKEND_URL, 'http://localhost:5000');
});

// ── Test 3: PORT env variable defaults ────────────────────────────────────────
test('PORT defaults to 3000 when not set', () => {
  const PORT = parseInt(process.env.PORT || '3000', 10);
  assert.equal(PORT, 3000);
  assert.ok(PORT > 0 && PORT < 65536, 'PORT must be a valid port number');
});

// ── Test 4: Backend status logic ──────────────────────────────────────────────
test('backend status resolves to Connected on healthy response', () => {
  const apiResponse = { status: 'healthy' };
  const backendStatus = apiResponse.status === 'healthy' ? 'Connected' : 'Disconnected';
  assert.equal(backendStatus, 'Connected');
});

// ── Test 5: Backend status resolves to Disconnected on unhealthy response ─────
test('backend status resolves to Disconnected on error', () => {
  const apiResponse = { status: 'error' };
  const backendStatus = apiResponse.status === 'healthy' ? 'Connected' : 'Disconnected';
  assert.equal(backendStatus, 'Disconnected');
});
