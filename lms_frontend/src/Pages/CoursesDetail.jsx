import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

function CoursesDetail() {
    const { slug } = useParams();
    const [course, setCourses] = useState(null);
    const [modules, setModules] = useState(null);
    const [teachers, setTeachers] = useState(null);

    const getCourse = async () => {
        const response = await axios.get(
            `http://127.0.0.1:8000/courses/${slug}/`
        );
        setCourses(response.data);
    };

    const getModules = async () => {
        const response = await axios.get(
            `http://127.0.0.1:8000/courses/${slug}/modules/`
        );
        setModules(response.data);
    };

    const getTeachers = async () => {
        const response = await axios.get(
            `http://127.0.0.1:8000/courses/${slug}/teachers/`
        );
        setTeachers(response.data);
    };

    useEffect(() => {
        getCourse();
        getModules();
        getTeachers();
    }, []);
    console.log(teachers);
    return (
        <div className="container">
            {course ? (
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
            ) : (
                <p>No course found</p>
            )}

            <div className="modules">
                <h1 className="container-title">Modules</h1>
                <ul>
                    {modules && modules.length > 0 ? (
                        modules.map((module) => (
                            <li key={module.id}>
                                <h3>{module.title}</h3>
                                {module.description && (
                                    <p>{module.description}</p>
                                )}
                            </li>
                        ))
                    ) : (
                        <li>No module found</li>
                    )}
                </ul>
            </div>

            <div className="teachers">
                <h1 className="container-title">Teachers</h1>
                <ul>
                    {teachers && teachers.length > 0 ? (
                        teachers.map((teacher) => (
                            <li key={teacher.id}>
                                <h3>
                                    {teacher.first_name} {teacher.last_name}
                                </h3>
                            </li>
                        ))
                    ) : (
                        <li>No teacher found</li>
                    )}
                </ul>
            </div>
        </div>
    );
}

export default CoursesDetail;
