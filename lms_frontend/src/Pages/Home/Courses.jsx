import { useEffect, useState } from "react";
import axios from "axios";

function Courses() {
    const [courses, setCourses] = useState([]);

    const getCourses = async () => {
        const response = await axios.get("http://127.0.0.1:8000/courses/");
        setCourses(response.data);
    };

    useEffect(() => {
        getCourses();
    }, []);

    return (
        <>
            <h1 className="container-title">Our Courses</h1>
            <div className="courses">
                {courses.map((course) => (
                    <div className="course">
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
                            <h2 className="course-price">{course.price} BDT</h2>
                            <button type="submit" className="button">
                                Enroll now
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
}

export default Courses;
