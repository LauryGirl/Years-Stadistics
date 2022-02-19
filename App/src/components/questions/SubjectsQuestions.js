const SubjectsQuestions = {
	locale: "es",
	title: "Sobre las asignaturas cursadas",
	pages: [
		{
			name: "SubjectsSurvey",
			elements: [
				{
					type: "matrix",
					name: "subjects",
					title: "¿Qué sentimientos te causaron las siguientes asignaturas?  ",
					isRequired: true,
					columns: ["Me gustó", "Meh...", "No me gustó"],
					rows: [
						"Lógica",
						"Álgebra I",
						"Análisis Matemático I",
						"Programación",
						"Filosofía y Sociedad",
						"Educación Física I",
						"Álgebra II",
						"Análisis Matemático II",
						"Historia de Cuba",
						"Economía Política",
						"Educación Física II",
					],
					isAllRowRequired: true,
				},
			],
		},
	],
};

export default SubjectsQuestions;
