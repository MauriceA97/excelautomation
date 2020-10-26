from enum import Enum


class AutoNumber(Enum):
     def __new__(cls):
         value = len(cls.__members__) + 1
         obj = object.__new__(cls)
         obj._value_ = value
         return obj

class AgentType(AutoNumber):
    AMBETTER      = () 
    AVMED         = ()
    BRIGHT_HEALTH = ()
    CIGNA         = ()
    MOLINA        = ()
    OSCAR         = ()
    WORKAGENTS    = ()
    

# Finish me

def set_agent_type(agent_type):
    agent = {
        AgentType.AMBETTER.value: {
            'subject':'AMBETTER COMMISSION STATEMENT SEPTEMBER 2020',
            'body': '''
            Hello Agent, 
            Please read the following instructions before claiming any policy. This will help you to avoid duplicate tasks. · Please find the attached the Ambetter Commission Statement of SEPTEMBER 2020, which was deposited into your bank account on 10/14/2020. · Keep in mind that the report is made based on the report received from Ambetter. · As an Agent Appointed with Ambetter, please utilize your broker portal to check the Broker Linkage Date and payment of premium paid through date before 09/27/2020. You must to verify the information before claiming any missing member for commission. In case there is a policy that needs to be reviewed, please use the spreadsheet “Amb_Broker Recon. Report” attached in this email. Also, Ambetter has a new rule to send a Reconciliation; 4.4.3. 120-Day Rule. Plan will not adjust any incorrect payments to Producer, except for payments made within 120-days prior to the date of adjustment, payments made as a result of fraud or incorrect information provided to Plan by Producer or a Sub-Producer, or as otherwise provided in Sections 4.7, 5.5, 5.7 and 6.5. In this regard, neither Producer nor Plan may assert a claim against the other relating to an incorrect payment amount under the terms of this Agreement unless such claim is made (and the resulting adjustment is commenced) within 120-days of the date of said incorrect payment
            
            Thank you

            Ricardo Hernandez
            Commissions Department
            Phone number: 786-471-6219
            Direct E-Fax: 305-357-9341
            Email: ricardo.h@sunshinelifehealth.com

            Confidentiality Notice: This message (and any attachment) is intended only for the use of the individual or entity to which it is addressed and may contain
            information that is privileged and/or confidential under applicable law. If the reader of this message is not the intended recipient  or the person responsible for
            delivering the message, you are hereby notified that any dissemination, distribution or copying of this communication is strictly prohibited. If you have
            received this communication in error, please notify Sunshine Life & Health Advisors immediately by returning it to the sender and delete this copy from your
            system. Thank You.
            '''
        },
        AgentType.AVMED.value: {
            'subject':'AVMED COMMISSION STATEMENT SEPTEMBER 2020'
        },
        AgentType.BRIGHT_HEALTH.value: {
            'subject':'BRIGHT_HEALTH COMMISSION STATEMENT SEPTEMBER 2020'
        },
        AgentType.CIGNA.value: {
            'subject':'CIGNA COMMISSION STATEMENT SEPTEMBER 2020'
        },
        AgentType.MOLINA.value: {
            'subject':'MOLINA COMMISSION STATEMENT SEPTEMBER 2020'
        },
        AgentType.OSCAR.value: {
            'subject':'OSCAR COMMISSION STATEMENT SEPTEMBER 2020',
            'body': '''
            Hello Agent,
            Please find the attached Oscar Commission Statement September 2020, which was deposited into
            your bank account on 10/20/2020.
            • Keep in mind that the report is made based on the report received from Oscar. If you need to
            reconcile your commission paid, please review the Oscar broker portal 
            https://accounts.hioscar.com/account/login/?client_context=business before add any discrepancy in the 
            spreadsheet that I have attached in this email and send it directly at commissions@hioscar.com
            
            Thank you

            Ricardo Hernandez
            Commissions Department
            Phone number: 786-471-6219
            Direct E-Fax: 305-357-9341
            Email: ricardo.h@sunshinelifehealth.com

            Confidentiality Notice: This message (and any attachment) is intended only for the use of the individual or entity to which it is addressed and may contain
            information that is privileged and/or confidential under applicable law. If the reader of this message is not the intended recipient  or the person responsible for
            delivering the message, you are hereby notified that any dissemination, distribution or copying of this communication is strictly prohibited. If you have
            received this communication in error, please notify Sunshine Life & Health Advisors immediately by returning it to the sender and delete this copy from your
            system. Thank You.
            '''
        },
        AgentType.WORKAGENTS.value: {
            'subject':'WORKAGENTS COMMISSION STATEMENT SEPTEMBER 2020'
        }
    }

    return agent.get(agent_type, 'Invalid value')