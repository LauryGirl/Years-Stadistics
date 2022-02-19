import React from "react";
import "survey-react/survey.css";
import * as Survey from "survey-react";
import FreeTimeQuestions from "../questions/FreeTimeQuestions";

const FreeTimeSurvey = (prop) => {
	return (
		<Survey.Survey
			json={FreeTimeQuestions}
			showCompletedPage={false}
			onComplete={(data) => prop.showCompletedPage(data.valuesHash)}
		/>
	);
};

export default FreeTimeSurvey;
