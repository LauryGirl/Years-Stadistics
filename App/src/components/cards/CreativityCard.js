import React from "react";
import creativityPic from "../../assets/creativity.jpg";

const CreativityCard = () => {
	return (
		<div className="card bg-dark h-100 text-center">
			<img src={creativityPic} alt="" />
			<div className="card-body text-light">
				<h4 className="card-title">Test de Creatividad</h4>
				<p className="card-text">
					¿Qué tan creativo eres? El siguiente test determina si tienes los
					rasgos de personalidad, actitudes, motivaciones e intereses que
					caracterizan la creatividad. Se basa en el estudio de varios años de
					los atributos que poseen hombres y mujeres en una variedad de campos y
					ocupaciones que piensan y actúan creativamente.
				</p>
				<a
					href="/survey/Creativity"
					className="btn btn-outline-secondary rounded-0"
				>
					Empezar
				</a>
			</div>
		</div>
	);
};

export default CreativityCard;
