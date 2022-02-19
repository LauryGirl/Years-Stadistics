import React from "react";
import creativityHumorPic from "../../assets/creativity-humor.jpg";

const CreativityHumorResultCard = () => {
	return (
		<div className="card bg-dark h-100 text-center">
			<img src={creativityHumorPic} alt="" />
			<div className="card-body text-light">
				<h4 className="card-title">
					Resultados de los tests de Creatividad y Humor
				</h4>
				<a
					href="/results/creativity-humor"
					className="btn btn-outline-secondary rounded-0 mt-5"
				>
					Ver
				</a>
			</div>
		</div>
	);
};

export default CreativityHumorResultCard;
