import React from "react";
import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js/auto";

const CreativityChart = ({ data }) => {
	if (!data.length) {
		return <div></div>;
	}

	let creativityData = [
		data[0]["no creativo"],
		data[0]["debajo promedio"],
		data[0]["promedio"],
		data[0]["encima promedio"],
		data[0]["muy creativo"],
		data[0]["excepcional"],
	];

	let reducer = (accumulator, curr) => accumulator + curr
	let sumTotal = creativityData.reduce(reducer)
	let total = `Encuestados: ${sumTotal}`
	

	return (
		<div className="CreativityChart">
			<Doughnut
				data={{
					labels: [
						"Nada de creatividad",
						"Creatividad pobre",
						"Creatividad promedio",
						"Ligeramente mejor que el promedio",
						"Buen índice de creatividad",
						"Creatividad excepcional",
					],
					datasets: [
						{
							label: "# of votes",
							data: creativityData,
							backgroundColor: [
								"rgba(128, 128, 128, 0.8)",
								"rgba(172, 115, 57, 0.8)",
								"rgba(0, 230, 115, 0.8)",
								"rgba(77, 166, 255, 0.8)",
								"rgba(255, 153, 187, 0.8)",
								"rgba(166, 77, 255, 0.9)",
							],
							borderColor: [
								"rgba(128, 128, 128, 1)",
								"rgba(172, 115, 57, 1)",
								"rgba(0, 230, 115, 1)",
								"rgba(77, 166, 255, 1)",
								"rgba(255, 153, 187, 1)",
								"rgba(166, 77, 255, 1)",
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
							position: "right",
							labels: {
								font: {
									size: 20,
								},
							},
						},
						title: {
							display: "true",
							text: "Creatividad",
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

export default CreativityChart;
