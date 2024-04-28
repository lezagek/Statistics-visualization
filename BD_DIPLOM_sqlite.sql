BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "student_group" (
	"group_id"	INTEGER,
	"group_name"	CHAR(15) UNIQUE,
	"group_majority"	VARCHAR(10),
	PRIMARY KEY("group_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "education_year" (
	"education_year_id"	INTEGER,
	"teacher_id"	INTEGER,
	"group_id"	INTEGER,
	PRIMARY KEY("education_year_id"),
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE,
	FOREIGN KEY("group_id") REFERENCES "student_group"("group_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "subgroup" (
	"subgroup_id"	INTEGER,
	"group_id"	INTEGER,
	"subgroup_num"	INTEGER,
	"teacher_id"	INTEGER,
	PRIMARY KEY("subgroup_id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "student_group"("group_id") ON DELETE CASCADE,
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "key_template" (
	"key_template_id"	INTEGER,
	"key_template_name"	VARCHAR(10),
	PRIMARY KEY("key_template_id")
);
CREATE TABLE IF NOT EXISTS "tree_type" (
	"tree_type_id"	INTEGER,
	"tree_type_name"	CHAR(3),
	PRIMARY KEY("tree_type_id")
);
CREATE TABLE IF NOT EXISTS "tree_template" (
	"tree_template_id"	INTEGER,
	"tree_type_id"	INTEGER,
	"key_template_id"	INTEGER,
	"tree_template_height"	INTEGER,
	"tree_template_keys_amount"	INTEGER,
	"tree_template_difficulty"	FLOAT,
	"teacher_id"	INTEGER,
	PRIMARY KEY("tree_template_id" AUTOINCREMENT),
	FOREIGN KEY("key_template_id") REFERENCES "key_template"("key_template_id") ON DELETE CASCADE,
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE,
	FOREIGN KEY("tree_type_id") REFERENCES "tree_type"("tree_type_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "input_template" (
	"input_template_id"	INTEGER,
	"is_tree"	INTEGER,
	"key_template_id"	INTEGER,
	PRIMARY KEY("input_template_id" AUTOINCREMENT),
	FOREIGN KEY("key_template_id") REFERENCES "key_template"("key_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "output_template" (
	"output_template"	INTEGER,
	"is_tree"	INTEGER,
	"key_template_id"	INTEGER,
	PRIMARY KEY("output_template" AUTOINCREMENT),
	FOREIGN KEY("key_template_id") REFERENCES "key_template"("key_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "suboperation_template" (
	"suboperation_template_id"	INTEGER,
	"suboperation_name"	VARCHAR(20),
	"input_template_id"	INTEGER,
	"output_template_id"	INTEGER,
	"suboperation_template_difficulty"	FLOAT,
	"suboperation_template_score"	FLOAT,
	"suboperation_text"	VARCHAR(50),
	PRIMARY KEY("suboperation_template_id" AUTOINCREMENT),
	FOREIGN KEY("output_template_id") REFERENCES "output_template"("output_template_id") ON DELETE CASCADE,
	FOREIGN KEY("input_template_id") REFERENCES "input_template"("input_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "operation_suboperation_template" (
	"operation_template_id"	INTEGER,
	"suboperation_template_id"	INTEGER,
	PRIMARY KEY("operation_template_id","suboperation_template_id"),
	FOREIGN KEY("suboperation_template_id") REFERENCES "suboperation_template"("suboperation_template_id") ON DELETE CASCADE,
	FOREIGN KEY("operation_template_id") REFERENCES "operation_template"("operation_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "formula" (
	"formula_id"	INTEGER,
	"formula_body"	VARCHAR(80),
	PRIMARY KEY("formula_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "task_template" (
	"task_template_id"	INTEGER,
	"task_template_bar"	INTEGER,
	"formula_id"	INTEGER,
	"task_template_difficulty"	FLOAT,
	"teacher_id"	INTEGER,
	"tree_template_id"	INTEGER,
	"operation_template_id"	INTEGER,
	PRIMARY KEY("task_template_id" AUTOINCREMENT),
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE,
	FOREIGN KEY("formula_id") REFERENCES "formula"("formula_id") ON DELETE CASCADE,
	FOREIGN KEY("operation_template_id") REFERENCES "operation_template"("operation_template_id") ON DELETE CASCADE,
	FOREIGN KEY("tree_template_id") REFERENCES "tree_template"("tree_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "test_template" (
	"test_template_id"	INTEGER,
	"test_template_difficulty"	FLOAT,
	"teacher_id"	INTEGER,
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE,
	PRIMARY KEY("test_template_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "test_task_template" (
	"test_template_id"	INTEGER,
	"task_template_id"	INTEGER,
	FOREIGN KEY("test_template_id") REFERENCES "test_template"("test_template_id") ON DELETE CASCADE,
	FOREIGN KEY("task_template_id") REFERENCES "task_template"("task_template_id") ON DELETE CASCADE,
	PRIMARY KEY("test_template_id","task_template_id")
);
CREATE TABLE IF NOT EXISTS "testing_session" (
	"testing_session_id"	INTEGER,
	"testing_session_name"	VARCHAR(30),
	"testing_session_date"	DATE,
	"testing_session_begin_time"	TIME,
	"testing_session_end_time"	TIME,
	"formula_id"	INTEGER,
	"teacher_id"	INTEGER,
	"test_template_id"	INTEGER,
	"test_template_bar"	INTEGER,
	FOREIGN KEY("teacher_id") REFERENCES "teacher"("teacher_id") ON DELETE CASCADE,
	FOREIGN KEY("test_template_id") REFERENCES "test_template"("test_template_id") ON DELETE CASCADE,
	FOREIGN KEY("formula_id") REFERENCES "formula"("formula_id") ON DELETE CASCADE,
	PRIMARY KEY("testing_session_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "student_testing_session" (
	"student_testing_session_id"	INTEGER,
	"student_id"	CHAR(6),
	FOREIGN KEY("student_id") REFERENCES "student"("student_id") ON DELETE CASCADE,
	PRIMARY KEY("student_testing_session_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "test" (
	"test_id"	INTEGER,
	"test_template_id"	INTEGER,
	"test_mark"	INTEGER,
	"test_date"	DATE,
	"test_time_begin"	TIME,
	"test_time_end"	TIME,
	"student_id"	CHAR(6),
	"testing_session_id"	INTEGER,
	FOREIGN KEY("student_id") REFERENCES "student"("student_id") ON DELETE CASCADE,
	FOREIGN KEY("test_template_id") REFERENCES "test_template"("test_template_id") ON DELETE CASCADE,
	FOREIGN KEY("testing_session_id") REFERENCES "testing_session"("testing_session_id") ON DELETE CASCADE,
	PRIMARY KEY("test_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "operation_template" (
	"operation_template_id"	INTEGER,
	"operation_name"	VARCHAR(20),
	"input_template_id"	INTEGER,
	"output_template_id"	INTEGER,
	"operation_template_difficulty"	FLOAT,
	"operation_template_score"	FLOAT,
	"operation_text"	VARCHAR(50),
	"tree_type_id"	INTEGER,
	FOREIGN KEY("output_template_id") REFERENCES "output_template"("output_template_id") ON DELETE CASCADE,
	FOREIGN KEY("input_template_id") REFERENCES "input_template"("input_template_id") ON DELETE CASCADE,
	FOREIGN KEY("tree_type_id") REFERENCES "tree_type"("tree_type_id") ON DELETE CASCADE,
	PRIMARY KEY("operation_template_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "input" (
	"input_id"	INTEGER,
	"input_data"	VARCHAR(50),
	"input_template_id"	INTEGER,
	"node_action"	CHAR(50),
	FOREIGN KEY("input_template_id") REFERENCES "input_template"("input_template_id") ON DELETE CASCADE,
	PRIMARY KEY("input_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "output" (
	"output_id"	INTEGER,
	"output_data"	VARCHAR(50),
	"output_template_id"	INTEGER,
	FOREIGN KEY("output_template_id") REFERENCES "output_template"("output_template") ON DELETE CASCADE,
	PRIMARY KEY("output_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS " task" (
	"task_id"	INTEGER,
	"task_template_id"	INTEGER,
	"test_id"	INTEGER,
	"tree_template_id"	INTEGER,
	"input_id"	INTEGER,
	"output_id"	INTEGER,
	"task_score"	FLOAT,
	FOREIGN KEY("task_template_id") REFERENCES "task_template"("task_template_id") ON DELETE CASCADE,
	FOREIGN KEY("test_id") REFERENCES "test"("test_id") ON DELETE CASCADE,
	FOREIGN KEY("input_id") REFERENCES "input"("input_id") ON DELETE CASCADE,
	FOREIGN KEY("output_id") REFERENCES "output"("output_id") ON DELETE CASCADE,
	PRIMARY KEY("task_id" AUTOINCREMENT),
	FOREIGN KEY("tree_template_id") REFERENCES "tree_template"("tree_template_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "suboperation" (
	"suboperation_id"	INTEGER,
	"input_id"	INTEGER,
	"output_id"	INTEGER,
	"suboperation_template_id"	INTEGER,
	"task_id"	INTEGER,
	"suboperation_score"	FLOAT,
	PRIMARY KEY("suboperation_id" AUTOINCREMENT),
	FOREIGN KEY("task_id") REFERENCES " task"("task_id") ON DELETE CASCADE,
	FOREIGN KEY("suboperation_template_id") REFERENCES "suboperation_template"("suboperation_template_id") ON DELETE CASCADE,
	FOREIGN KEY("input_id") REFERENCES "input"("input_id") ON DELETE CASCADE,
	FOREIGN KEY("output_id") REFERENCES "output"("output_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "teacher" (
	"teacher_id"	INTEGER,
	"teacher_name"	VARCHAR(50),
	"teacher_login"	VARCHAR(50),
	"teacher_password"	VARCHAR(50),
	PRIMARY KEY("teacher_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "student" (
	"student_id"	CHAR(6),
	"student_name"	VARCHAR(50),
	"subgroup_id"	INTEGER,
	"student_login"	VARCHAR(50),
	"student_password"	VARCHAR(50),
	PRIMARY KEY("student_id"),
	FOREIGN KEY("subgroup_id") REFERENCES "subgroup"("subgroup_id") ON DELETE CASCADE
);
INSERT INTO "student_group" ("group_id","group_name","group_majority") VALUES (1,'Б9120-09.03.04','прогин'),
 (2,'Б9122-09.03.04','прогин');
INSERT INTO "education_year" ("education_year_id","teacher_id","group_id") VALUES (1,1,1),
 (2,2,2);
INSERT INTO "subgroup" ("subgroup_id","group_id","subgroup_num","teacher_id") VALUES (1,1,1,1),
 (2,2,1,2);
INSERT INTO "key_template" ("key_template_id","key_template_name") VALUES (1,'Числовой'),
 (2,'Строковый');
INSERT INTO "tree_type" ("tree_type_id","tree_type_name") VALUES (1,'БДП'),
 (2,'АВЛ');
INSERT INTO "teacher" ("teacher_id","teacher_name","teacher_login","teacher_password") VALUES (1,'Остроухова Светлана Николаевна',NULL,NULL),
 (2,'Крестникова Ольга Александровна',NULL,NULL);
INSERT INTO "student" ("student_id","student_name","subgroup_id","student_login","student_password") VALUES ('111111','Доржиев Арсалан Сенгэевич',1,NULL,NULL),
 ('111112','Чемериская Елизавета Вячеславовна',1,NULL,NULL),
 ('111113','Шулятьев Артём Андреевич',1,NULL,NULL);
COMMIT;
