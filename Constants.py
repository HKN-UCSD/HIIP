COLUMNS = ['First Name', 'Last Name', 'Class Standing', 'Cum GPA', 'Major Code', 'Dept', 'Email']
DEPTS = ['CSE', 'ECE', 'MATH', 'BENG']
CLASS_STANDINGS = ['SO', 'JR', 'SR']
DEPTS_MAJORS = dict()  # bit of a faux-pas...
DEPTS_MAJORS['CSE'] = ['CS25', 'CS26', 'CS27', 'CS28']
DEPTS_MAJORS['ECE'] = ['EC26', 'EC27', 'EC28']
DEPTS_MAJORS['MATH'] = ['MA30']
DEPTS_MAJORS['BENG'] = ['BE25', 'BE26', 'BE27', 'BE28']
CLASS_QUANTILE = {'SO': 0.8, 'JR': 0.75, 'SR': 0.667}