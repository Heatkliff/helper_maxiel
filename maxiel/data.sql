PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2020-10-17 22:31:38.466547');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2020-10-17 22:31:38.478441');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2020-10-17 22:31:38.487805');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2020-10-17 22:31:38.497705');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2020-10-17 22:31:38.518091');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2020-10-17 22:31:38.532167');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2020-10-17 22:31:38.541191');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2020-10-17 22:31:38.561669');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2020-10-17 22:31:38.574348');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2020-10-17 22:31:38.584822');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2020-10-17 22:31:38.587902');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2020-10-17 22:31:38.604242');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2020-10-17 22:31:38.615570');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2020-10-17 22:31:38.624422');
INSERT INTO django_migrations VALUES(15,'auth','0010_alter_group_name_max_length','2020-10-17 22:31:38.632728');
INSERT INTO django_migrations VALUES(16,'auth','0011_update_proxy_permissions','2020-10-17 22:31:38.639787');
INSERT INTO django_migrations VALUES(17,'auth','0012_alter_user_first_name_max_length','2020-10-17 22:31:38.647812');
INSERT INTO django_migrations VALUES(18,'base','0001_initial','2020-10-17 22:31:38.656202');
INSERT INTO django_migrations VALUES(19,'sessions','0001_initial','2020-10-17 22:31:38.666060');
INSERT INTO django_admin_log VALUES(1,'2020-10-17 23:48:32.128386','1','CommandElem object (1)','[{"added": {}}]',7,1,1);
INSERT INTO django_admin_log VALUES(2,'2020-10-18 02:29:19.397296','2','CommandElem object (2)','[{"added": {}}]',7,1,1);
INSERT INTO django_admin_log VALUES(3,'2020-10-18 03:37:50.433412','3','открыть браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(4,'2020-10-18 03:49:08.126790','4','открыть браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(5,'2020-10-18 03:50:11.028304','5','Открой браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(6,'2020-10-18 09:53:06.807807','6','открой браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(7,'2020-10-18 20:23:08.097311','7','открой браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(8,'2020-10-18 20:25:00.558396','9','открой браузер','',7,1,3);
INSERT INTO django_admin_log VALUES(9,'2020-10-18 20:25:00.783383','8','открой калькулятор','',7,1,3);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'base','commandelem');
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_commandelem','Can add command elem');
INSERT INTO auth_permission VALUES(26,7,'change_commandelem','Can change command elem');
INSERT INTO auth_permission VALUES(27,7,'delete_commandelem','Can delete command elem');
INSERT INTO auth_permission VALUES(28,7,'view_commandelem','Can view command elem');
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$216000$qjdxMoY8fvB3$i0AQmbTylMWRbzWJmBD8HLNnJp+JX30naox+c4lKB74=','2020-10-17 23:41:21.353186',1,'dev','','bahyce@gmail.com',1,1,'2020-10-17 23:41:09.204717','');
INSERT INTO base_commandelem VALUES(1,'открой youtube','action/youtube.py');
INSERT INTO base_commandelem VALUES(2,'создать команду','action/create_command.py');
INSERT INTO base_commandelem VALUES(10,'открой браузер','action/browser_KaldO3f.py');
INSERT INTO django_session VALUES('sf0vwz0ov47n9wyqdxk6npfw9rjm9vff','.eJxVjL0OwyAQg9-FuULAkXB07J5nQBw_JW1FpJBMVd-9QcrQbrY_22_m_L4Vt7e0ujmyK5Ps8puRD89UO4gPX-8LD0vd1pl4r_CTNj4tMb1uZ_fvoPhWjjWBFQpxNKjzSKCEGSKgtIhhAO3pMDlCltp4kyQo1QWS1ZIwWhDs8wWvxDaY:1kTvpB:tzM57fQuh4N8zdBS9RZMkSCuPZnG_CUd39zo0uddOos','2020-10-31 23:41:21.356790');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',19);
INSERT INTO sqlite_sequence VALUES('django_admin_log',9);
INSERT INTO sqlite_sequence VALUES('django_content_type',7);
INSERT INTO sqlite_sequence VALUES('auth_permission',28);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('base_commandelem',10);
COMMIT;
