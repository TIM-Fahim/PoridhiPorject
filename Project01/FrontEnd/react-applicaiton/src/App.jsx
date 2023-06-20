import { Student } from "./Student";
import { useState, useEffect } from "react";

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5050/getlist").then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  return (
    <div>
      <pre>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
  // return (
  //   <div>
  //     <h1>Student Information</h1>
  //     <Student />
  //   </div>
  // );
}

export default App;