// FactorySummary.jsx
import React, { useEffect, useState } from "react";
import { API_BASE } from "../api";

export default function FactorySummary() {
  const [summary, setSummary] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/factory/metrics`)
      .then((res) => {
        if (!res.ok) throw new Error(`Status ${res.status}`);
        return res.json();
      })
      .then(setSummary)
      .catch((err) => {
        console.error(err); // log full error
        setError("Failed to fetch factory metrics");
      });
  }, []);

  if (error) return <p className="text-red-500">{error}</p>;
  if (!summary) return <p>Loading factory metrics...</p>;

  return (
    <div className="mb-5">
      <h2 className="text-2xl font-semibold mb-4">🏭 Factory Summary</h2>

      <div className="flex gap-5 flex-wrap">
        <Metric
          label="Total Productive Time (hrs)"
          value={summary.total_productive_hours}
        />
        <Metric label="Total Units Produced" value={summary.total_units} />
        <Metric label="Avg Utilization (%)" value={summary.avg_utilization} />
      </div>
    </div>
  );
}

function Metric({ label, value }) {
  return (
    <div className="border border-gray-300 rounded-lg p-4 min-w-[200px] shadow-sm">
      <h4 className="text-gray-700 mb-2">{label}</h4>
      <strong className="text-xl">{value}</strong>
    </div>
  );
}
