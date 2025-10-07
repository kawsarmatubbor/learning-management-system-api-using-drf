import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function Categories() {
    const [categories, setCategories] = useState([]);

    const getCategories = async () => {
        const response = await axios.get("http://127.0.0.1:8000/categories/");
        setCategories(response.data);
    };

    useEffect(() => {
        getCategories();
    }, []);

    return (
        <div className="container">
            <h1 className="container-title">Categories</h1>
            <div className="categories">
                {categories.map((category) => (
                    <Link
                        to={`/categories/${category.slug}`}
                        className="category"
                        key={category.id}
                    >
                        {category.title}
                    </Link>
                ))}
            </div>
        </div>
    );
}

export default Categories;
