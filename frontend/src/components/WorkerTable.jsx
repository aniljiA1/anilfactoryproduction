// WorkerTable.jsx
import React, { useEffect, useState } from "react";
import { getWorkerMetrics } from "../api";

export default function WorkerTable() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    getWorkerMetrics()
      .then(setMetrics)
      .catch((err) => console.error(err));
  }, []);

  if (!metrics) return <p>Loading worker metrics...</p>;

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full border border-gray-300 divide-y divide-gray-200">
        <thead className="bg-gray-100">
          <tr>
            <th className="px-4 py-2 text-left">Worker</th>
            <th className="px-4 py-2 text-left">Working (s)</th>
            <th className="px-4 py-2 text-left">Idle (s)</th>
            <th className="px-4 py-2 text-left">Utilization (%)</th>
            <th className="px-4 py-2 text-left">Units</th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {Object.entries(metrics).map(([wid, data]) => (
            <tr key={wid} className="hover:bg-gray-50">
              <td className="px-4 py-2">{wid}</td>
              <td className="px-4 py-2">{data.working_seconds}</td>
              <td className="px-4 py-2">{data.idle_seconds}</td>
              <td className="px-4 py-2">{data.utilization}</td>
              <td className="px-4 py-2">{data.units}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
