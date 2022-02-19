import React, { useState, useCallback } from "react";
import axios from "axios";
import HumorSurvey from "../surveys/HumorSurvey";
import Thanks from "../Thanks";

const humorUrl = "http://127.0.0.1:8000/process-average-test/humor";

const HumorPage = () => {
	const [showPage, setShowPage] = useState(true);

	const onCompletePage = useCallback(
		(data) => {
			axios
				.post(humorUrl, data)
				.then((res) => console.log(res))
				.catch((err) => console.log(err));

			setShowPage(!showPage);
		},
		[showPage]
	);

	const setFinalPage = () => {
		return <Thanks />;
	};

	return (
		<div>
			{showPage ? (
				<HumorSurvey
					showCompletedPage={(data) => onCompletePage(data)}
				/>
			) : (
				setFinalPage()
			)}
		</div>
	);
};

export default HumorPage;
