####���洫�����������Ϣ
create table sensor_info
(
	id              int  UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	topic_name	    varchar(100),
	sensor_location					varchar(100)
)

####���洫��������
create table sensor_data
(
	id              int  UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	topic_name	    varchar(100),
	data_value		  varchar(100),
	data_time				varchar(14),
	received_time		varchar(14)
)
