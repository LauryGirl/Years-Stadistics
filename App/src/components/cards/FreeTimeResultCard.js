import React from "react";
import freeTimePic from "../../assets/freetimeResult.jpg";

const FreeTimeResultCard = () => {
	return (
		<div className="card bg-dark h-100 text-center">
			<img src={freeTimePic} alt="" />
			<div className="card-body text-light">
				<h4 className="card-title">Resultados del test de Tiempo Libre</h4>
				<a
					href="/results/free-time"
					className="btn btn-outline-secondary rounded-0 mt-5"
				>
					Ver
				</a>
			</div>
		</div>
	);
};

export default FreeTimeResultCard;
