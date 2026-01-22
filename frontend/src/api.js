// api.js
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const getWorkerMetrics = async () => {
  const res = await fetch(`${API_BASE_URL}/workers/metrics`);
  if (!res.ok) {
    throw new Error("Failed to fetch worker metrics");
  }
  return res.json();
};
