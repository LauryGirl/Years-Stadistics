import React from "react";
import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

const HumorChart = ({ data }) => {
	if (!data.length) {
		return <div></div>;
	}

	let humorData = [
		data[0].serio,
		data[0].pobre,
		data[0].justo,
		data[0].promedio,
		data[0].excelente,
	];

	let reducer = (accumulator, curr) => accumulator + curr;
	let sumTotal = humorData.reduce(reducer);
	let total = `Encuestados: ${sumTotal}`;

	return (
		<div className="HumorChart">
			<Doughnut
				data={{
					labels: [
						"Sufre de seriositis crónica",
						"Deficiencia del sentido del humor",
						"Sentido del humor un poco deteriorado",
						"Sentido del humor promedio y saludable",
						"Excelente sentido del humor y actitud",
					],
					datasets: [
						{
							label: "# of votes",
							data: humorData,
							backgroundColor: [
								"rgba(255, 0, 0, 0.7)",
								"rgba(255, 159, 64, 0.8)",
								"rgba(255, 255, 102, 0.8)",
								"rgba(54, 162, 235, 0.8)",
								"rgba(92, 214, 92, 0.8)",
							],
							borderColor: [
								"rgba(255, 0, 0, 1)",
								"rgba(255, 159, 64, 1)",
								"rgba(255, 255, 102, 1)",
								"rgba(54, 162, 235, 1)",
								"rgba(92, 214, 92, 1)",
							],
							borderWidth: 2,
						},
					],
				}}
				height={400}
				width={600}
				options={{
					maintainAspectRatio: false,
					plugins: {
						legend: {
							position: "left",
							labels: {
								font: {
									size: 20,
								},
							},
						},
						title: {
							display: "true",
							text: "Sentido del Humor",
							position: "top",
							font: {
								size: 28,
							},
						},
						subtitle: {
							display: "true",
							text: total,
							position: "bottom",
							font: {
								size: 21,
							},
						},
					},
				}}
			/>
		</div>
	);
};

export default HumorChart;
