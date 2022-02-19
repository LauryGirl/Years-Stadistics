import React from "react";
import subjectsPic from "../../assets/subjects.jpg";

const SubjectsCard = () => {
	return (
		<div className="card bg-dark h-100 text-center">
			<img src={subjectsPic} alt="" />
			<div className="card-body text-light">
				<h4 className="card-title">Test de Asignaturas</h4>
				<p className="card-text">
					Las asignaturas de cada curso fomentan tu formación integral. Los
					conocimientos adquiridos no solo tendrán una aplicación potencial en
					el ámbito laboral, sino que tienen un alcance práctico en el marco de
					la vida diaria. Déjanos saber la impresión que te causaron las
					asignaturas del test.
				</p>
				<a
					href="/survey/Subjects"
					className="btn btn-outline-secondary rounded-0"
				>
					Empezar
				</a>
			</div>
		</div>
	);
};

export default SubjectsCard;
