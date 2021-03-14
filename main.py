import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
#Begin Import from https://github.com/teamsoo/flask-api-upload-image/blob/master/server.py
from flask import Flask, url_for, send_from_directory, request
import logging, os
# end of upload import
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

"""
SECCION DE AGENCIAS, GET, POST Y UPDATE
"""
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
		cursor.execute('SELECT * FROM n_nemesis_n_agency_model WHERE certification NOT LIKE %%disinstallato%% ORDER BY id DESC')
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

@app.route('/agencyiso/<int:agencyId>')
def agencyIso(agencyId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_agency_model WHERE id =%s', agencyId)
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

@app.route('/agency/update/<int:id>', methods=['POST'])
def update_agency(id):
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_managerId = _json['managerId']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		_certification = _json['certification']
		# _customerId = _json['customerId']
		_moreInfo = _json['moreInfo']
		# _ids = _json['ids']
		# _version = _json['version']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_agency_model SET name=%s, address=%s, managerId=%s, vat=%s, email=%s, phone=%s, certification=%s, moreInfo=%s WHERE id=%s"
			data = (_name, _address, _managerId, _vat, _email, _phone, _certification, _moreInfo, id)
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

#Metodo Ok Final
@app.route('/contact/add', methods=['POST'])
def add_contact():
	try:
		_json = request.json
		_name = _json['name']
		_surname = _json['surname']
		_taxCode = _json['taxCode']
		_address = _json['address']
		_phone = _json['phone']
		_email = _json['email']
		_customerId = _json['customerId']
		_version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = "INSERT INTO n_nemesis_n_contact_model (name, surname, taxCode, address, phone, email, customerId, version) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
			data = (_name, _surname, _taxCode, _address, _phone, _email, _customerId, _version)
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

#Metodo OK Final
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

#Metodo OK Final
@app.route('/contactiso/<int:id>')
def contactIso(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_contact_model WHERE id=%s", id)
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

# Metodo OK Final
@app.route('/contact/update/<int:id>', methods=['POST'])
def update_contact(id):
	try:
		_json = request.json
		_name = _json['name']
		_surname = _json['surname']
		_taxCode = _json['taxCode']
		_address = _json['address']
		_email = _json['email']
		_phone = _json['phone']
		# _user = _json['user']
		# _customerId = _json['customerId']
		# _ids = _json['ids']
		# _version = _json['version']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_contact_model SET name=%s, surname=%s, taxCode=%s, address=%s, email=%s, phone=%s WHERE id=%s"
			data = (_name, _surname, _taxCode, _address, _email, _phone,  id)
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
"""
BLOQUE DE CLIENTES / CUSTOMERS
"""

#Metodo OK final
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

@app.route('/customer/update/<int:id>', methods=['POST'])
def update_customer(id):
	try:
		_json = request.json
		_name = _json['name']
		_address = _json['address']
		_vat = _json['vat']
		_email = _json['email']
		_phone = _json['phone']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_customer_model SET name=%s, address=%s, vat=%s, email=%s, phone=%s WHERE id=%s"
			data = (_name, _address, _vat, _email, _phone, id)
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
# # DONDE INGRESAMOS LOS ITEMS ADICIONALES
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

		# DELETE FROM `nemesis`.`n_nemesis_n_equipment_model` WHERE (`id` = '59');
		# UPDATE `nemesis`.`n_nemesis_n_equipment_model` SET `item` = 'BENQ 22\"' WHERE (`id` = '60');

# Añadir equipment METODO OK FINAL
@app.route('/ticket-equip/', methods=['POST'])
def add_equipent():
	try:
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

# Update Equipment Data
@app.route('/ticket-equip/update/<int:id>', methods=['POST'])
def update_item(id):
	try:
		_json = request.json
		_item = _json['item']
		# _warehouse = _json['warehouseId']
		_ticketId = _json['ticketId']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_equipment_model SET item = %s WHERE (id = %s AND ticketId =%s)"
			data = (_item, id, _ticketId)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Item object updated correctly')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# get Equipment List from Ticket by ticketId METODO OK FINAL
@app.route('/equipmentList/<int:ticketId>')
def equipmentList(ticketId):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_equipment_model WHERE ticketId = %s', ticketId)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


# Añadir Seriales METODO OK FINAL
@app.route('/ticket-serial/<int:id>', methods=['POST'])
def add_serial(id):
	try:
		_json = request.json
		_item_serial = _json['item_serial']
		# _warehouse = _json['warehouseId']
		_ticketId = _json['ticketId']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_equipment_model SET item_serial = %s WHERE (id = %s AND ticketId =%s)"
			data = (_item_serial, id, _ticketId)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Item Serial updated correctly')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Añadir Tecnico Asignado METODO OK FINAL
@app.route('/ticket/technicianassign/<int:id>', methods=['POST'])
def add_technician(id):
	try:
		_json = request.json
		_tech = _json['tech_assign']
		_assignedDate = _json['assignedDate']
		_version = _json['version']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_ticket_model SET tech_assign = %s, assignedDate=%s, version = %s WHERE id=%s"
			data = (_tech,_assignedDate, _version, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
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


# Actualizar Nuevo Técnico METODO OK FINAL
@app.route('/ticket/technicianupdate/<int:id>', methods=['POST'])
def update_technician(id):
	try:
		_json = request.json
		_tech = _json['tech_assign']
		_assignedDate = _json['assignedDate']
		_version = _json['version']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_ticket_model SET tech_assign = %s, assignedDate=%s, version = %s WHERE id=%s"
			data = (_tech,_assignedDate, _version, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
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
		cursor.execute('SELECT name, description, isStack, minimumStack FROM n_nemesis_n_warehouseitemtype_model')
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
# METODO OK FINAL
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
		_code = _json['code']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_ticket_model (createdBy, type, customerId, status, priority, agencyId, description, ids, version, code) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
			data = (_createdBy, _type, _customerId, _status, _priority, _agencyId, _description, _ids, _version, _code)
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

# METODO OK FINAL
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

# METODO OK FINAL
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

#Update version for ticketing METODO OK FINAL
@app.route('/ticketv/<int:id>', methods=['POST'])
def update_ticketversion(id):
	try:
		_json = request.json
		_version = _json['version']
		_status = _json['status']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_ticket_model SET version=%s, status=%s WHERE id=%s"
			data = (_version, _status, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket version updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# REJECT TICKET for ticketing METODO OK FINAL
@app.route('/ticketreject/<int:id>', methods=['POST'])
def update_ticketreject(id):
	try:
		_json = request.json
		_version = _json['version']
		_status = _json['status']
		_tech_assign = _json['tech_assign']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_ticket_model SET version=%s, status=%s, tech_assign=%s WHERE id=%s"
			data = (_version, _status, _tech_assign, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket rejected from technician. Status updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# RESOLVED TICKET for ticketing METODO OK FINAL
@app.route('/ticketresolved/<int:id>', methods=['POST'])
def update_ticketresolved(id):
	try:
		_json = request.json
		_version = _json['version']
		_status = _json['status']
		_assigned_tags = _json['assigned_tags']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_ticket_model SET version=%s, status=%s, assigned_tags=%s, closedDate=CURRENT_TIMESTAMP WHERE id=%s"
			data = (_version, _status, _assigned_tags, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket resolved, good work!. Status updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


# Item from Warehouse stock of product
@app.route('/ticketcountopen')
def ticketcountopen():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT status, COUNT(*) FROM n_nemesis_n_ticket_model AS A where (A.status = 'OPENED') GROUP BY status;")
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Item from Warehouse stock of product
@app.route('/ticketcountworking')
def ticketcountworking():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT status, COUNT(*) FROM n_nemesis_n_ticket_model AS A where (A.status = 'WORKING') GROUP BY status;")
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Item from Warehouse stock of product
@app.route('/clientscount')
def clientscount():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT COUNT(*) FROM n_nemesis_n_customer_model;")
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Item from Warehouse stock of product
@app.route('/ticketwarehouse')
def ticketwarehouse():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_warehouse_model")
		row = cursor.fetchall()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


# GET INFO TO UPDATE TICKET
@app.route('/ticket2up/<int:Id>')
def ticketinfotoup(Id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT type, priority, agencyId, description, code FROM n_nemesis_n_ticket_model WHERE id=%s ', Id)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# TICKET UPDATE ONLY NECCESARY FIELDS, METODO OK FINAL
@app.route('/ticket/update/<int:id>', methods=['POST'])
def update_ticketdata(id):
	try:
		_json = request.json
		_type = _json['type']
		_priority = _json['priority']
		_agencyId = _json['agencyId']
		_description = _json['description']
		_code = _json['code']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = "UPDATE n_nemesis_n_ticket_model SET type=%s, priority=%s, agencyId=%s, description=%s, code=%s WHERE id=%s"
			data = (_type, _priority, _agencyId, _description, _code, id)
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


# Elemento de ticket eliminar
@app.route('/ticket-equip/del/<int:id>', methods=['GET'])
def delete_ItemEquipmentticket(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM n_nemesis_n_equipment_model WHERE id=%s", (id,))
		conn.commit()
		resp = jsonify('Item from Additional equipment deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

#Consulta de Seriales y nombre item
# @app.route('/equipmentSerialCheck/<string:serial>', methods=['POST'])
@app.route('/equipmentSerialCheck/', methods=['GET'])
def serialchecker():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT serial FROM n_nemesis_n_warehouseitem_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Abort Ticket
@app.route('/ticket/abort/<int:id>', methods=['POST'])
def abort_ticket(id):
	try:
		_json = request.json
		_status = _json['status']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_ticket_model SET status=%s WHERE id=%s"
			data = (_status, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Ticket send to Aborted Status successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

##
##
## BLOQUE REFERENTE A WAREHOUSE Y TODAS SUS SOLICITUDES
## Añadir items, actualizar, Nombres de bodegas, categorias, item por tipo
##
##
##

@app.route('/warehouse/additem', methods=['POST'])
def add_warehouseitem():
	try:
		_json = request.json
		_name = _json['name']
		_description = _json['description']
		_serial = _json['serial']
		_supplier= _json['supplier']
		_category = _json['categoryId']
		_status = _json['status']
		_warrantyPeriod = _json['warrantyPeriod']
		# _statusDetails = _json['statusDetails']
		# _technicianNotes = _json['technicianNotes']
		# _isMoving = _json['isMoving']
		_isDeleted = _json['isDeleted']
		_warehouseId = _json['warehouseId']
		_isUsed = _json['isUsed']
		_invoice_purchase = _json['invoice_purchase']
		# _agencyId = _json['agencyId']
		_userId= -_json['userId']
		_changes = _json['changes']
		_type = _json['type']
		_descriptionTrack = _json['descriptionTrack']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_warehouseitem_model (name, description, serial, categoryId, status, warehouseId, used, supplierId, warranty_period, warranty_invoiceId, isDelete) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
			data = (_name, _description, _serial, _category, _status, _warehouseId, _isUsed, _supplier, _warrantyPeriod, _invoice_purchase, _isDeleted)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Item added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Actualizar Nuevo Técnico METODO OK FINAL
@app.route('/warehouseitemup/<int:id>', methods=['POST'])
def update_warehouseitem(id):
	try:
		_json = request.json
		_serial = _json['serial']
		_activation = _json['activation']
		_warehouseId = _json['warehouseId']
		_used = _json['used']
		_location = _json['location']
		_status = _json['status']
		_statusDescription = _json['statusDescription']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_warehouseitem_model SET serial=%s, activation=%s, warehouseId = %s, used=%s, location=%s, status=%s, statusDescription=%s WHERE id=%s"
			data = (_serial, _activation,_warehouseId,_used,_location,_status,_statusDescription, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Item updated Correctly.')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

#ITEM Tracking info Post
@app.route('/warehouse/itemtracking', methods=['POST'])
def add_warehouseitemtracking():
	try:
		_json = request.json
		_serial = _json['serial']
		_userId= -_json['userId']
		_changes = _json['changes']
		_type = _json['type']
		_descriptionTrack = _json['descriptionTrack']
		# validate the received values
		if request.method == 'POST':
			# save edits
			sql = 'INSERT INTO n_nemesis_n_warehousetracking_model (itemId, userId, changes, type, descriptionTrack) VALUES(%s, %s, %s, %s, %s)'
			data = (_serial, _userId, _changes, _type, _descriptionTrack)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('Item track info added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# COMPLETE WAREHOUSE LIST
@app.route('/warehousenames')
def warehousenames():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_warehouse_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Category WAREHOUSE LIST
@app.route('/warehousecategory', methods=['GET','POST'])
def warehousecategory():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		# CODIGO DE VER TODAS LAS CATEGORIAS
		cursor.execute('SELECT * FROM n_nemesis_n_itemscategory_model ORDER BY category_name ASC')
		#
		#
		#CODIGO CORRECTO DONDE CUENTO LAS EXISTENCIAS DE ESE ITEM SEGUN SU CATEGORIA
		# cursor.execute('SELECT category_name, COUNT(*) FROM (n_nemesis_n_warehouseitem_model AS A, n_nemesis_n_itemscategory_model AS B) where (A.categoryId = B.id) GROUP BY category_name;')
		# cursor.execute('INSERT INTO n_nemesis_n_itemscategory_model (category_name) SELECT (%s) WHERE NOT EXISTS(select category_name from n_nemesis_n_itemscategory_model Where category_name = %s) LIMIT 1')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/warehousecategorycount', methods=['GET'])
def warehousecategorycount():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		#CODIGO CORRECTO DONDE CUENTO LAS EXISTENCIAS DE ESE ITEM SEGUN SU CATEGORIA
		cursor.execute('SELECT category_name, COUNT(*) FROM (n_nemesis_n_warehouseitem_model AS A, n_nemesis_n_itemscategory_model AS B) where (A.categoryId = B.id) GROUP BY category_name;')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# ITEM TRACKING
@app.route('/warehouse/tracking', methods=['GET'])
def warehousetrackingget(serial):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * n_nemesis_n_warehousetracking_model WHERE itemId=%s', serial)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


@app.route('/warehouseitemtrack', methods=['POST'])
def warehousetrackingupdate(serial):
	try:
		_json = request.json
		_name = _json['name']
		_description = _json['description']
		_serial = _json['serial']
		_supplier= _json['supplier']
		_category = _json['categoryId']
		_status = _json['status']
		_warrantyPeriod = _json['warrantyPeriod']
		# _statusDetails = _json['statusDetails']
		# _technicianNotes = _json['technicianNotes']
		# _isMoving = _json['isMoving']
		_isDeleted = _json['isDeleted']
		_warehouseId = _json['warehouseId']
		_isUsed = _json['isUsed']
		_invoice_purchase = _json['invoice_purchase']
		# _agencyId = _json['agencyId']
		_userId= -_json['userId']
		_changes = _json['changes']
		_type = _json['type']
		_descriptionTrack = _json['descriptionTrack']
		# validate the received values
		if _name and request.method == 'POST':
			# save edits
			data =('INSERT INTO n_nemesis_n_warehousetracking_model (date, itemId, userId, changes, type, descriptionTrack, rawData, version, userTraza) \
				VALUES(CURRENT_TIMESTAMP, %s, %s, %s, %s, %s,"", 1, 3);')
			data = ()
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


@app.route('/warehousecategory/add', methods=['POST'])
def warehousecategoryadd():
	try:
		_json = request.json
		_category = _json['category_name']
		if request.method == 'POST':
			sql = "INSERT INTO n_nemesis_n_itemscategory_model (category_name) SELECT (%s) WHERE NOT EXISTS(select category_name from n_nemesis_n_itemscategory_model Where category_name = %s) LIMIT 1"
			data = (_category)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('New category added succesfully')
			resp.status_code = 200
			return resp
		else:
			return not_found()
			err_msg = 'Category could not be added.'
			return err_msg
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

#Warehouse category Stock Update
@app.route('/warehousecategory/stockppdate/<int:id>', methods=['POST'])
def warehousecategoryadd(id):
	try:
		_json = request.json
		_minimumStock = _json['minimumStock']
		if request.method == 'POST':
			sql = "UPDATE n_nemesis_n_itemscategory_model (minimumStock) SELECT (%s) WHERE id=%s"
			data = (_minimumStock, id)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('New category added succesfully')
			resp.status_code = 200
			return resp
		else:
			return not_found()
			err_msg = 'Category could not be added.'
			return err_msg
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# ITEM COMPLETE STOCK
@app.route('/warehouseitemspertype')
def witemspertype():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_warehouseitemtype_model, n_nemesis_n_warehouseitem_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# ITEM COMPLETE STOCK
@app.route('/warehouseitems')
def witemsmodel():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_warehouseitem_model')
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Item Individual Info
@app.route('/itemiso/<int:id>')
def witeminfoindividual(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute('SELECT * FROM n_nemesis_n_warehouseitem_model WHERE id=%s',id)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# Item from principal list- get Individual item List
@app.route('/itemlist/<int:id>')
def witeminfo(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		# cursor.execute('SELECT * FROM nemesis.n_nemesis_n_equipment_model,n_nemesis_n_warehouseitemtype_model WHERE item = n_nemesis_n_warehouseitemtype_model.name AND n_nemesis_n_warehouseitemtype_model.id = %s ORDER BY name, item_serial, TicketId DESC',id)
		# 
		# CODIGO FUNCIONAL DE VISUALIZAR TODOS LOS ITEMS DE ESA CATEGORIA
		cursor.execute('SELECT * FROM n_nemesis_n_warehouseitem_model AS A, n_nemesis_n_itemscategory_model AS B where A.categoryId = B.id AND B.id=%s', id)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# ITEM SERIALIZED ITEMS
@app.route('/warehouseserialitems')
def wserialitems():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM n_nemesis_n_warehouseitem_model")
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

# ADD NEW ITEM TO WAREHOUSE 
@app.route('/witem', methods=['POST'])
def add_witem():
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
def delete_witem(name):
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
# Image Upload api code
#

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ALLOWED_EXT ={"jpg","jpeg","png", "pdf"}
# def check_file(file):
# 	return '.' in file and file.rsplit('.',1)[1].lower() in ALLOWED_EXT
def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route('/uploadimage', methods = ['POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.files['image']:
    	app.logger.info(app.config['UPLOAD_FOLDER'])
    	img = request.files['image']
    	img_name = (img.filename)
    	create_new_folder(app.config['UPLOAD_FOLDER'])
    	saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    	app.logger.info("saving {}".format(saved_path))
    	img.save(saved_path)
    	return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
    else:
    	return "Where is the image?"


#
#  Bloque de informacion de Usuarios
#

@app.route('/user/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_email = _json['email']
		_password = _json['password']
		_RoleA = _json['RoleA']
		_RoleE = _json['RoleE']
		_RoleC = _json['RoleC']
		_RoleT = _json['RoleT']
		_version = 1
		# validate the received values
		if _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO n_nemesis_users_user_model (email, password, version, RoleA, RoleE, RoleC, RoleT) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			data = (_email, _hashed_password, _version, _RoleA, _RoleE, _RoleC, _RoleT)
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

##LOGIN
@app.route('/user/mail', methods=['POST'])
def usermail():
	try:
		_json = request.json
		_mail = _json['usermail']
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT a.id, a.email, a.RoleA, a.RoleC, a.RoleE, a.RoleT, b.name, b.surname, b.address, b.phone \
			 FROM n_nemesis_users_user_model a, n_nemesis_n_contact_model b WHERE a.email=%s and a.email = b.email", _mail)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

### Busqueda de tecnicos Metodo OK FINAL
@app.route('/techn')
def techn():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, username, IsAvailable FROM n_nemesis_users_user_model WHERE RoleT = 1 AND IsAvailable = 1")
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
			data = (_name, _email, _hashed_password, _id)
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
