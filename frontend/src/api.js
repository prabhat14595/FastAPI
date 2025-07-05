// API utility for all backend endpoints
const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:8000';

export async function registerUser(data) {
  const res = await fetch(`${API_BASE}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function loginUser(data) {
  const res = await fetch(`${API_BASE}/auth/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getProtected(token) {
  const res = await fetch(`${API_BASE}/auth/protected`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}

export async function healthcheck() {
  const res = await fetch(`${API_BASE}/api/healthcheck`);
  return res.json();
}

export async function createItem(data, token) {
  const res = await fetch(`${API_BASE}/api/items/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function getItemById(id, token) {
  const res = await fetch(`${API_BASE}/api/items/${id}`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.json();
}
