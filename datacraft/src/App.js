import React, { useEffect, useState } from 'react';
import { getTests } from './api';



const TestComponent = () => {
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    const fetchData = async () => {
            try {
              const data = await getTests();
              setTests(data);
            } catch (error) {
              setError(error);
            } finally {
                setLoading(false);
              }
        };
        
        fetchData();
      }, []);
      
      if (loading) return <div>Loading...</div>;
      if (error) return <div>Error: {error.message}</div>;
      
      return (
        <div>
            <h1>Lista de Testes</h1>
            <ul>
                {tests.map((test) => (
                  <li key={test.id}>{test.name}</li>
                ))}
            </ul>
        </div>
    );
  };
  
  export default TestComponent;

/*import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/
