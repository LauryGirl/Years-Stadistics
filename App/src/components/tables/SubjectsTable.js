import React from "react";

const SubjectsTable = ({ data, column }) => {
	return (
		<div className="table-responsive">
			<table className="table-dark table-striped table-hover table align-middle">
				<thead>
					<tr className="text-end fs-5">
						<p>Cantidad de votos obtenidos por categorías </p>
					</tr>
					<tr className="fs-5">
						{column.map((item, index) => (
							<TableHeadItem item={item} />
						))}
					</tr>
				</thead>
				<tbody>
					{data.map((item, index) => (
						<TableRow item={item} column={column} />
					))}
				</tbody>
			</table>
		</div>
	);
};

const TableHeadItem = ({ item }) => <th scope="col">{item.heading}</th>;

const TableRow = ({ item, column }) => (
	<tr className="fs-5">
		{column.map((columnItem, index) => {
			return <td>{item[`${columnItem.value}`]}</td>;
		})}
	</tr>
);

export default SubjectsTable;
