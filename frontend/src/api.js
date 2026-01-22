// api.js
export const API_BASE = "http://127.0.0.1:8000";

export const getWorkerMetrics = async () => {
  const res = await fetch(`${API_BASE}/workers/metrics`);
  if (!res.ok) throw new Error("API error");
  return res.json();
};
