from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from application.models import PersonalInfo, MobileNumberInfo, SkillsInfo, CompanyInfo,TelephoneNumberInfo,CutOffPeriodInfo, AttendanceInfo, EmployeePayroll, EmployeeSalary, EmployeeLeaves, EmployeeItenerary, EmployeeIteneraryDetails,Concerns
import os
from decimal import Decimal

def file_validator(value):

    file_size = value.size
    valid_file_extension = ['.xlsx','.xls']

    file_extension = os.path.splitext(value.name)[1]

    print("File Name: ", value.name)
    print("File Extension: ", file_extension)

    file_size_kb = file_size * 0.001
    file_size_mb = file_size_kb * 0.0001

    print("File Size: ", file_size, " Bytes")
    print("File Size: ", file_size_kb, " KB")
    print("File Size: ", file_size_mb, " MB")

    if not file_extension in valid_file_extension:
        print("Invalid file! Valid files only: ('.xlsx', '.xls')")
        raise ValidationError("Invalid file! Valid files only: ('.xlsx', '.xls')")

    else:
        if file_size_mb > 5: # 5MB
            print("File too large! The maximum file size can be upload is 5 MB")
            raise ValidationError("The maximum file size can be upload is 5 MB")
        else:
            print('FILE is VALID')
            return value


class UserAccountCredentialsForm(UserCreationForm):
    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserAccountCredentialsForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Username',
        }

        self.fields['email'].widget.attrs = {
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'required',
        }

        self.fields['password1'].widget.attrs = {
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Password',
        }

        self.fields['password2'].widget.attrs = {
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Retype password',
        }

class PersonalForm(forms.ModelForm):

    dob = forms.DateField(
        widget=forms.DateInput(
            format='%m/%d/%Y',
            attrs={
                'id': 'dob',
                'type': 'text',
                'class': 'form-control pull-right',
            }
        ),
        input_formats=('%m/%d/%Y', )
    )

    date_started = forms.DateField(
        widget=forms.DateInput(
            format='%m/%d/%Y',
            attrs={
                'id': 'date_started',
                'type': 'text',
                'class': 'form-control pull-right',
            }
        ),
        input_formats=('%m/%d/%Y', )
    )

    class Meta():
        model = PersonalInfo
        exclude = ("fk_user", "key_id", "date_added")

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)

        self.fields['suffix'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Suffix if any',
        }
        self.fields['first_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'First name',
        }
        self.fields['middle_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Middle Name',
        }
        self.fields['last_name'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Last name',
        }
        self.fields['age'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Age',
        }
        # self.fields['gender'].widget.attrs = {
        #     'class': 'form-control select2',
        #     'style': 'width: 100%;',
        # }

        self.fields['gender'].widget.attrs = {
            'type': 'text',
            'class': 'form-control', 
        }
        self.fields['address'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Address',
        }

        self.fields['education'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Education',
        }

        self.fields['experience'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Experience',
        }

        self.fields['notes'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Notes',
        }

        self.fields['emer_cont_pers'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Emergency Contact Person',
        }

        self.fields['emer_cont_pers_cont_no'].widget.attrs = {
            'type': 'number',
            'class': 'form-control',
            'placeholder': 'Emergency Contact Person Number',
        }

class MobileNumberForm(forms.ModelForm):
    class Meta():
        model = MobileNumberInfo
        exclude = ("fk_mobile_user",)

    def __init__(self, *args, **kwargs):
        super(MobileNumberForm, self).__init__(*args, **kwargs)

        self.fields['mobile_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Mobile Number',
            'required': 'required',
        }

class SkillsForm(forms.ModelForm):

    SKILL_LIST = (
        ('Abstract Factory', 'Abstract Factory'),
        ('Accounting System', 'Accounting System'),
        ('Accuracy and Precision', 'Accuracy and Precision'),
        ('Acquisition management', 'Acquisition management'),
        ('ActiveRecord', 'ActiveRecord'),
        ('Acunetix', 'Acunetix'),
        ('Acute Coronary Syndrome', 'Acute Coronary Syndrome'),
        ('Acute Pain Management', 'Acute Pain Management'),
        ('ADamSoft', 'ADamSoft'),
        ('ADIC', 'ADIC'),
        ('Administration and Configuration', 'Administration and Configuration'),
        ('Adobe Fireworks', 'Adobe Fireworks'),
        ('Adobe FrameMaker', 'Adobe FrameMaker'),
        ('Adobe FreeHand', 'Adobe FreeHand'),
        ('Adolescent Health', 'Adolescent Health'),
        ('Advanced Features of Carbonado', 'Advanced Features of Carbonado'),
        ('Aggressive Marketing', 'Aggressive Marketing'),
        ('Agile', 'Agile'),
        ('AgileJ StructureViews', 'AgileJ StructureViews'),
        ('Agm', 'Agm'),
        ('AhnLab Site Guard', 'AhnLab Site Guard'),
        ('AIML', 'AIML'),
        ('AlaSQL', 'AlaSQL'),
        ('Aleph', 'Aleph'),
        ('All-Source Analysis', 'All-Source Analysis'),
        ('Alternative Dispute Resolution', 'Alternative Dispute Resolution'),
        ('ALV Reporting', 'ALV Reporting'),
        ('Amanda', 'Amanda'),
        ('Amateur Photography', 'Amateur Photography'),
        ('Amazon SQS', 'Amazon SQS'),
        ('AMD Am29000', 'AMD Am29000'),
        ('Amira', 'Amira'),
        ('AMPL', 'AMPL'),
        ('AMQP', 'AMQP'),
        ('Anaerobic Microbiology', 'Anaerobic Microbiology'),
        ('Analog Multimeter', 'Analog Multimeter'),
        ('Analyse-it', 'Analyse-it'),
        ('Animal and Stem Cells', 'Animal and Stem Cells'),
        ('Annuity', 'Annuity'),
        ('AnyDoc Software', 'AnyDoc Software'),
        ('Apache Mina SSHD', 'Apache Mina SSHD'),
        ('API Testing', 'API Testing'),
        ('Apollo', 'Apollo'),
        ('Apple Graphics Library ', 'Apple Graphics Library '),
        ('Apple Motion', 'Apple Motion'),
        ('Applied to Discrete Models', 'Applied to Discrete Models'),
        ('Aquatic Therapy', 'Aquatic Therapy'),
        ('Arabic', 'Arabic'),
        ('Arbortext Command', 'Arbortext Command'),
        ('Ardor3D', 'Ardor3D'),
        ('Arduino Diecimila', 'Arduino Diecimila'),
        ('ArgoUML', 'ArgoUML'),
        ('Arranging Angel Funding', 'Arranging Angel Funding'),
        ('Arts Integration', 'Arts Integration'),
        ('ASC-THCLSO11', 'ASC-THCLSO11'),
        ('Asian Cuisine', 'Asian Cuisine'),
        ('ASP.NET', 'ASP.NET'),
        ('ASRemi', 'ASRemi'),
        ('Asset Write Downs', 'Asset Write Downs'),
        ('Astah', 'Astah'),
        ('Athletic Footwear', 'Athletic Footwear'),
        ('ATL', 'ATL'),
        ('Autodesk Inventor', 'Autodesk Inventor'),
        ('Automated Testing', 'Automated Testing'),
        ('Automotive Industry Knowledge', 'Automotive Industry Knowledge'),
        ('Availability Management', 'Availability Management'),
        ('Awk Programming Language', 'Awk Programming Language'),
        ('B.Tech', 'B.Tech'),
        ('BABOK', 'BABOK'),
        ('Bachman', 'Bachman'),
        ('Back Bay', 'Back Bay'),
        ('BackBox', 'BackBox'),
        ('Backjumping', 'Backjumping'),
        ('Bacterio', 'Bacterio'),
        ('Badboy', 'Badboy'),
        ('Balochi', 'Balochi'),
        ('Bancware', 'Bancware'),
        ('Behavior Management', 'Behavior Management'),
        ('Belief Propagation', 'Belief Propagation'),
        ('Bell Desk', 'Bell Desk'),
        ('Bi-Directional RNN', 'Bi-Directional RNN'),
        ('Biochip', 'Biochip'),
        ('Bitvise SSH Server', 'Bitvise SSH Server'),
        ('BizTalk', 'BizTalk'),
        ('Black-Box Testing', 'Black-Box Testing'),
        ('BOOPSI', 'BOOPSI'),
        ('Bottle', 'Bottle'),
        ('British Standards', 'British Standards'),
        ('Bulk Endocytosis', 'Bulk Endocytosis'),
        ('Burp Suite', 'Burp Suite'),
        ('Business Consultant', 'Business Consultant'),
        ('Business Studies', 'Business Studies'),
        ('Butchery', 'Butchery'),
        ('C Programming Language', 'C Programming Language'),
        ('C Suite', 'C Suite'),
        ('C#', 'C#'),
        ('Cakewalk', 'Cakewalk'),
        ('Call Logging', 'Call Logging'),
        ('Capacity Management', 'Capacity Management'),
        ('Capacity Management Strategies', 'Capacity Management Strategies'),
        ('Carbon Credits', 'Carbon Credits'),
        ('Cartels', 'Cartels'),
        ('Cash Advance', 'Cash Advance'),
        ('Cash Management', 'Cash Management'),
        ('Catalog Merchandising', 'Catalog Merchandising'),
        ('CBP-IEEE', 'CBP-IEEE'),
        ('CCA - PegaSystems', 'CCA - PegaSystems'),
        ('CDCP', 'CDCP'),
        ('Ceramic Analysis', 'Ceramic Analysis'),
        ('Change Management', 'Change Management'),
        ('Chipscope Pro', 'Chipscope Pro'),
        ('Chlorin', 'Chlorin'),
        ('Chronic Rhinitis', 'Chronic Rhinitis'),
        ('Circumscription Logic', 'Circumscription Logic'),
        ('CisionPoint', 'CisionPoint'),
        ('Clade', 'Clade'),
        ('ClickDummy', 'ClickDummy'),
        ('Client Education', 'Client Education'),
        ('Client Focus', 'Client Focus'),
        ('Client Relations', 'Client Relations'),
        ('CLM', 'CLM'),
        ('Cloud', 'Cloud'),
        ('CLR Profiler', 'CLR Profiler'),
        ('Cobal', 'Cobal'),
        ('Code Coverage Tools', 'Code Coverage Tools'),
        ('Codeship', 'Codeship'),
        ('Cold Calls', 'Cold Calls'),
        ('Collection', 'Collection'),
        ('Compatibility Testing', 'Compatibility Testing'),
        ('Compiler Development', 'Compiler Development'),
        ('Compiling', 'Compiling'),
        ('Concert Photography', 'Concert Photography'),
        ('Connector', 'Connector'),
        ('Consensus decision-making', 'Consensus decision-making'),
        ('Contextual Design', 'Contextual Design'),
        ('Convolutional Neural Network', 'Convolutional Neural Network'),
        ('CopSSH', 'CopSSH'),
        ('Core Graphics', 'Core Graphics'),
        ('CRB', 'CRB'),
        ('Create Test Strategy', 'Create Test Strategy'),
        ('Critical Care Medicine', 'Critical Care Medicine'),
        ('CRM Sales', 'CRM Sales'),
        ('Crop Protection', 'Crop Protection'),
        ('C-TPAT', 'C-TPAT'),
        ('Cupping', 'Cupping'),
        ('Custom Synthesis', 'Custom Synthesis'),
        ('CWP-ED', 'CWP-ED'),
        ('CY8C5xxxx', 'CY8C5xxxx'),
        ('Cython', 'Cython'),
        ('D900', 'D900'),
        ('DaDaBik', 'DaDaBik'),
        ('Data Design System', 'Data Design System'),
        ('Data Dictionary', 'Data Dictionary'),
        ('Data Management', 'Data Management'),
        ('Data Systems', 'Data Systems'),
        ('Database Capacity Management', 'Database Capacity Management'),
        ('Database Creation', 'Database Creation'),
        ('Database Monitoring & Performance Tuning',
         'Database Monitoring & Performance Tuning'),
        ('DataONE', 'DataONE'),
        ('Dbx Debugger', 'Dbx Debugger'),
        ('DDoS Mitigation', 'DDoS Mitigation'),
        ('Dealer Operations', 'Dealer Operations'),
        ('Debugging', 'Debugging'),
        ('Defaunation', 'Defaunation'),
        ('Defining the Specification', 'Defining the Specification'),
        ('Dental Anesthesia', 'Dental Anesthesia'),
        ('Department Budgeting', 'Department Budgeting'),
        ('Deployment Management', 'Deployment Management'),
        ('Design and Planning', 'Design and Planning'),
        ('Desktop Application Development', 'Desktop Application Development'),
        ('Development of Triggers', 'Development of Triggers'),
        ('Dielectric Heating', 'Dielectric Heating'),
        ('Digital Imaging', 'Digital Imaging'),
        ('DirSync Pro', 'DirSync Pro'),
        ('Disaster Mitigation', 'Disaster Mitigation'),
        ('Discourse Analysis', 'Discourse Analysis'),
        ('Discrete Phase-Type Distribution', 'Discrete Phase-Type Distribution'),
        ('Diversity Recruitment', 'Diversity Recruitment'),
        ('Dividend Yield', 'Dividend Yield'),
        ('Do', 'Do'),
        ('Dropmysite', 'Dropmysite'),
        ('DSDM', 'DSDM'),
        ('Dynamics NAV Server', 'Dynamics NAV Server'),
        ('Eager Learning', 'Eager Learning'),
        ('Easy CD Creator', 'Easy CD Creator'),
        ('Eclipse TPTP', 'Eclipse TPTP'),
        ('Eco-efficiency', 'Eco-efficiency'),
        ('Eco-Investing', 'Eco-Investing'),
        ('EDA', 'EDA'),
        ('EDRP', 'EDRP'),
        ('EDWinXP', 'EDWinXP'),
        ('Ejector Refrigeration Systems', 'Ejector Refrigeration Systems'),
        ('ElephantDrive', 'ElephantDrive'),
        ('Embedded Systems', 'Embedded Systems'),
        ('Encore', 'Encore'),
        ('Encryption Software', 'Encryption Software'),
        ('EnergyMech', 'EnergyMech'),
        ('Engagement Marketing', 'Engagement Marketing'),
        ('Enteral Feeding', 'Enteral Feeding'),
        ('Enterprise Application Development',
         'Enterprise Application Development'),
        ('Entrepreneurial Finance', 'Entrepreneurial Finance'),
        ('Environmental Data Analysis', 'Environmental Data Analysis'),
        ('Environmental Geology', 'Environmental Geology'),
        ('EOS', 'EOS'),
        ('EPMA', 'EPMA'),
        ('EPMLive', 'EPMLive'),
        ('EQATEC Profiler', 'EQATEC Profiler'),
        ('ERP Selection', 'ERP Selection'),
        ('Escalations', 'Escalations'),
        ('ESpeak', 'ESpeak'),
        ('Eukaryotic Initiation Factor', 'Eukaryotic Initiation Factor'),
        ('European Politics', 'European Politics'),
        ('Evolutionary Art', 'Evolutionary Art'),
        ('Facility management', 'Facility management'),
        ('FactSet', 'FactSet'),
        ('Family Medicine', 'Family Medicine'),
        ('Fantom', 'Fantom'),
        ('FAQ', 'FAQ'),
        ('FDMA', 'FDMA'),
        ('FedEx', 'FedEx'),
        ('Feeder Protection', 'Feeder Protection'),
        ('FEMA Matters', 'FEMA Matters'),
        ('File Commander', 'File Commander'),
        ('Files-11', 'Files-11'),
        ('Financial Freedom', 'Financial Freedom'),
        ('Financial Sector', 'Financial Sector'),
        ('Finite-Difference Time-Domain Method',
         'Finite-Difference Time-Domain Method'),
        ('Fire Pumps', 'Fire Pumps'),
        ('Firmware', 'Firmware'),
        ('Fluke', 'Fluke'),
        ('FMOD', 'FMOD'),
        ('FOH', 'FOH'),
        ('Folkewall', 'Folkewall'),
        ('Follow-on Offerings', 'Follow-on Offerings'),
        ('Forensic Anthropology', 'Forensic Anthropology'),
        ('fortrabbit', 'fortrabbit'),
        ('Front End Programming/Scripting', 'Front End Programming/Scripting'),
        ('FSG', 'FSG'),
        ('FTA', 'FTA'),
        ('Functional Viewpoint', 'Functional Viewpoint'),
        ('Fund Flow Statement', 'Fund Flow Statement'),
        ('Futures', 'Futures'),
        ('G8D', 'G8D'),
        ('Galaxkey', 'Galaxkey'),
        ('Gallery Administration', 'Gallery Administration'),
        ('Game Artificial Intelligence', 'Game Artificial Intelligence'),
        ('Game Development', 'Game Development'),
        ('Games, Entertainment', 'Games, Entertainment'),
        ('GD Graphics Library', 'GD Graphics Library'),
        ('Gene Silencing', 'Gene Silencing'),
        ('General Accounts', 'General Accounts'),
        ('Generating Primary Keys', 'Generating Primary Keys'),
        ('Generating Revenue', 'Generating Revenue'),
        ('Generative Topographic Map', 'Generative Topographic Map'),
        ('Genomic Counseling', 'Genomic Counseling'),
        ('Genomic Imprinting', 'Genomic Imprinting'),
        ('GLIMMERHMM', 'GLIMMERHMM'),
        ('Global', 'Global'),
        ('Global Label Management', 'Global Label Management'),
        ('Global Strategy', 'Global Strategy'),
        ('GlowCode', 'GlowCode'),
        ('GNU M4', 'GNU M4'),
        ('GNU Toolchain', 'GNU Toolchain'),
        ('Go', 'Go'),
        ('Google BigQuery', 'Google BigQuery'),
        ('Government Relations', 'Government Relations'),
        ('Gradle', 'Gradle'),
        ('Grant management', 'Grant management'),
        ('Granular Configuration Automation', 'Granular Configuration Automation'),
        ('Group Policy', 'Group Policy'),
        ('gulp.js', 'gulp.js'),
        ('Gypsum', 'Gypsum'),
        ('Hadoop', 'Hadoop'),
        ('Hair Stylist', 'Hair Stylist'),
        ('Ham Passwords', 'Ham Passwords'),
        ('Hammond Organ', 'Hammond Organ'),
        ('HAP', 'HAP'),
        ('Hardware Sizing', 'Hardware Sizing'),
        ('Hbase', 'Hbase'),
        ('HCFA', 'HCFA'),
        ('HCNP-CC', 'HCNP-CC'),
        ('Health Club', 'Health Club'),
        ('Healthcare Consulting', 'Healthcare Consulting'),
        ('Healthcare Transaction base', 'Healthcare Transaction base'),
        ('HEC-2', 'HEC-2'),
        ('Here', 'Here'),
        ('Hilbert System', 'Hilbert System'),
        ('Home Warranty', 'Home Warranty'),
        ('Homebuilding', 'Homebuilding'),
        ('HORNETDRIVE', 'HORNETDRIVE'),
        ('Hospital Pharmacy', 'Hospital Pharmacy'),
        ('Hospitals, Clinics', 'Hospitals, Clinics'),
        ('HP StorageWorks', 'HP StorageWorks'),
        ('HR Coordination', 'HR Coordination'),
        ('HR Software', 'HR Software'),
        ('Huffyuv', 'Huffyuv'),
        ('IMAGE cDNA Clones', 'IMAGE cDNA Clones'),
        ('Immigration', 'Immigration'),
        ('IMS DB', 'IMS DB'),
        ('Infographics', 'Infographics'),
        ('Informatica PowerCenter', 'Informatica PowerCenter'),
        ('Injectable', 'Injectable'),
        ('Ink Cartridges', 'Ink Cartridges'),
        ('Insurance Advisory', 'Insurance Advisory'),
        ('Insurance Bank', 'Insurance Bank'),
        ('Integrated Design', 'Integrated Design'),
        ('Interactomics', 'Interactomics'),
        ('International Real Estate', 'International Real Estate'),
        ('International Regulations', 'International Regulations'),
        ('Inverse Dynamics', 'Inverse Dynamics'),
        ('IoT Operating System', 'IoT Operating System'),
        ('IPSec', 'IPSec'),
        ('ISO Procedures', 'ISO Procedures'),
        ('ISO/TS 16949', 'ISO/TS 16949'),
        ('Iterative Viterbi Decoding', 'Iterative Viterbi Decoding'),
        ('IwGame Engine', 'IwGame Engine'),
        ('Job Coaching', 'Job Coaching'),
        ('Juvederm', 'Juvederm'),
        ('JZBot', 'JZBot'),
        ('Keen Planner', 'Keen Planner'),
        ('Kimball Methodology', 'Kimball Methodology'),
        ('Kreata Global', 'Kreata Global'),
        ('KYC', 'KYC'),
        ('Labour Laws', 'Labour Laws'),
        ('Lamebook', 'Lamebook'),
        ('LANDesk management', 'LANDesk management'),
        ('Language Services', 'Language Services'),
        ('Laser beam', 'Laser beam'),
        ('Lattice C', 'Lattice C'),
        ('Layouting', 'Layouting'),
        ('LEED', 'LEED'),
        ('Legal Process', 'Legal Process'),
        ('Libpolo', 'Libpolo'),
        ('Licensed Master Electrician', 'Licensed Master Electrician'),
        ('Life/work Balance', 'Life/work Balance'),
        ('LifeSize Video Conferencing', 'LifeSize Video Conferencing'),
        ('Lightwave', 'Lightwave'),
        ('Link Contract', 'Link Contract'),
        ('Linode', 'Linode'),
        ('Linux Userland File System', 'Linux Userland File System'),
        ('LINX (IPC)', 'LINX (IPC)'),
        ('Liquid Handling Robot', 'Liquid Handling Robot'),
        ('LiquidPlanner', 'LiquidPlanner'),
        ('LIS', 'LIS'),
        ('LisaProject', 'LisaProject'),
        ('Literary Theory', 'Literary Theory'),
        ('Live Event Producer', 'Live Event Producer'),
        ('Livestock Husbandary', 'Livestock Husbandary'),
        ('Load Runner 7.x', 'Load Runner 7.x'),
        ('Long Hair', 'Long Hair'),
        ('LPR', 'LPR'),
        ('LSF', 'LSF'),
        ('LTE Physical Layer', 'LTE Physical Layer'),
        ('Lymphoid Organs', 'Lymphoid Organs'),
        ('Machine Learning', 'Machine Learning'),
        ('Macintosh Networking', 'Macintosh Networking'),
        ('MacProject', 'MacProject'),
        ('Madaline', 'Madaline'),
        ('Magento Architecture', 'Magento Architecture'),
        ('Magics', 'Magics'),
        ('Mailers', 'Mailers'),
        ('Major Gift Solicitations', 'Major Gift Solicitations'),
        ('Making Deposits', 'Making Deposits'),
        ('Mallet Software Project', 'Mallet Software Project'),
        ('Management of Suppliers', 'Management of Suppliers'),
        ('Managing Database Instances', 'Managing Database Instances'),
        ('Manpower Utilization', 'Manpower Utilization'),
        ('Mantis', 'Mantis'),
        ('MASE-NSSysSup07', 'MASE-NSSysSup07'),
        ('Master Scheduling', 'Master Scheduling'),
        ('MBE', 'MBE'),
        ('McCLIM', 'McCLIM'),
        ('MCITP(GP 10.0)', 'MCITP(GP 10.0)'),
        ('Medical Compliance', 'Medical Compliance'),
        ('Medical Practice', 'Medical Practice'),
        ('Medication Administration', 'Medication Administration'),
        ('Mentoring New Hires', 'Mentoring New Hires'),
        ('Meta Databases', 'Meta Databases'),
        ('Microeconomics', 'Microeconomics'),
        ('Microsoft Exchange', 'Microsoft Exchange'),
        ('Microsoft Intermediate', 'Microsoft Intermediate'),
        ('Microsoft PIX', 'Microsoft PIX'),
        ('Microsoft Software Updater', 'Microsoft Software Updater'),
        ('Microsoft Windows administration', 'Microsoft Windows administration'),
        ('Microsoft Yammer', 'Microsoft Yammer'),
        ('MiniGLX', 'MiniGLX'),
        ('MMDF', 'MMDF'),
        ('MOAB', 'MOAB'),
        ('Mobile Application', 'Mobile Application'),
        ('mod jk', 'mod jk'),
        ('ModelRight', 'ModelRight'),
        ('Modems', 'Modems'),
        ('Modernization', 'Modernization'),
        ('Molecular Biology', 'Molecular Biology'),
        ('Molecular Genetics', 'Molecular Genetics'),
        ('monkeyrunner', 'monkeyrunner'),
        ('MONOCLdb', 'MONOCLdb'),
        ('MoU', 'MoU'),
        ('Moulds', 'Moulds'),
        ('MPC-MLQ', 'MPC-MLQ'),
        ('MS Cluster', 'MS Cluster'),
        ('MS SQL Server', 'MS SQL Server'),
        ('MSP Advanced Practitioner', 'MSP Advanced Practitioner'),
        ('Multi-country', 'Multi-country'),
        ('Multimedia Bandwidth', 'Multimedia Bandwidth'),
        ('Multiservice Media Gateway', 'Multiservice Media Gateway'),
        ('Music Criticism', 'Music Criticism'),
        ('Music Journalism', 'Music Journalism'),
        ('MySAP CRM', 'MySAP CRM'),
        ('NAMD', 'NAMD'),
        ('Namespace Nodes', 'Namespace Nodes'),
        ('Nautilus', 'Nautilus'),
        ('NCBI Epigenomics', 'NCBI Epigenomics'),
        ('Nearshore', 'Nearshore'),
        ('Netsniff-ng', 'Netsniff-ng'),
        ('Network enhancements', 'Network enhancements'),
        ('NeXpose', 'NeXpose'),
        ('Nielsen Nitro', 'Nielsen Nitro'),
        ('NIH Shift', 'NIH Shift'),
        ('Node.js Stream', 'Node.js Stream'),
        ('Nokia IPSO', 'Nokia IPSO'),
        ('Non-infringement', 'Non-infringement'),
        ('Novell Netmail', 'Novell Netmail'),
        ('Nuitka', 'Nuitka'),
        ('Numerical Simulation', 'Numerical Simulation'),
        ('Obfuscation', 'Obfuscation'),
        ('Objective C', 'Objective C'),
        ('OBPM', 'OBPM'),
        ('ODE', 'ODE'),
        ('Olympic Lifting', 'Olympic Lifting'),
        ('Oncology', 'Oncology'),
        ('Opening Hotels', 'Opening Hotels'),
        ('OpenOffice', 'OpenOffice'),
        ('OpenSMTPD', 'OpenSMTPD'),
        ('Operational Execution', 'Operational Execution'),
        ('Ophthalmics', 'Ophthalmics'),
        ('Oracle Data Mining', 'Oracle Data Mining'),
        ('Organization Performance Management',
         'Organization Performance Management'),
        ('Pacemaker', 'Pacemaker'),
        ('Package Inserts', 'Package Inserts'),
        ('PADS', 'PADS'),
        ('Panchakarma', 'Panchakarma'),
        ('Paper Converting', 'Paper Converting'),
        ('Parent-Teacher Communication', 'Parent-Teacher Communication'),
        ('PASMA', 'PASMA'),
        ('Passive House', 'Passive House'),
        ('Password management', 'Password management'),
        ('Password Protection', 'Password Protection'),
        ('Payroll Taxes', 'Payroll Taxes'),
        ('PEGylation', 'PEGylation'),
        ('Personal Accident', 'Personal Accident'),
        ('Pharmaceutical Production', 'Pharmaceutical Production'),
        ('PhotoModeler', 'PhotoModeler'),
        ('PicOS', 'PicOS'),
        ('PicTar', 'PicTar'),
        ('Pioneer Factor', 'Pioneer Factor'),
        ('Piping Isometrics', 'Piping Isometrics'),
        ('PL/1', 'PL/1'),
        ('Plant Layout Preparation', 'Plant Layout Preparation'),
        ('Plasma Cutting', 'Plasma Cutting'),
        ('Plasmas', 'Plasmas'),
        ('Platial', 'Platial'),
        ('PLC M', 'PLC M'),
        ('Pneumonia', 'Pneumonia'),
        ('Podcast Submissions', 'Podcast Submissions'),
        ('Political Participation', 'Political Participation'),
        ('Polypropylene', 'Polypropylene'),
        ('Poseidon for UML', 'Poseidon for UML'),
        ('PostGIS', 'PostGIS'),
        ('POSTMAN', 'POSTMAN'),
        ('Pre-Boot Authentication', 'Pre-Boot Authentication'),
        ('Predictive Learning', 'Predictive Learning'),
        ('Preparation', 'Preparation'),
        ('Primary Biliary Cirrhosis', 'Primary Biliary Cirrhosis'),
        ('Primer Design', 'Primer Design'),
        ('Print Marketing', 'Print Marketing'),
        ('Process Scheduler', 'Process Scheduler'),
        ('Product Analysis', 'Product Analysis'),
        ('Production Budgeting', 'Production Budgeting'),
        ('Professional Ethics', 'Professional Ethics'),
        ('Professional Negligence', 'Professional Negligence'),
        ('Profitability Manager', 'Profitability Manager'),
        ('Programmers', 'Programmers'),
        ('Programming for', 'Programming for'),
        ('Project Initiation', 'Project Initiation'),
        ('Project Purchasing', 'Project Purchasing'),
        ('Prolog', 'Prolog'),
        ('ProRealTime', 'ProRealTime'),
        ('Protein Expression', 'Protein Expression'),
        ('Psychological Assessment', 'Psychological Assessment'),
        ('Psychosocial', 'Psychosocial'),
        ('Python Class Mechanism', 'Python Class Mechanism'),
        ('Pyxplot', 'Pyxplot'),
        ('Q.SIG', 'Q.SIG'),
        ('Quality Assurance Professionals', 'Quality Assurance Professionals'),
        ('Quality Auditing', 'Quality Auditing'),
        ('Quality Center', 'Quality Center'),
        ('Quality Control Tools', 'Quality Control Tools'),
        ('RAC Administration', 'RAC Administration'),
        ('Raku', 'Raku'),
        ('Real Estate Financing', 'Real Estate Financing'),
        ('Reason 5', 'Reason 5'),
        ('Recover My Files', 'Recover My Files'),
        ('Remediation Engineering', 'Remediation Engineering'),
        ('Reporting', 'Reporting'),
        ('Rescue Diving', 'Rescue Diving'),
        ('Respiratory Quotient', 'Respiratory Quotient'),
        ('Reunion', 'Reunion'),
        ('Reverse Osmosis Plants', 'Reverse Osmosis Plants'),
        ('Revolving Lines of Credit', 'Revolving Lines of Credit'),
        ('Rhetoric', 'Rhetoric'),
        ('Ribosomal Binding Site', 'Ribosomal Binding Site'),
        ('RISC Architecture', 'RISC Architecture'),
        ('RNA Editing', 'RNA Editing'),
        ('RNAstructure', 'RNAstructure'),
        ('Robotics Hardware', 'Robotics Hardware'),
        ('Role Model', 'Role Model'),
        ('ROOT Statistical Software', 'ROOT Statistical Software'),
        ('RTI', 'RTI'),
        ('RuBot II', 'RuBot II'),
        ('Rural Health', 'Rural Health'),
        ('Safety Culture', 'Safety Culture'),
        ('SAG', 'SAG'),
        ('SAIL', 'SAIL'),
        ('Sales Brochures', 'Sales Brochures'),
        ('Sandwiches', 'Sandwiches'),
        ('SAP CRM 7.0', 'SAP CRM 7.0'),
        ('SAP EC', 'SAP EC'),
        ('SAP EHS', 'SAP EHS'),
        ('SAP EP', 'SAP EP'),
        ('SAP EWM', 'SAP EWM'),
        ('SAP FM', 'SAP FM'),
        ('SAP FSCM', 'SAP FSCM'),
        ('Sar (Unix)', 'Sar (Unix)'),
        ('SAS Macros', 'SAS Macros'),
        ('SAS/C C++', 'SAS/C C++'),
        ('Scandinavian', 'Scandinavian'),
        ('Schaefer Dichotomy Theorem', 'Schaefer Dichotomy Theorem'),
        ('Scheme - Strings', 'Scheme - Strings'),
        ('Scholarly Communication', 'Scholarly Communication'),
        ('Scratch Golfer', 'Scratch Golfer'),
        ('Scripting', 'Scripting'),
        ('Search & Rescue', 'Search & Rescue'),
        ('Selenium IDE', 'Selenium IDE'),
        ('Sell Side', 'Sell Side'),
        ('Sellerdeck', 'Sellerdeck'),
        ('Semantria', 'Semantria'),
        ('Sequential Erlang Programming', 'Sequential Erlang Programming'),
        ('Sequential Pattern Mining', 'Sequential Pattern Mining'),
        ('Servant', 'Servant'),
        ('Set Construction', 'Set Construction'),
        ('Shaft Alignment', 'Shaft Alignment'),
        ('SHARC', 'SHARC'),
        ('Shareplex', 'Shareplex'),
        ('Shortage Control', 'Shortage Control'),
        ('Sieve Analysis', 'Sieve Analysis'),
        ('Silk Test', 'Silk Test'),
        ('Silverstripe', 'Silverstripe'),
        ('SimGear', 'SimGear'),
        ('Similarity Learning', 'Similarity Learning'),
        ('Sintering', 'Sintering'),
        ('Sirius', 'Sirius'),
        ('Site Acquisition', 'Site Acquisition'),
        ('Site Maps', 'Site Maps'),
        ('Six Sigma Initiatives', 'Six Sigma Initiatives'),
        ('Slang', 'Slang'),
        ('S-Lang Programming Library', 'S-Lang Programming Library'),
        ('Smalltalk Compilers', 'Smalltalk Compilers'),
        ('Smart View', 'Smart View'),
        ('Software Project Management', 'Software Project Management'),
        ('Solarwinds SIEM', 'Solarwinds SIEM'),
        ('Solid Surface', 'Solid Surface'),
        ('Sony Vegas Video', 'Sony Vegas Video'),
        ('Soprano', 'Soprano'),
        ('Source Code Control System', 'Source Code Control System'),
        ('Spot Model Checker', 'Spot Model Checker'),
        ('SPV', 'SPV'),
        ('Spyder', 'Spyder'),
        ('SQL Commands', 'SQL Commands'),
        ('Stage Setting', 'Stage Setting'),
        ('Stamp Duties', 'Stamp Duties'),
        ('Start-up Environment', 'Start-up Environment'),
        ('Start-up Support', 'Start-up Support'),
        ('State Space Planning', 'State Space Planning'),
        ('Statistical semantics', 'Statistical semantics'),
        ('Stellent', 'Stellent'),
        ('Stones', 'Stones'),
        ('Storage engineering', 'Storage engineering'),
        ('Story Editing', 'Story Editing'),
        ('Strata 3D', 'Strata 3D'),
        ('Strategic Visionary', 'Strategic Visionary'),
        ('Studio', 'Studio'),
        ('Sub7', 'Sub7'),
        ('Subcontractor/Crew Supervision', 'Subcontractor/Crew Supervision'),
        ('Subfunctionalization', 'Subfunctionalization'),
        ('SuiteCRM', 'SuiteCRM'),
        ('Sulfonamides', 'Sulfonamides'),
        ('SuperMap', 'SuperMap'),
        ('Surgical Pathology', 'Surgical Pathology'),
        ('SVOX', 'SVOX'),
        ('System documentation', 'System documentation'),
        ('System Identification', 'System Identification'),
        ('Systems Ecology', 'Systems Ecology'),
        ('Tactics', 'Tactics'),
        ('Talent Development', 'Talent Development'),
        ('TCP/IP', 'TCP/IP'),
        ('Tcsh', 'Tcsh'),
        ('Team Operations', 'Team Operations'),
        ('TeamViewer', 'TeamViewer'),
        ('Techinline', 'Techinline'),
        ('Temperature', 'Temperature'),
        ('Teradici', 'Teradici'),
        ('Test Case Design', 'Test Case Design'),
        ('Test Development', 'Test Development'),
        ('Test Point Analysis', 'Test Point Analysis'),
        ('Testing for compatibility', 'Testing for compatibility'),
        ('The Robotic Workshop', 'The Robotic Workshop'),
        ('Thermophilic Microbes', 'Thermophilic Microbes'),
        ('ThinC', 'ThinC'),
        ('Thyroid Surgery', 'Thyroid Surgery'),
        ('TIBCO Designer', 'TIBCO Designer'),
        ('Tobacco Treatment', 'Tobacco Treatment'),
        ('Traffic channel operations', 'Traffic channel operations'),
        ('Transcription Factors', 'Transcription Factors'),
        ('Travel Coordination', 'Travel Coordination'),
        ('Tree Testing', 'Tree Testing'),
        ('Trimos', 'Trimos'),
        ('Troubleshooting Skills', 'Troubleshooting Skills'),
        ('Trustee', 'Trustee'),
        ('Turf', 'Turf'),
        ('TXL', 'TXL'),
        ('UMTS', 'UMTS'),
        ('Underground Mining', 'Underground Mining'),
        ('Underscore.js', 'Underscore.js'),
        ('Union Management', 'Union Management'),
        ('Unix Korn Shell Scripting', 'Unix Korn Shell Scripting'),
        ('Upgrading Rails', 'Upgrading Rails'),
        ('Varnish', 'Varnish'),
        ('VBC', 'VBC'),
        ('Vendor Master Data Management', 'Vendor Master Data Management'),
        ('Veraz', 'Veraz'),
        ('VGACAD', 'VGACAD'),
        ('Visual', 'Visual'),
        ('Visual SourceSafe ', 'Visual SourceSafe '),
        ('Viz Artist', 'Viz Artist'),
        ('V-Max', 'V-Max'),
        ('VMGL', 'VMGL'),
        ('VSD', 'VSD'),
        ('VSS', 'VSS'),
        ('Waste Water', 'Waste Water'),
        ('Water Resource Engineering', 'Water Resource Engineering'),
        ('WBTs', 'WBTs'),
        ('Web API', 'Web API'),
        ('WebDrive', 'WebDrive'),
        ('Websocket.js', 'Websocket.js'),
        ('WinSCP', 'WinSCP'),
    )

    class Meta():
        model = SkillsInfo
        exclude = ("fk_skills_user",)

    skills = forms.ChoiceField(choices=SKILL_LIST,)

    def __init__(self, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)

        self.fields['skills'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'required': 'required',
        }

class CompanyForm(forms.ModelForm):
    class Meta():
        model = CompanyInfo
        exclude = ("fk_company_user",)
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.fields['company_id'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Company ID',
            'required': 'required',
        }

        self.fields['company_tin'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Company TIN',
        }

        self.fields['designation'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Designation',
        }

        self.fields['department'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Department',
        } 

        self.fields['personal_tin'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Personal TIN',
        }

        self.fields['sss_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'SSS Number',
        }

        self.fields['pagibig'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Pag-ibig',
        }

        self.fields['philhealth'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Philhealth',
        }

class TelephoneNumberForm(forms.ModelForm):
    class Meta():
        model = TelephoneNumberInfo
        exclude = ("fk_telephone_user",)

    def __init__(self, *args, **kwargs):
        super(TelephoneNumberForm, self).__init__(*args, **kwargs)

        self.fields['telephone_number'].widget.attrs = {
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Telephone Number',
            'required': 'required',
        }

class CutOffPeriodForm(forms.ModelForm):
    attendance_file = forms.FileField(validators=[file_validator], label="Attendance .xlsx file")
    class Meta:
        model = CutOffPeriodInfo
        fields = ("attendance_file",)

class AttendanceForm(forms.ModelForm):
    class Meta():
        model = AttendanceInfo
        exclude = ("id", "employee_profile", "cut_off_period")

        time_in = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )

        time_out = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)

        self.fields['days_of_week'].label = False
        self.fields['days_of_week'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['date'].label = False
        self.fields['date'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
            
        }
        self.fields['time_in'].label = False
        self.fields['time_in'].widget.attrs = {
            'class': 'form-control timeIn timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['time_out'].label = False
        self.fields['time_out'].widget.attrs = { 
            'class': 'form-control timeOut timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['late'].label = False
        self.fields['late'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }   
        self.fields['undertime'].label = False
        self.fields['undertime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['overtime'].label = False
        self.fields['overtime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['payment_computation_for_work_done'].label = False
        self.fields['payment_computation_for_work_done'].widget.attrs = {
            'class': 'form-control select2',
        }
        self.fields['payment_computation_overtime'].label = False
        self.fields['payment_computation_overtime'].widget.attrs = {
            'class': 'form-control select2',
        }

class AttendanceFormManual(forms.ModelForm):
    class Meta():
        model = AttendanceInfo
        exclude = ("id", "employee_profile", "cut_off_period")

        time_in = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )

        time_out = forms.TimeField(
        widget=forms.TimeInput(
            format='%I:%M', 
        ),
        input_formats=('%I:%M',),
        required=False,
        )


    def __init__(self, *args, **kwargs):
        super(AttendanceFormManual, self).__init__(*args, **kwargs)

        self.fields['days_of_week'].label = False
        self.fields['days_of_week'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['date'].label = False
        self.fields['date'].widget.attrs = {
            'class': 'form-control mydate',
            'readonly': 'readonly',
            
        }
        self.fields['time_in'].label = False
        self.fields['time_in'].widget.attrs = {
            'class': 'form-control timeIn timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['time_out'].label = False
        self.fields['time_out'].widget.attrs = { 
            'class': 'form-control timeOut timepicker', 
            # 'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
        self.fields['late'].label = False
        self.fields['late'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }   
        self.fields['undertime'].label = False
        self.fields['undertime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['overtime'].label = False
        self.fields['overtime'].widget.attrs = {
            'class': 'form-control',
            'readonly': 'readonly',
        }
        self.fields['payment_computation_for_work_done'].label = False
        self.fields['payment_computation_for_work_done'].widget.attrs = {
            'class': 'form-control select2',
        }
        self.fields['payment_computation_overtime'].label = False
        self.fields['payment_computation_overtime'].widget.attrs = {
            'class': 'form-control select2',
        }
  
class EmployeePayrollForm(forms.ModelForm):
    default_val = Decimal('0.00')

    # payroll_date = forms.DateField(
    #     widget=forms.DateInput(
    #         format='%b %d %Y',
    #         attrs={
    #             'id': 'payroll_date',
    #         }
    #     ),
    #     input_formats=('%b %d %Y',)
    # )
    #monthly_rate = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    #monthly_allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    basic_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    overtime_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    legal_holiday = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    special_holiday = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    late_or_absences = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    salary_or_cash_advance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)

    # deductions
    sss_premiums = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    philhealth_contribution = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    pagibig_contribution = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    withholding_tax = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    pagibig_loan = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    deducted_salary_cash_advance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    #thirteenth_month_pay = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)


    class Meta():
        model = EmployeePayroll
        exclude = ("employee_fk","payroll_cutoff_period","payroll_date" ,"date_added","is_seen","monthly_rate","monthly_allowance","thirteenth_month_pay")
    
    def __init__(self, *args, **kwargs):
        super(EmployeePayrollForm, self).__init__(*args, **kwargs)

        self.fields['basic_pay'].widget.attrs = {
            'id':'basicPay',
            'class': 'form-control',
        }
        self.fields['allowance'].widget.attrs = {
            'id':'allowance',
            'class': 'form-control',
        }
        self.fields['overtime_pay'].widget.attrs = {
            'id':'overtimePay',
            'class': 'form-control',
        }
        self.fields['legal_holiday'].widget.attrs = {
            'id':'legalHoliday',
            'class': 'form-control',
        }
        self.fields['special_holiday'].widget.attrs = {
            'id':'sundaySpecialHoliday',
            'class': 'form-control',
        }
        self.fields['late_or_absences'].widget.attrs = {
            'id':'lateAbsences',
            'class': 'form-control',
        }
        self.fields['salary_or_cash_advance'].widget.attrs = {
            'id':'salaryCashAdvance',
            'class': 'form-control',
        } 
        self.fields['gross_pay'].widget.attrs = {
            'id': 'grossPay',
            'class': 'form-control text-green',
            'readonly': 'readonly',
        }
        self.fields['net_pay'].widget.attrs = {
            'id': 'netPay',
            'class': 'form-control text-green',
            'style': 'font-weight:bold;',
            'readonly': 'readonly',
        }
        #---
        self.fields['philhealth_contribution'].widget.attrs = {
            'id':'philhealContribution',
            'class': 'form-control',
        } 
        self.fields['pagibig_contribution'].widget.attrs = {
            'id':'pagibigContribution',
            'class': 'form-control',
        } 
        self.fields['sss_premiums'].widget.attrs = {
            'id':'sssPremius',
            'class': 'form-control',
        }
        self.fields['withholding_tax'].widget.attrs = {
            'id':'withholdingTax',
            'class': 'form-control',
        } 
        self.fields['pagibig_loan'].widget.attrs = {
            'id':'pagibigLoan',
            'class': 'form-control',
        } 
        self.fields['deducted_salary_cash_advance'].widget.attrs = {
            'id':'deductionSalaryCashAdvance',
            'class': 'form-control',
        }  
        self.fields['total_deduction'].widget.attrs = {
            'id': 'totalDeduction',
            'class': 'form-control text-red',
            'readonly': 'readonly',
        }

class EmployeeSalaryForm(forms.ModelForm):
    default_val = Decimal('0.00')
    amount = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    allowance = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val, required=True)
    class Meta():
        model = EmployeeSalary
        exclude = ("employee_salary_fk","date_added")

    def __init__(self, *args, **kwargs):
        super(EmployeeSalaryForm, self).__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the amount.",
        }
        self.fields['allowance'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the allowance.",
        }
        self.fields['reason'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
            'placeholder': "Enter the reason.",
        }

class EmployeeLeavesForm(forms.ModelForm):
    default_val = Decimal('0.00')
    leave_credits = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    less_this_application = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)
    balance_as_of_this_date = forms.DecimalField(max_digits=12, decimal_places=2, initial=default_val)

    class Meta():
            model = EmployeeLeaves
            exclude = ("employee_leave_fk","date_filed","department","status","noted_by","checked_by","approved_by",)

    def __init__(self, *args, **kwargs):
        super(EmployeeLeavesForm, self).__init__(*args, **kwargs)

        # self.fields['department'].widget.attrs = {
        #     'class': 'form-control', 

        #     'placeholder': "Enter the department.",
        # }
        #status must be disabled on the employee side
        # self.fields['status'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        self.fields['no_days'].widget.attrs = {
            'id': 'noOfDays',
            'class': 'form-control',  
            'readonly': 'readonly',
        }
        self.fields['inclusive_dates'].widget.attrs = {
            'id': 'inclusiveDates',
            'readonly': 'readonly',
            'class': 'form-control',  
        }
        self.fields['reasons'].widget.attrs = {
            'class': 'form-control', 
            'placeholder': "Enter the reasons.",
        }
        self.fields['classification_of_leave'].widget.attrs = {
            'id': 'classificationOfLeave',
            'class': 'form-control',  
            'style': 'width:100%',
        }
        self.fields['leave_credits'].widget.attrs = {
            'class': 'form-control',  
        }
        self.fields['less_this_application'].widget.attrs = {
            'class': 'form-control',  
        }
        self.fields['balance_as_of_this_date'].widget.attrs = {
            'class': 'form-control',  
        }
        # self.fields['noted_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        # self.fields['checked_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }
        # self.fields['approved_by'].widget.attrs = {
        #     'class': 'form-control',  
        # }

class EmployeeIteneraryForm(forms.ModelForm):
    class Meta():
            model = EmployeeItenerary
            exclude = ("employee_itenerary_fk","date_filed",)

    def __init__(self, *args, **kwargs):
        super(EmployeeIteneraryForm, self).__init__(*args, **kwargs)

class EmployeeIteneraryDetailsForm(forms.ModelForm):
    class Meta():
        model = EmployeeIteneraryDetails
        exclude = ("employee_itenerary",)

    def __init__(self, *args, **kwargs):
        super(EmployeeIteneraryDetailsForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs = {  
            'class': 'form-control frmEIDDate',   
            'readonly': 'readonly',
            #'required': 'required',
        }
        self.fields['timeIn'].widget.attrs = { 
            'class': 'form-control frmEIDTimeIn',  
            'readonly': 'readonly', 
            #'required': 'required',
        }
        self.fields['timeOut'].widget.attrs = { 
            'class': 'form-control frmEIDTimeOut', 
            'readonly': 'readonly',  
           # 'required': 'required',
        }
        self.fields['reasons'].widget.attrs = { 
            'class': 'form-control ifReasons',   
            #'required': 'required',
        }

class ConcernsEmployeeForm(forms.ModelForm):
    class Meta():
        model = Concerns
        exclude = ("sender","reply","date_filed",)
    def __init__(self, *args, **kwargs):
        super(ConcernsEmployeeForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].widget.attrs = {
            'id': 'concernTo',
            'style': 'width:100%',
            'required':'required', 
            'class': 'form-control',  
        }
        self.fields['subject'].widget.attrs = {
            'class': 'form-control',  
        }
        self.fields['message'].widget.attrs = {
            'class': 'form-control',  
        }

class ConcernsReplyEmployeeForm(forms.ModelForm):
    class Meta():
        model = Concerns
        exclude = ("sender","receiver","subject","message","date_filed",)
    def __init__(self, *args, **kwargs):
        super(ConcernsReplyEmployeeForm, self).__init__(*args, **kwargs)
      
      
        self.fields['reply'].widget.attrs = {
            'class': 'form-control',  
            'rows' : '5',
        }