import React from "react";
import { Route, Routes } from "react-router-dom";
import "./App.css";

import Nothing from "./components/Nothing";
import HumorPage from "./components/pages/HumorPage";
import AllSurveysPage from "./components/pages/AllSurveysPage";
import CreativityPage from "./components/pages/CreativityPage";
import FreeTimePage from "./components/pages/FreeTimePage";
import SubjectsPage from "./components/pages/SubjectsPage";

import ResultPage from "./components/pages/ResultPage";
import CreativityHumorResultPage from "./components/pages/CreativityHumorResultPage";
import FreeTimeResultPage from "./components/pages/FreeTimeResultPage";
import SubjectsResultPage from "./components/pages/SubjectsResultPage";

function App() {
	return (
		<div className="App bg-dark">
			<div>
				<Routes>
					<Route path="/" element={<AllSurveysPage />} />
					<Route path="/survey/Creativity" element={<CreativityPage />} />
					<Route path="/survey/Humor" element={<HumorPage />} />
					<Route path="/survey/FreeTime" element={<FreeTimePage />} />
					<Route path="/survey/Subjects" element={<SubjectsPage />} />
					<Route path="/results/" element={<ResultPage />} />
					<Route path="results/free-time" element={<FreeTimeResultPage />} />
					<Route path="results/subjects" element={<SubjectsResultPage />} />
					<Route
						path="results/creativity-humor"
						element={<CreativityHumorResultPage />}
					/>

					<Route path="*" element={<Nothing />} />
				</Routes>
			</div>
		</div>
	);
}

export default App;
