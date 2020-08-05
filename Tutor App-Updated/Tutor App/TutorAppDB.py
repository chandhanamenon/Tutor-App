import mysql.connector

"""
This class handles all the database transactions for the application
"""

class TutorAppDB():

    def __init__(self):

        # Connect to the database
        self.connection = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="",
          database="tutor_db",
          port=3308
        )

        # Get a cusror to execute the queries
        self.cursor = self.connection.cursor()

    # Method to close the connection and cursor
    def close_connection(self):
        self.cursor.close()
        self.connection.close()


    # Method to select a student based on an id
    def get_student_for_ids(self, student_id):

        query = "SELECT student_name, mobile, parent_name, date_joined FROM student_master WHERE student_id=%s"
        values = (student_id,)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)

    # Method to add a new student, date_joined format should be 'YYYY-MM-DD'
    def save_student(self, student_name, mobile, parent_name, date_joined):

         query = "INSERT INTO student_master (student_name, mobile, parent_name, date_joined,status) VALUES (%s, %s, %s, %s, %s)"
         values = (student_name,mobile,parent_name,date_joined,"ACTIVE")
        
         self.cursor.execute(query,values)

         self.connection.commit()

         self.close_connection()

    # Method to add a new student, date_joined format should be 'YYYY-MM-DD'
    def save_attendance(self, date, student_id, batch_id, comment):

         query = "INSERT INTO attendance(date, student_id, is_absent, batch_id, comment) VALUES (%s, %s, %s, %s, %s)"
         values = (date, student_id, "True", batch_id, comment)
        
         self.cursor.execute(query,values)

         self.connection.commit()

         self.close_connection()
        

    # Method to deactivate a student
    def deactivate_student(self, student_id):

        query = "UPDATE student_master SET status=%s WHERE student_id=%s"
        values = ("INACTIVE",student_id)
        
        self.cursor.execute(query,values)

        self.connection.commit()

        self.close_connection()
    

    # Method to get all the students for a batch
    def get_all_students_for_batch(self, batch_id):

        query = "SELECT a.student_id, b.student_name, b.mobile, b.date_joined FROM student_batch a, student_master b WHERE a.batch_id=%s AND a.student_id=b.student_id AND b.status=%s"

        values = (batch_id,'ACTIVE')
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)

        # Method to get all the students for a batch for the attendance
    def get_all_students_for_batch_attendance(self):

        query = "SELECT  c.batch_name, b.student_name, b.student_id FROM student_batch a, student_master b, batch_master c WHERE a.student_id=b.student_id AND a.batch_id=c.batch_id AND b.status=%s"

        values = ("ACTIVE",)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)

        # Method to get all the fee details
    def get_fee_det(self):
        
        query = "SELECT a.student_id, a.student_name, b.batch_name, b.fee, a.student_id from student_master a,batch_master b,student_batch c WHERE c.batch_id=b.batch_id AND c.student_id=a.student_id AND b.status=%s"

        values = ("ACTIVE",)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)
    
        #to print the pay now page for the recipt    
    def get_fee_det_pay(self,student_id):
        
        query = "SELECT  a.student_name, b.batch_name, b.fee, b.batch_id,a.student_id from student_master a,batch_master b,student_batch c WHERE c.batch_id=b.batch_id AND c.student_id=a.student_id AND a.student_id=%s AND a.status=%s"

        values = (student_id,"ACTIVE",)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)


    # Method to update a student record
    def update_student(self, student_name, mobile, parent_name, date_joined, student_id):

        query = "UPDATE student_master SET student_name=%s, mobile=%s, parent_name=%s, date_joined=%s WHERE student_id=%s"
        values = (student_name,mobile,parent_name,date_joined,student_id)
        
        self.cursor.execute(query,values)

        self.connection.commit()

        self.close_connection()

    # Method to get list of all batches

    # Method to insert a new batch
    def save_batch(self,batch_name,description,fee):

        try:
            query = "INSERT INTO batch_master(batch_name, description, status, fee) VALUES (%s,%s,%s,%s)"
            values = (batch_name,description,"ACTIVE", fee)
        
            self.cursor.execute(query,values)

            self.connection.commit()            
            
        except Exception as ex:
            print(ex)
        finally:
            self.close_connection()

        #to save the fee paid by the student after clicking pay now
    def save_receipt(self,paid_on_date,fees_amount,student_id,batch_id):

        try:
            query = "INSERT INTO receipt(paid_on_date,fees_amount,student_id,batch_id,remarks) VALUES (%s,%s,%s,%s,%s)"
            values = (paid_on_date,fees_amount,student_id,batch_id,"Paid")
        
            self.cursor.execute(query,values)

            self.connection.commit()            
            
        except Exception as ex:
            print(ex)
        finally:
            self.close_connection()       
            

    # Method to save a batch in the database
    def update_batch(self,batch_name,description,batch_id,fee):
        query = "UPDATE batch_master SET batch_name=%s, description=%s, fee=%s WHERE batch_id=%s"
        values = (batch_name,description,fee,batch_id)
        
        self.cursor.execute(query,values)

        self.connection.commit()


        self.close_connection()
        

    # Method to deactivate a batch
    def deactvate_batch(self,batch_id):
        query = "UPDATE batch_master SET status=%s WHERE batch_id=%s"
        values = ("INACTIVE",batch_id)
        
        self.cursor.execute(query,values)
        self.connection.commit()
        self.close_connection()
        

    # Method to retrieve the details of a batch
    def get_batch(self,batch_id):
        query = "SELECT batch_name, description, fee FROM batch_master WHERE batch_id=%s"
        values = (batch_id,)
        
        self.cursor.execute(query,values)
        result = self.cursor.fetchall()
        
        self.close_connection()
        
        return(result)
    
    #Method to get information for the attendance table
    def get_attendnace(self,student_id):
        query = "SELECT student_id, batch_id FROM student_batch WHERE student_id=%s"
        values = (student_id,)
        
        self.cursor.execute(query,values)
        result = self.cursor.fetchall()
        
        self.close_connection()
        
        return(result)

    # Method to get all the active batches from the database
    def get_active_batches(self):
        query = "SELECT batch_name, description, batch_id FROM batch_master WHERE status=%s"
        values = ("ACTIVE",)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)

    # Method to get all the active batches from the database
    def get_active_student(self):
        query = "SELECT student_name, mobile, parent_name, date_joined, student_id FROM student_master WHERE status=%s"
        values = ("ACTIVE",)
        
        self.cursor.execute(query,values)

        result = self.cursor.fetchall()

        self.close_connection()

        return(result)

    
    

# Test the class - Do not run this code if imported by other file
if __name__ == "__main__":
    db = TutorAppDB()
    student_data = db.get_student_for_ids(1)
    for student in student_data:
        print(student)
        
