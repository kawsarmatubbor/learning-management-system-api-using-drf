import { Link } from "react-router-dom";

function Header() {
    return (
        <header className="header">
            <Link to="/" className="logo">
                LMS
            </Link>
            <ul className="main-menu">
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/about">About</Link>
                </li>
                <li>
                    <Link to="/contact">Contact</Link>
                </li>
            </ul>
            <Link to="/login" className="button">
                Login
            </Link>
        </header>
    );
}

export default Header;
