import React, { useState, useCallback } from "react";
import CreativitySurvey from "../surveys/CreativitySurvey";
import Thanks from "../Thanks";
import axios from "axios";

const creativityUrl = "http://127.0.0.1:8000/process-average-test/creativity"

const CreativityPage = () => {
	const [showPage, setShowPage] = useState(true);

	const onCompletePage = useCallback(
		(data) => {
			axios
				.post(creativityUrl, data)
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
				<CreativitySurvey showCompletedPage={(data) => onCompletePage(data)} />
			) : (
				setFinalPage()
			)}
		</div>
	);
};

export default CreativityPage;
