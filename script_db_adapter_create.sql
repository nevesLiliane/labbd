CREATE TABLE dataset_schema(
	ds_id serial,
	dataflow_id INTEGER,
	FOREIGN KEY(dataflow_id) REFERENCES dataflow(df_id)
);

CREATE TABLE adapter(
	a_id serial,
	command_template VARCHAR(50),
	type VARCHAR(10),
	dataset_sch_id INTEGER,
	FOREIGN KEY(dataset_sch_id) REFERENCES dataset_schema(ds_id)
);

CREATE TABLE dataset(
	data_element_id serial,
	ds_id INTEGER,
	previous_task_id INTEGER,
	next_task_id INTEGER,
	FOREIGN KEY(ds_id) REFERENCES dataset_schema(ds_id)
);