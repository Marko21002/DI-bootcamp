import logo from './logo.svg';
import './App.css';

import ErrorBoundary from './ErrorBoundary';
import Counter from './components/Counter';


function App() {
  return (
    <div className="App">
      <header className="App-header">
       <ErrorBoundary>
       <Counter/>
       </ErrorBoundary>
         
        
       
      </header>
    </div>
  );
}

export default App;
