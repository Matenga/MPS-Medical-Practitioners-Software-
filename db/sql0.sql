create table patient_demographics(patient_id text primary key,nid text,fullname text,dob text,home_district text,physical_address text,marital_status text,email text,phone_number text,next_of_keen text,photo text,gender text,date_of_registration text,occupation text);
create table patient_visit(visit_id text primary key,patient_id text references patient_demographics(patient_id),date_of_visit text, visit_type text);
create table patient_visitstate(visit_id text primary key,patient_visits_state text);
create table patient_age(visit_id text references patient_visit(visit_id),patient_age text,date_of_record text);
create table patient_weight(visit_id text references patient_visit(visit_id),patient_weight text,date_of_record text);
create table patientbloodpressure(visit_id text references patient_visit(visit_id),patient_blood_pressure text,date_of_record text);
create table patient_temperature(visit_id text references patient_visit(visit_id),patient_temperature text, date_of_record text);
create table patient_drug_allergy(visit_id text references patient_visit(visit_id),drug text,date_of_record text);
create table patient_current_status(patient_id text references patient_demographics(patient_id),current_status text);
create table staff_demographics(staff_id text primary key, full_name text,gender text,marital_status text,dob text,physical_address text,date_of_employment text, jod_designation text, phone_number text, date_of_registration text,nationality text,home_district text,nid text);
create table out_going_call(call_id text primary key, caller text references staff_demographics(staff_id),reciever text,timeofcall text);
create table in_coming_call(call_id text primary key, caller text,reciever text references staff_demographics(staff_id));
create table message(message_id text primary key,sender text references staff_demographics(staff_id),reciever text references staff_demographics(staff_id),message_subject text, message_body text, date_of_send text,date_of_reception text);
create table department(department_id text primary key, department_name text);
create table department_head(department_id text references department(department_id),staff_id text references staff_demographics(staff_id),date_of_assignment text);
create table current_department_head(department_id text references department(department_id),staff_id text references staff_demographics(staff_id),date_of_assignment text);
create table queue(queue_id text primary key,staff_id text references staff_demographics(staff_id),queue_type text,date_of_creation text,queue_size text);
create table queue_patient_rel(queue_id text references queue(queue_id),visit_id text references patient_visit(visit_id));
create table queue_status(queue_id text references queue(queue_id),queue_status text);
create table department_staff_rel(department_id text references department(department_id),staff_id text references staff_demographics(staff_id),date_of_assignment text);
create table patient_allergy(patient_id text references patient_demographics(patient_id),allergy_name text,allergy_description text,date_of_record text);
create table patient_triage_detail(visit_id text references patient_visit(visit_id),patient_complaint text,earlier_medication text,other_physician text);
create table patient_lnmp(visit_id text references patient_visit(visit_id),lnmp text,date_of_record text);
create table staff_qualification(staff_id text references staff_demographics(staff_id),qualification_name text,document_name text, date_of_upload text, qualification_note text);
create table patient_medical_detail(patient_id text references patient_demographics(patient_id),hiv_aids text, blood_group text);
create table staff_leave_status(staff_id text references staff_demographics(staff_id),staff_leave_status text);
create table staff_leave_application(leave_id text primary key, staff_id text references staff_demographics(staff_id),application_date text,leave_reason text);
create table accepted_leave_detail(leave_id text references staff_leave_application(leave_id),on_set_date text,off_set_date text,leave_state text,date_of_acceptance text);
create table rejected_leave_detail(leave_id text references staff_leave_application(leave_id),staff_id text references staff_demographics(staff_id), rejection_reason text, date_of_reject text);
create table leave_forward(leave_id text references staff_leave_application(leave_id), staff_id text references staff_demographics(staff_id),forward_state text,forward_reason text,forward_date text);
alter table patient_demographics add column nationality text;
alter table patient_visitstate rename to patient_visit_state;
create table patient_status(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),patient_status text,date_of_status text);
alter table staff_demographics rename column jod_designation to job_designation;
alter table patient_medical_detail add column sickle_cells text;
alter table patient_medical_detail add column asthma text;
alter table patient_medical_detail add column other_complications text;
create table staff_medical_detail(staff_id text references staff_demographics(staff_id),hiv_aids text,blood_group text,sickle_cells text,asthma text,other_complication text);
alter table out_going_call rename column timeofcall to time_of_call;
alter table in_coming_call add column time_of_call text;
create table message_reciever_delete_status(message_id text references message(message_id),delete_status text);
create table message_sender_delete_status(message_id text references message(message_id),delete_status text);
alter table staff_qualification add column qualification_id text primary key;
alter table rejected_leave_detail drop column staff_id;
alter table patient_allergy add column allergy_id text primary key;
alter table staff_demographics add column appointment_id text;
create table users(username text primary key,password_ text,date_of_creation text);
alter table users add column user_type text;
alter table staff_demographics add column photo text;
create table hospital_details(hospital_name text primary key, hospital_physical_address text,hospital_registration_no text, license_no text,date_of_business_onset text,date_of_creation text);
alter table hospital_details rename to hospital_detail;
alter table hospital_detail add column hospital_logo text;
create table staff_photo(staff_id text references staff_demographics(staff_id),photo text, date_of_creation text);
create table patient_photo(staff_id text references staff_demographics(staff_id),photo text, date_of_creation text);
create table user_log_state(username text references users(username),log_state text,date_of_state text);
alter table hospital_detail add column hospital_email text, add column hospital_tel text,add column hospital_box_no text;
alter table users add column passwordState text;
alter table users rename column passwordState to password_state;
create table staff_demographics_users_rel(staff_id text references staff_demographics(staff_id),username text references users(username));
create table staffState(staff_id text references staff_demographics(staff_id),staff_state text,state_description text,date_of_onset text);
alter table staffstate rename to staff_state;
create table staff_account_state(staff_id text references staff_demographics(staff_id),account_state text, date_of_state text);
create table staff_current_account_state(staff_id text references staff_demographics(staff_id),account_state text,date_of_state text);
insert into department(department_id,department_name)VALUES('D001','TRIAGE');
insert into department(department_id,department_name)VALUES('D002','CLINIC (OPD)');
insert into department(department_id,department_name)VALUES('D003','LABORATORY');
insert into department(department_id,department_name)VALUES('D004','PHARMACY');
insert into department(department_id,department_name)VALUES('D005','STORE');
insert into department(department_id,department_name)VALUES('D100','ADMINISTRATION');
insert into department(department_id,department_name)VALUES('D101','HUMAN RESOURCES');
insert into department(department_id,department_name)VALUES('D103','INFORMATION TECHNOLOGY AND COMMUNICATION');
insert into department(department_id,department_name)VALUES('D000','FRONT DESK');
alter table staff_leave_status add column leave_status_date text;
alter table patient_demographics drop column next_of_keen;
create table patient_visit_staff_rel(visit_id text references patient_visit(visit_id),staff_id text references staff_demographics(staff_id));
create table patient_demographics_staff_rel(patient_id text references patient_demographics(patient_id),staff_id text references staff_demographics(staff_id));
create table patient_current_age(visit_id text references patient_visit(visit_id),age text, date_of_record text);
create table patient_current_weight(visit_id text references patient_visit(visit_id),patient_weight text,date_of_record text);
create table patient_current_temperature(visit_id text references patient_visit(visit_id),patient_temperature text, date_of_record text);
create table patient_current_blood_pressure(visit_id text references patient_visit(visit_id),patient_blood_pressure text, date_of_record text);
create table patient_employer(patient_id text references patient_demographics(patient_id),employer_name text,employer_address text, date_of_record text);
create table patient_current_employer(patient_id text references patient_demographics(patient_id),employer_name text,employer_address text, date_of_record text);
create table patient_next_of_keen(patient_id text references patient_demographics(patient_id),fullname text,physical_address text,mobile_phone text,date_of_record text);
create table patient_current_next_of_keen(patient_id text references patient_demographics(patient_id),fullname text,physical_address text,mobile_phone text,date_of_record text);
create table patient_physical_address(visit_id text references patient_visit(visit_id),physical_address text, date_of_record text);
create table patient_email_address(visit_id text references patient_visit(visit_id),email_address text,date_of_record text);
create table patient_phone_number(visit_id text references patient_visit(visit_id),phone_number text,date_of_record text);
create table patient_iphi(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),social_security_Number text,dob text,gender text,fullname text,physical_address text,home_phone text,work_phone text,email_address text,employer text,relationship_to_patient text, date_of_record text);
create table patient_current_iphi(patient_id text references patient_demographics(patient_id),social_security_number text, date_of_record text);
create table patient_insurance_state(patient_id text references patient_demographics(patient_id),patient_insurance_state text,date_of_record text);
create table patient_current_insurance_state(patient_id text references patient_demographics(patient_id),patient_insurance_state text,date_of_record text);
create table patient_system_review(visit_id text references patient_visit(visit_id),review_category text,review_name text,review_detail text,date_of_record text);
create table patient_previous_medication(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),medicine text,dose text,date_of_medication_onset text,date_of_medication_offset text, date_of_record text);
create table patient_other_physician_detail(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),physician_fullname text,physical_address text,mobile_phone_number text, email_address text,date_of_record text);
create table patient_current_system_review(visit_id text references patient_visit(visit_id),review_category text,review_name text,review_detail text,date_of_record text);
create table patient_laboratory_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),test_name text,test_detail text, date_of_record text);
create table patient_current_laboratory_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),test_name text,test_detail text, date_of_record text);
create table patient_medical_insurance_info(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),insurance_company_name text,insurance_state text, date_of_record text);
create table patient_current_medical_insurance_info(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),insurance_company_name text,insurance_state text, date_of_record text);
create table patient_past_surgical_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),surgery_type text,surgery_date text,surgery_description text,date_of_record text);
create table patient_family_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),relative_name text,relative_type text,condition_type text, date_of_record text);
create table patient_past_medical_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),medical_condition text,date_of_record text);
create table patient_social_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),social_condition text,condition_description text,date_of_record text);
create table patient_current_social_history(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),social_condition text,condition_description text,date_of_record text);
create table patient_visit_comment(visit_id text references patient_visit(visit_id),visit_comment text,date_of_record text);
create table patient_spouse_detail(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),spouse_name text,spouse_address text,spouse_phone_number text,date_of_record text);
create table patient_current_spouse_detail(patient_id text references patient_demographics(patient_id),visit_id text references patient_visit(visit_id),spouse_name text,spouse_address text,spouse_phone_number text,date_of_record text);
alter table patient_demographics add column social_security_number text;
alter table patient_spouse_detail drop column visit_id;
alter table patient_current_spouse_detail drop column visit_id;
alter table patient_status drop column visit_id;
