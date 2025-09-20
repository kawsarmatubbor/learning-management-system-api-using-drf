import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "./Components/Header/Header";
import Home from "./Pages/Home/Home";

function App() {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route
                    path="/about"
                    element={<div className="container">About</div>}
                />
                <Route
                    path="/contact"
                    element={<div className="container">Contact</div>}
                />
                <Route
                    path="/login"
                    element={<div className="container">Login</div>}
                />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
