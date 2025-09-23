import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
    const [formData, setFormData] = useState({
        phone_number: "",
        password: "",
    });
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
        const response = await axios.post(
            "http://127.0.0.1:8000/login/",
            formData
        );

        handleReset();

        const { access, refresh } = response.data;

        localStorage.setItem("access", access);
        localStorage.setItem("refresh", refresh);

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
