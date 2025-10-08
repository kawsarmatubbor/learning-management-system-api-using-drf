import { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

function Header() {
    const { user, logout } = useContext(AuthContext);

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
            {user ? (
                <div className="button-wrapper">
                    <Link to="/profile" className="button">
                        Profile
                    </Link>
                    <button className="button secondary" onClick={logout}>
                        Logout
                    </button>
                </div>
            ) : (
                <Link to="/login" className="button">
                    Login
                </Link>
            )}
        </header>
    );
}

export default Header;
