import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { Link } from "react-router-dom";

function CategoriesDetail() {
    const { slug } = useParams();
    const [category, setCategory] = useState(null);
    const [courses, setCourses] = useState(null);

    const getCategory = async () => {
        const response = await axios(
            `http://127.0.0.1:8000/categories/${slug}`
        );
        setCategory(response.data);
    };

    const getCourses = async () => {
        const response = await axios(
            `http://127.0.0.1:8000/categories/${slug}/courses`
        );
        setCourses(response.data);
    };

    useEffect(() => {
        getCategory();
        getCourses();
    }, []);
    return (
        <div className="container">
            <h1 className="container-title">{category?.title}</h1>
            {courses && courses.length > 0 ? (
                <div className="courses">
                    {courses.map((course) => (
                        <div className="course" key={course.id}>
                            <div className="course-info">
                                <div className="thumbnail-wrapper">
                                    <img
                                        src={
                                            course.thumbnail
                                                ? `http://127.0.0.1:8000${course.thumbnail}`
                                                : "/thumbnail.png"
                                        }
                                        alt={course.title}
                                        className="thumbnail"
                                    />
                                </div>
                                <h4 className="course-title">{course.title}</h4>
                                <h2 className="course-price">
                                    {course.price} BDT
                                </h2>
                                <Link
                                    to={`/courses/${course.slug}`}
                                    className="button"
                                >
                                    Details
                                </Link>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <p>No course found.</p>
            )}
        </div>
    );
}

export default CategoriesDetail;
