import React from "react";

const Thanks = () => {
	return (
		<div>
			<div>
				<nav className="navbar navbar-light mb-3 p-3">
					<form className="container-fluid justify-content-start">
						<a
							href="/"
							className="btn btn-md btn-outline-success"
							type="button"
						>
							Página Principal
						</a>
					</form>
				</nav>
			</div>

			<div className="cover-container d-flex w-100 h-100 flex-column mx-auto p-3">
				<main className="text-success px-3">
					<h1>Gracias por completar el test</h1>
				</main>
			</div>
		</div>
	);
};

export default Thanks;
