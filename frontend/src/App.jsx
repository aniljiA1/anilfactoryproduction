// App.jsx
import React from "react";
import WorkerTable from "./components/WorkerTable";
import FactorySummary from "./components/FactorySummary";

export default function App() {
  return (
    <div className="p-5 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">
        🏭 Factory Productivity Dashboard
      </h1>
      <FactorySummary />
      <WorkerTable />
    </div>
  );
}
