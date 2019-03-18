####保存传感器的相关信息
create table sensor_info
(
	id              int  UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	topic_name	    varchar(100),
	sensor_location					varchar(100)
)

####保存传感器数据
create table sensor_data
(
	id              int  UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	topic_name	    varchar(100),
	data_value		  varchar(100),
	data_time				varchar(14),
	received_time		varchar(14)
)
