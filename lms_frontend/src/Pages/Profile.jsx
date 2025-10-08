import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

function Profile() {
    const { user } = useContext(AuthContext);
    return <div className="container">{user?.phone_number}</div>;
}

export default Profile;
