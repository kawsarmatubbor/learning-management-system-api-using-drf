import axios from "axios";
import { createContext, useEffect, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [access, setAccess] = useState(null);

    const getAccess = () => {
        setAccess(localStorage.getItem("access"));
    };

    useEffect(() => {
        getAccess();
    }, [access]);

    const login = async (formData) => {
        const response = await axios.post(
            "http://127.0.0.1:8000/login/",
            formData
        );

        const { access, refresh } = response.data;
        localStorage.setItem("access", access);
        localStorage.setItem("refresh", refresh);

        setAccess(access);
    };

    const logout = () => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");

        setAccess(null);
    };

    return (
        <AuthContext.Provider value={{ access, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
