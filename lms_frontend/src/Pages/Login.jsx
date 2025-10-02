import { useContext, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

function Login() {
    const [formData, setFormData] = useState({
        phone_number: "",
        password: "",
    });
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const handelChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleReset = () => {
        setFormData({
            phone_number: "",
            password: "",
        });
    };

    const handelSubmit = async (e) => {
        e.preventDefault();
        login(formData);
        handleReset();
        navigate("/");
    };

    return (
        <div className="container login">
            <div className="login-form">
                <h1 className="container-title">Login</h1>
                <form onSubmit={handelSubmit}>
                    <div className="phone-number form-group">
                        <label htmlFor="phone-number">Phone number</label>
                        <input
                            type="number"
                            name="phone_number"
                            id="phone-number"
                            onChange={handelChange}
                            value={formData.phone_number}
                        />
                    </div>
                    <div className="password form-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            name="password"
                            id="password"
                            onChange={handelChange}
                            value={formData.password}
                        />
                    </div>
                    <button type="submit" className="button">
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
}

export default Login;
