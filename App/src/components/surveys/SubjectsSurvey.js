import React from "react";
import "survey-react/survey.css";
import * as Survey from "survey-react";
import SubjectsQuestions from "../questions/SubjectsQuestions";

const SubjectsSurvey = (prop) => {
	return (
		<Survey.Survey
			json={SubjectsQuestions}
			showCompletedPage={false}
			onComplete={(data) => prop.showCompletedPage(data.valuesHash)}
		/>
	);
};

export default SubjectsSurvey;
