import React from "react";
import "survey-react/survey.css";
import * as Survey from "survey-react";
import CreativityQuestions from "../questions/CreativityQuestions";

const CreativitySurvey = (prop) => {
	return (
		<Survey.Survey
			json={CreativityQuestions}
			showCompletedPage={false}
			onComplete={(data) => prop.showCompletedPage(data.valuesHash)}
		/>
	);
};

export default CreativitySurvey;
