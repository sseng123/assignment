#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE loan (
            loan_Num VARCHAR(255),
            loan_Type VARCHAR(255),
            loan_Status VARCHAR(255),
            interest_rate VARCHAR(255),
            currency VARCHAR(255),
            orig_principal_amt VARCHAR(255),
            cancelled_amt VARCHAR(255),
            Undisbursed_amt VARCHAR(255),
            disbursed_amt VARCHAR(255),
            IBRD_repaid VARCHAR(255),
            IDA_repaid VARCHAR(255),
            IBRD_due VARCHAR(255),
            IDA_due VARCHAR(255),
            exch_adjust VARCHAR(255),
            borrower_obligatn VARCHAR(255),
            thirpart_sold VARCHAR(255),
            thirpart_repaid VARCHAR(255),
            thirpart_due VARCHAR(255)

        )
        """,
        """ CREATE TABLE country (
                country VARCHAR(255),
                region VARCHAR(255),
                country_code VARCHAR(255),
                guarantor_country_code VARCHAR(255)
                )
        """,
        """
        CREATE TABLE project (
                project_name VARCHAR(255),
                project_id VARCHAR(255),
        )
        """,
        """
        CREATE TABLE dates (
                first_repayment VARCHAR(255),
                last_repayment VARCHAR(255),
                agreemt_date VARCHAR(255),
                board_appr_date VARCHAR(255),
                effective_date VARCHAR(255),
                close_date VARCHAR(255),
                last_disbursement_date VARCHAR(255)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
