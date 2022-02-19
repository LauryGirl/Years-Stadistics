import React, { useEffect, useState } from "react";
import CreativityChart from "../charts/CreativityChart";
import HumorChart from "../charts/HumorChart";
import axios from "axios";

const creativityUrl =
	"http://127.0.0.1:8000/process-years-particularities/creativity";

const humorUrl = "http://127.0.0.1:8000/process-years-particularities/humor";

const ResultPage = () => {
	const [humorData, setHumorData] = useState([]);
	const [creativityData, setCreativityData] = useState([]);

	useEffect(() => {
		axios
			.get(creativityUrl)
			.then((res) => setCreativityData(res.data))
			.catch((err) => console.log(err));

		axios
			.get(humorUrl)
			.then((res) => setHumorData(res.data))
			.catch((err) => console.log(err));
	}, []);

	return (
		<div>
			<div>
				<nav className="navbar navbar-light mb-3 p-3">
					<form className="container-fluid justify-content-start">
						<a
							href="/results"
							className="btn btn-md btn-outline-success"
							type="button"
						>
							Resultados
						</a>
					</form>
				</nav>
			</div>

			<div className="p-3">
				<CreativityChart data={creativityData} />
			</div>

			<div className="mt-5 p-4">
				<HumorChart data={humorData} />
			</div>
		</div>
	);
};

export default ResultPage;
