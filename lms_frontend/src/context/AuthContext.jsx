import axios from "axios";
import { createContext, useEffect, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);

    const getUser = async (access) => {
        const response = await axios.get("http://127.0.0.1:8000/profile/", {
            headers: {
                Authorization: `Bearer ${access}`,
            },
        });
        setUser(response.data);
    };

    useEffect(() => {
        getUser(localStorage.getItem("access"));
    }, []);

    const login = async (formData) => {
        const response = await axios.post(
            "http://127.0.0.1:8000/login/",
            formData
        );

        const { access, refresh } = response.data;
        localStorage.setItem("access", access);
        localStorage.setItem("refresh", refresh);

        getUser(access);
    };

    const logout = () => {
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");

        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
