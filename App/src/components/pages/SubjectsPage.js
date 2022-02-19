import React, { useState, useCallback } from "react";
import SubjectsSurvey from "../surveys/SubjectsSurvey";
import Thanks from "../Thanks";
import axios from "axios";

const subjectsUrl = "http://127.0.0.1:8000/process-subject-test/";

const SubjectsPage = () => {
	const [showPage, setShowPage] = useState(true);

	const onCompletePage = useCallback(
		(data) => {
			axios
				.post(subjectsUrl, data)
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
				<SubjectsSurvey
					showCompletedPage={(data) => onCompletePage(data)}
				/>
			) : (
				setFinalPage()
			)}
		</div>
	);
};

export default SubjectsPage;
