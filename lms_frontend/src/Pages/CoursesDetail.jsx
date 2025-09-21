import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function CoursesDetail() {
    const { slug } = useParams();
    const [course, setCourses] = useState({});

    const getCourse = async () => {
        const response = await axios(`http://127.0.0.1:8000/courses/${slug}`);
        setCourses(response.data);
    };

    useEffect(() => {
        getCourse();
    }, []);

    return (
        <div className="container">
            <div className="course-detail">
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
                <div className="course-detail-info">
                    <h1 className="course-detail-title">{course.title}</h1>
                    {course.description && (
                        <p className="course-detail-description">
                            {course.description}
                        </p>
                    )}
                    <h2 className="course-price">{course.price} BDT</h2>
                    <button type="submit" className="button">
                        Enroll now
                    </button>
                </div>
            </div>
        </div>
    );
}

export default CoursesDetail;
