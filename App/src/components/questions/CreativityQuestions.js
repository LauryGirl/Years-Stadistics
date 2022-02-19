const CreativityQuestions = {
	locale: "es",
	title: "¿Cuán creativo eres? ",
	pages: [
		{
			name: "page1",
			elements: [
				{
					type: "checkbox",
					name: "question1",
					title:
						"Siempre trabajo con mucha certeza de que estoy siguiendo el procedimiento correcto para resolver un problema en particular.",
					correctAnswer: ["item1"],
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question2",
					title:
						"Sería una pérdida de tiempo para mí hacer preguntas si no tuviera esperanza de obtener respuestas.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question3",
					title:
						"Me concentro más en lo que me interesa que la mayoría de la gente.",
					isRequired: true,
					choices: [
						{
							value: "4",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question4",
					title:
						"Siento que un método lógico paso a paso es mejor para resolver problemas.",
					isRequired: true,
					choices: [
						{
							value: "-2",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question5",
					title:
						"En grupos, de vez en cuando expreso opiniones que parecen desanimar a la gente.",
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question6",
					title:
						"Paso mucho tiempo pensando en lo que los demás piensan de mí.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question7",
					title:
						"Es más importante para mí hacer lo que creo que es correcto que intentar ganarme la aprobación de los demás.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question8",
					title:
						"Las personas que parecen inseguras acerca de las cosas pierden mi respeto.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question9",
					title:
						"Más que otras personas, necesito tener cosas interesantes y emocionantes.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question10",
					title: "Sé cómo controlar mis impulsos internos.",
					isRequired: true,
					choices: [
						{
							value: "1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question11",
					title:
						"Soy capaz de enfrentarme a problemas difíciles durante largos períodos de tiempo.",
					isRequired: true,
					choices: [
						{
							value: "4",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question12",
					title: "De vez en cuando me entusiasmo demasiado.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question13",
					title:
						"A menudo tengo mis mejores ideas cuando no hago nada en particular.",
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question14",
					title:
						'Confío en corazonadas intuitivas y sentimientos de "correcto" o "incorrecto" cuando avanzo hacia la solución de un problema.',
					isRequired: true,
					choices: [
						{
							value: "4",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question15",
					title:
						"Cuando resuelvo problemas, trabajo más rápido cuando analizo el problema y más lento cuando sintetizo la información que he recopilado.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question16",
					title:
						"A veces disfruto rompiendo las reglas y haciendo cosas que se supone que no debo hacer.",
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question17",
					title: "Me gustan los pasatiempos que implican coleccionar cosas.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question18",
					title:
						"Soñar despierto ha proporcionado el ímpetu para muchos de mis proyectos más importantes.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question19",
					title: "Me gusta la gente objetiva y racional.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question20",
					title:
						"Si tuviera que elegir entre dos ocupaciones distintas a la que tengo ahora, preferiría ser médico que explorador.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
			],
		},
		{
			name: "page2",
			elements: [
				{
					type: "checkbox",
					name: "question21",
					title:
						"Puedo llevarme mejor con las personas si pertenecen a la misma clase social y empresarial que yo.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question22",
					title: "Tengo un alto grado de sensibilidad estética.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question23",
					title: "Estoy impulsado a lograr un alto estatus y poder en la vida.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question24",
					title: "Me gusta la gente que está segura de sus conclusiones.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question25",
					title:
						"La inspiración no tiene nada que ver con la solución exitosa de los problemas.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question26",
					title:
						"Cuando estoy en una discusión, mi mayor placer sería que la persona que no está de acuerdo conmigo se convierta en mi amigo, incluso al precio de sacrificar mi punto de vista.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question27",
					title:
						"Estoy mucho más interesado en generar nuevas ideas que en tratar de vendérselas a otros.",
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question28",
					title:
						'Disfrutaría pasar un día entero solo, simplemente "exprimiendo" mis pensamientos.',
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question29",
					title:
						"Tiendo a evitar situaciones en las que podría sentirme inferior.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question30",
					title:
						"Al evaluar la información, la fuente es más importante para mí que el contenido.",
					isRequired: true,
					choices: [
						{
							value: "-2",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question31",
					title: "Me molesta que las cosas sean inciertas e impredecibles.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question32",
					title:
						'Me gusta la gente que sigue la regla, "los negocios antes que el placer".',
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question33",
					title:
						"El respeto por uno mismo es mucho más importante que el respeto por los demás.",
					isRequired: true,
					choices: [
						{
							value: "3",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "-1",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question34",
					title:
						"Siento que las personas que luchan por la perfección son imprudentes.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
			],
		},
		{
			name: "page3",
			elements: [
				{
					type: "checkbox",
					name: "question35",
					title:
						"Prefiero trabajar con otros en un esfuerzo de equipo en lugar de solo.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question36",
					title: "Me gusta el trabajo en el que debo influenciar a las demás.",
					isRequired: true,
					choices: [
						{
							value: "1",
							text: "Sí",
						},
						{
							value: "2",
							text: "No lo sé",
						},
						{
							value: "3",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question37",
					title:
						"Muchos problemas que encuentro en la vida no se pueden resolver en términos de soluciones correctas o incorrectas.",
					isRequired: true,
					choices: [
						{
							value: "2",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "0",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question38",
					title:
						"Para mí es importante tener un lugar para cada cosa y cada cosa en su lugar.",
					isRequired: true,
					choices: [
						{
							value: "0",
							text: "Sí",
						},
						{
							value: "1",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question39",
					title:
						"Los escritores que usan palabras extrañas e inusuales simplemente quieren presumir.",
					isRequired: true,
					choices: [
						{
							value: "-1",
							text: "Sí",
						},
						{
							value: "0",
							text: "No lo sé",
						},
						{
							value: "2",
							text: "No",
						},
					],
					colCount: 3,
					maxSelectedChoices: 1,
				},
				{
					type: "checkbox",
					name: "question40",
					title:
						"A continuación se muestra una lista de términos que describen a las personas. Elige las diez palabras que mejor te caractericen.",
					isRequired: true,
					choices: [
						{
							value: "2#energica",
							text: "enérgica",
						},
						{
							value: "1#alerta",
							text: "alerta",
						},
						{
							value: "0#persuasiva",
							text: "persuasiva",
						},
						{
							value: "2#curiosa",
							text: "curiosa",
						},
						{
							value: "2#observador",
							text: "observadora",
						},
						{
							value: "0#organizada",
							text: "organizada",
						},
						{
							value: "0#alamoda",
							text: "a la moda",
						},
						{
							value: "0#sinemociones",
							text: "sin emociones",
						},
						{
							value: "1#segurodesimismo",
							text: "seguro de sí mismo",
						},
						{
							value: "1#pensamientoabierto",
							text: "pensamiento claro",
						},
						{
							value: "2#perseverante",
							text: "perseverante",
						},
						{
							value: "0#comprensiva",
							text: "comprensiva",
						},
						{
							value: "2#original",
							text: "original",
						},
						{
							value: "2#dinamica",
							text: "dinámica",
						},
						{
							value: "0#cautelosa",
							text: "cautelosa",
						},
						{
							value: "2#autoexigente",
							text: "autoexigente",
						},
						{
							value: "0#decostumbre",
							text: "de costumbres",
						},
						{
							value: "0#refinada",
							text: "refinada",
						},
						{
							value: "2#ingeniosa",
							text: "ingeniosa",
						},
						{
							value: "2#valiente",
							text: "valiente",
						},
						{
							value: "0#egolatra",
							text: "ególatra",
						},
						{
							value: "0#eficiente",
							text: "eficiente",
						},
						{
							value: "2#independiente",
							text: "independiente",
						},
						{
							value: "0#servicial",
							text: "servicial",
						},
						{
							value: "0#severa",
							text: "severa",
						},
						{
							value: "2#perceptiva",
							text: "perceptiva",
						},
						{
							value: "0#previsible",
							text: "previsible",
						},
						{
							value: "0#agil",
							text: "ágil",
						},
						{
							value: "0#formal",
							text: "formal",
						},
						{
							value: "0#bondadosa",
							text: "bondadosa",
						},
						{
							value: "1#informal",
							text: "informal",
						},
						{
							value: "1#exhaustiva",
							text: "exhaustiva",
						},
						{
							value: "2#dedicada",
							text: "dedicada",
						},
						{
							value: "0#impulsiva",
							text: "impulsiva",
						},
						{
							value: "1#largavision",
							text: "larga visión",
						},
						{
							value: "1#determinada",
							text: "determinada",
						},
						{
							value: "0#realista",
							text: "realista",
						},
						{
							value: "1#dementeabierta",
							text: "de mente abierta",
						},
						{
							value: "0#modesta",
							text: "modesta",
						},
						{
							value: "0#diplomatica",
							text: "diplomática",
						},
						{
							value: "2#involucarada",
							text: "involucrada",
						},
						{
							value: "0#inhubida",
							text: "inhibida",
						},
						{
							value: "0#despistada",
							text: "despistada",
						},
						{
							value: "2#entusiasta",
							text: "entusiasta",
						},
						{
							value: "2#flexible",
							text: "flexible",
						},
						{
							value: "2#innovadora",
							text: "innovadora",
						},
						{
							value: "0#sociable",
							text: "sociable",
						},
						{
							value: "0#lista",
							text: "lista",
						},
						{
							value: "0agradable",
							text: "agradable",
						},
						{
							value: "0#codiciosa",
							text: "codiciosa",
						},
						{
							value: "1#inquitea",
							text: "inquieta",
						},
						{
							value: "0#practica",
							text: "práctica",
						},
						{
							value: "0#reservado",
							text: "reservado",
						},
					],
					colCount: 5,
					maxSelectedChoices: 10,
				},
			],
		},
	],
	pagePrevText: {
		default: "Atrás",
		es: "Anterior",
	},
	pageNextText: "Siguiente",
	completeText: {
		default: "Finalizar",
		es: "Completar",
	},
};

export default CreativityQuestions;
