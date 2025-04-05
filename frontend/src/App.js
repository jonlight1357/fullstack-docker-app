import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [timestamp, setTimestamp] = useState("");

  useEffect(() => {
    axios.get("http://51.24.8.215:5000/api/data").then((res) => {
      setTimestamp(res.data.timestamp);
    });
  }, []);

  return (
    <div>
      <h1>React + Flask + PostgreSQL</h1>
      <p>Timestamp from backend: {timestamp}</p>
    </div>
  );
}

export default App;
