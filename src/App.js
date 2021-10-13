import Home from "./components/Home";
import Navbar from "./components/Navbar";
// import Chat from "./components/Chat";
function App() {
  return (
    <div className="App">
      <header className="App-header">
      {/* <Chat/> */}
      <Navbar/>
      <Home/>
      </header>
    </div>
  );
}

export default App;
