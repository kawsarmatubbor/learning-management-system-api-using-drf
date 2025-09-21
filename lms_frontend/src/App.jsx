import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "./Components/Header/Header";
import Home from "./Pages/Home";
import CoursesDetail from "./Pages/CoursesDetail";
import CategoriesDetail from "./Pages/CategoriesDetail";

function App() {
    return (
        <BrowserRouter>
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/courses/:slug" element={<CoursesDetail />} />
                <Route
                    path="/categories/:slug"
                    element={<CategoriesDetail />}
                />
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
