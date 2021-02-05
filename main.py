import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


#
#  Bloque de informacion de agencias
#

@app.route('/agency/add', methods=['POST'])
def add_agency():
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_managerId = _json['managerId']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		_certification = _json['certification']
		_customerId = _json['customerId']
		_moreInfo = _json['moreInfo']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and _email and request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_agency_model (name, address, managerId, vat, email, phone, certification, customerId, moreInfo, ids, version) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
			data = (_name, _address, _managerId, _vat, _email, _phone, _certification, _customerId, _moreInfo, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Agency added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agencies')
def agencys():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_agency_model ORDER BY id DESC')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agenciesperclient')
def agencys_per_client():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_agency_model WHERE certification NOT LIKE %disinstallato% ORDER BY id DESC')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/agency/<string:customerId>')
def agencyCustomer(customerId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT id, name, address, managerId, certification, email, phone, vat FROM n_nemesis_n_agency_model WHERE customerId =%s', customerId)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agency/<int:agencyId>')
def agencyId(agencyId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT id, name, address, managerId, certification, email, phone, vat FROM n_nemesis_n_agency_model WHERE id =%s', agencyId)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agency/<string:name>')
def agency(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_agency_model WHERE name=%s", name)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agency/update', methods=['POST'])
def update_agency():
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_managerId = _json['managerId']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		_certification = _json['certification']
		_customerId = _json['customerId']
		_moreInfo = _json['moreInfo']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and _email and request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_agency_model SET name=%s, address=%s, managerId=%s, vat=%s, mail=%s, phone=%s, certification=%s, customerId=%s, moreInfo=%s, ids=%s, version=%s WHERE id=%s"
			data = (_name, _address, _managerId, _vat, _email, _phone, _certification, _customerId, _moreInfo, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Agency updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/agency/delete/<string:name>')
def delete_agency(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_agency_model WHERE name=%s", (name,))
		conn.commit()
		resp = jsonify('Agency deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

#
#  Bloque de informacion de contacts
#

@app.route('/contact/add', methods=['POST'])
def add_contact():
	try:
		_json = request.json
		_name = _json['name']
		_surname = _json['surname']
		_taxCode = _json['taxCode']
		_address = _json['address']
		_phone = _json['phone']
		_user = _json['user']
		_customerId = _json['customerId']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = "INSERT INTO n_nemesis_n_contact_model (name, surname, taxCode, address, phone, user, customerId, ids, version) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
			data = (_name, _surname, _taxCode, _address, _phone, _user, _customerId, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Contact added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/contact')
def contacts():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_contact_model ORDER BY id DESC")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/contact/<string:name>')
def contact(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_contact_model WHERE name=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/contact/update', methods=['POST'])
def update_contact():
	try:
		_json = request.json
		_json = request.json
		_name = _json['name']
		_surname = _json['surname']
		_taxCode = _json['taxCode']
		_address = _json['address']
		_phone = _json['phone']
		_user = _json['user']
		_customerId = _json['customerId']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_contact_model SET name=%s, surname=%s, taxCode=%s, address=%s, phone=%s, user=%s, customerId=%s, ids=%s, version=%s WHERE id=%s"
			data = (_name, _surname, _taxCode, _address, _phone, _user, _customerId, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Contact updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/contact/delete/<string:name>')
def delete_contact(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_contact_model WHERE name=%s", (name,))
		conn.commit()
		resp = jsonify('Contact deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


#
#  Bloque de informacion de customers
#

@app.route('/customer/add', methods=['POST'])
def add_customer():
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and _email and request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_customer_model (name, address, vat, email, phone, ids, version) VALUES(%s, %s, %s, %s, %s, %s, %s)'
			data = (_name, _address, _vat, _email, _phone, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Contact added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/customers')
def customers():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_customer_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/customeriso/<int:id>')
def customerIso(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_customer_model WHERE id=%s', id)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/customer/<string:name>')
def customer(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_customer_model WHERE name=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/customer/update', methods=['POST'])
def update_customer():
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and _email and request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_customer_model SET name=%s, address=%s, vat=%s, mail=%s, phone=%s, ids=%s, version=%s WHERE id=%s"
			data = (_name, _address, _vat, _email, _phone, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Customer updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/customer/delete/<string:name>')
def delete_customer(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_customer_model WHERE name=%s", (name,))
		conn.commit()
		resp = jsonify('Customer deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()



# # BLOQUE EQUIPO ADICIONAL DEL TICKET
# #
# #

# get equipment
@app.route('/ticket-equipment')
def get_equipment():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_equipment_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Añadir equipment
@app.route('/ticket-equip/', methods=['POST'])
def add_equipent():
	try:
		# _createdBy = _json['createdBy']
		# _customerId = _json['customerId']
		# _agencyId = _json['agencyId']
		# _warehouseId = _json['warehouseId']
		# _subdivision = _json['subdivision']
		# _userTraza = _json['userTraza']
		# _assignedDate = _json['assignedDate']
		# _item_description = _json['item_description']
		# _item_serial = _json['item_serial']
		_json = request.json
		_item = _json['item']
		_quantity = _json['quantity']
		_ticketId = _json['ticketId']
		if request.method == 'POST':
			sql = 'INSERT INTO n_nemesis_n_equipment_model (item, quantity, ticketId) VALUES (%s, %s, %s)'
			data = (_item, _quantity, _ticketId)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Adittional Data added')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Añadir Seriales
@app.route('/ticket-serial/', methods=['POST'])
def add_serial(serial, name):
	try:
		_json = request.json
		_item = _json['item']
		_item_serial = _json['item_serial']
		_createdBy = _json['createdBy']
		_customerId = _json['customerId']
		_agencyId = _json['agencyId']
		if request.method == 'POST':
			sql = ('SELECT item, item_serial FROM n_nemesis_n_equipment_model; UPDATE n_nemesis_n_equipment_model SET serial=%s WHERE name=%s', serial, name)
			data = (_item, _item_serial)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Adittional Data added')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Añadir Tecnico Asignado
@app.route('/ticket-technician/', methods=['POST'])
def add_technician(id_tech):
	try:
		_json = request.json
		_tech = _json['tech_assign']
		_assignedDate = _json['assignedDate']
		if request.method == 'POST':
			sql = ('UPDATE n_nemesis_n_ticket_model SET tech_assign = %s, assignedDate=%s version = 4 WHERE id=%s', _tech, _assignedDate, id_tech)
			# data = (_tech,_assignedDate)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql)
			conn.commit()
			resp = jsonify('Technician Assigned added')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


#
#  Bloque de informacion de tags
#

@app.route('/tag/add', methods=['POST'])
def add_tag():
	try:
		_json = request.json
		_name = _json['name']
		_description = _json['description']
		_type = _json['type']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_warehouseitemtype_model (name, description, type, ids, version) VALUES(%s, %s, %s, %s, %s, %s, %s)'
			data = (_name, _description, _type, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Tag added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/tags')
def tags():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_warehouseitemtype_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/tag/<string:name>')
def tag(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_warehouseitemtype_model WHERE name=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/tag/update', methods=['POST'])
def update_tag():
	try:
		_json = request.json
		_name = _json['name']
		_description = _json['description']
		_type = _json['type']
		_ids = _json['ids']
		_version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_tag_model SET name=%s, description=%s, type=%s, ids=%s, version=%s WHERE id=%s"
			data = (_name, _description, _type, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Tag updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/tag/delete/<string:name>')
def delete_tag(name):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_warehouseitemtype_model WHERE name=%s", (name,))
		conn.commit()
		resp = jsonify('Tag deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


#
#  Bloque de informacion de tickets
#

@app.route('/ticket/add', methods=['POST'])
def add_ticket():
	try:
		_json = request.json
		_createdBy = _json['createdBy']
		_type = _json['type']
		_customerId = _json['customerId']
		_status = _json['status']
		_priority = _json['priority']
		_agencyId = _json['agencyId']
		_description = _json['description']
		_ids = _json['ids']
		_version = _json['version']
		#_code = _json['code']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_ticket_model (createdBy, type, customerId, status, priority, agencyId, description, ids, version) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
			data = (_createdBy, _type, _customerId, _status, _priority, _agencyId, _description, _ids, _version)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/tickets')
def tickets():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_ticket_model, n_nemesis_n_agency_model WHERE n_nemesis_n_ticket_model.agencyId = n_nemesis_n_agency_model.id ORDER BY n_nemesis_n_ticket_model.id DESC')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/ticket/<int:id>')
def ticket(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_ticket_model, n_nemesis_n_agency_model WHERE n_nemesis_n_ticket_model.agencyId = n_nemesis_n_agency_model.id AND n_nemesis_n_ticket_model.id=%s", id)
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# @app.route('/ticket/update', methods=['POST'])
# def update_ticket():
# 	try:
# 		_json = request.json
# 		_createdBy = _json['createdBy']
# 		_type = _json['_type']
# 		_customerId = _json['customerId']
# 		_creationDate = _json['creationDate']
# 		_status = _json['status']
# 		_priority = _json['priority']
# 		_agencyId = _json['agencyId']
# 		_description = _json['description']
# 		_ids = _json['ids']
# 		_version = _json['version']
# 		_code = _json['code']
# 		# validate the received values
# 		if request.method == 'POST':
# 			# save edits
# 			sql = "UPDATE n_nemesis_n_ticket_model SET createdBy=%s, type=%s, customerId=%s, creationDate=%s, status=%s, priority=%s, agencyId=%s, description=%s, ids=%s, version=%s, code=%s WHERE id=%s"
# 			data = (_createdBy, _type, _customerId, _creationDate, _status, _priority, _agencyId, _customerId, _ids, _version, _code)
# 			conn = mysql.connect()
# 			cursor = conn.cursor()
# 			cursor.execute(sql, data)
# 			conn.commit()
# 			resp = jsonify('Ticket updated successfully!')
# 			resp.status_code = 200
# 			return resp
# 		else:
# 			return not_found()
# 	except Exception as e:
# 		print(e)
# 	finally:
# 		cursor.close()
# 		conn.close()

# TICKET UPDATE ONLY NECCESARY FIELDS, 
@app.route('/ticket/update/<int:id>', methods=['POST'])
def update_ticket(id):
	try:
		_json = request.json
		_assignedDate = _json['assignedDate']
		_status = _json['status']
		_description = _json['description']
		_tech_assign = _json['tech_assign']
		_assigned_tags = jsonify['assigned_tags']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_ticket_model SET status=%s, description=%s, tech_assign=%s, assigned_tags=%s, assignedDate=%s, WHERE id=%s"
			data = (_status, _description, _tech_assign, _assigned_tags, _assignedDate, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/ticket/delete/<int:id>')
def delete_ticket(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_ticket_model WHERE id=%s", (id))
		conn.commit()
		resp = jsonify('Ticket deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


#
#  Bloque de informacion de Usuarios
#

@app.route('/user/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


### Busqueda de tecnicos
@app.route('/techn')
def techn():
	try:
		conn = mysql.connect()
		# role = 1
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, username, IsAvailable FROM n_nemesis_users_user_model WHERE RoleT = 1")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT user_id id, user_name name, user_email email, user_password pwd FROM tbl_user")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/user/<int:id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT user_id id, user_name name, user_email email, user_password pwd FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/user/update', methods=['POST'])
def update_user():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/user/delete/<int:id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()
