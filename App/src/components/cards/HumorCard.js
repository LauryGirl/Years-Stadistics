import React from "react";
import humorPic from "../../assets/humor.jpg";

const HumorCard = () => {
	return (
		<div className="card bg-dark h-100 text-center">
			<img src={humorPic} alt="" />
			<div className="card-body text-light">
				<h4 className="card-title">Test de Humor</h4>
				<p className="card-text">
					El sentido del humor es una de las estrategias que más nos ayuda a
					vivir. Las personas experimentan y expresan el humor de muchas maneras
					diferentes, pero lo cierto es que todas tienen una función reparadora.
					Responda este test sobre el sentido del humor con la mayor honestidad
					y objetividad posible.
				</p>
				<a href="/survey/Humor" className="btn btn-outline-secondary rounded-0">
					Empezar
				</a>
			</div>
		</div>
	);
};

export default HumorCard;
