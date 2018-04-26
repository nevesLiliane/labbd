DROP TABLE IF EXISTS dataset_schema;
DROP TABLE IF EXISTS hyperparameter_value;
DROP TABLE IF EXISTS exec_data_transform;
DROP TABLE IF EXISTS parameter_tuning;
DROP TABLE IF EXISTS user_action;
DROP TABLE IF EXISTS adapter;
DROP TABLE IF EXISTS hyperparameterVariation_tuned;
DROP TABLE IF EXISTS hv_tuning;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS hyperparameter;
DROP TABLE IF EXISTS combination_result;
DROP TABLE IF EXISTS parameter_grid;
DROP TABLE IF EXISTS hv_block;
DROP TABLE IF EXISTS hv;
DROP TABLE IF EXISTS block;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS experiment;

CREATE TABLE experiment( --dominio
	e_id SERIAL,
	split_size INTEGER,
	date_start TIMESTAMP
);
CREATE TABLE task(
	t_id serial,
	start_time TIMESTAMP,
	end_time TIMESTAMP
);
CREATE TABLE block(
	b_id INTEGER,
	e_id INTEGER,
	FOREIGN KEY(e_id) REFERENCES experiment(e_id)
);
CREATE TABLE hv(
	hv_id serial,
	learn_rate_variation VARCHAR(50),
	epoch_variation VARCHAR(50),
	optimizer_variation VARCHAR(50),
	init_mode_variation VARCHAR(50),
	batch_size_variation VARCHAR(50),
	momentum_variation VARCHAR(50)
);
CREATE TABLE parameter_grid(
	id serial,
	t_id INTEGER,
	hv_id INTEGER,
	epoch_in_grid VARCHAR(50),
	learn_rate_in_grid VARCHAR(50),
	optimizer_in_grid VARCHAR(50),
	init_mode_in_grid VARCHAR(50),
	batch_size_in_grid VARCHAR(50),
	momentum_in_grid VARCHAR(50),
	FOREIGN KEY(hv_id) REFERENCES hv(hv_id),
	FOREIGN KEY(t_id) REFERENCES task(t_id)
);
CREATE TABLE combination_result( --dominio
	id SERIAL,
	learn_rate_used REAL,
	epoch_used INTEGER,
	batch_size_used INTEGER,
	init_mode_used REAL,
	momentum_used VARCHAR(50),
	optimizer_used VARCHAR(50),
	AUC REAL,
	accuracy REAL,
	precision REAL,
	recall REAL,
	f1_score INTEGER,
	pg_id INTEGER,
	FOREIGN KEY(pg_id) REFERENCES parameter_grid(id)
);
CREATE TABLE hyperparameter(
	id SERIAL,
	h_name VARCHAR(50),
	hv_id INTEGER,
	FOREIGN KEY(hv_id) REFERENCES hv(hv_id)
);
CREATE TABLE person(
	p_id SERIAL
);
CREATE TABLE hv_tuning(
	hvt_id SERIAL,
	hv_modified INTEGER,
	p_id INTEGER,
	start_time TIMESTAMP,
	FOREIGN KEY(hv_modified) REFERENCES hv(hv_id),
	FOREIGN KEY(p_id) REFERENCES person(p_id)
);
CREATE TABLE hyperparameterVariation_tuned(
	h_id INTEGER,
	hvt_id INTEGER,
	old_hp_variation VARCHAR(50),
	new_hp_variation VARCHAR(50),
	FOREIGN KEY(h_id) REFERENCES hyperparameter(h_id),
	FOREIGN KEY(hvt_id) REFERENCES hv_tuning(hvt_id)
);
CREATE TABLE adapter(--???
	a_id SERIAL,
	PATH VARCHAR(50),
	version REAL

);
CREATE TABLE exec_data_transform(
	id SERIAL,
	block_id INTEGER,
	FOREIGN KEY(block_id) REFERENCES block(b_id)
);
CREATE TABLE hyperparameter_value( --adaptação
	id SERIAL,
	learn_rate VARCHAR(100),
	epoch VARCHAR(100),
	batch_size VARCHAR(100),
	init_mode VARCHAR(50),
	momentum VARCHAR(50),
	optimizer VARCHAR(100),
	e_id INTEGER,
	FOREIGN KEY(e_id) REFERENCES experiment(e_id)
);
CREATE TABLE dataset_schema( --dominio
	ds_id SERIAL,
	experiment_id INTEGER,
	FOREIGN KEY(experiment_id) REFERENCES experiment(e_id)
);