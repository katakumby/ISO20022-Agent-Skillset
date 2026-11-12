---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.14 StatementFrequencyAndFormat <StmtFrqcyAndFrmt>", "3.4.4.2.1.14.2 CommunicationMethod <ComMtd>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.14.2 CommunicationMethod <ComMtd>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
Datatype: "Frequency7Code" on page 178
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
DAIL Daily Event takes place every day.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
TEND TenDays Event takes place every ten business
days.
MOVE TriggeredByMovement Event takes place at the end of the day if
there was a movement on the account,
otherwise nothing is sent that day.
WEEK Weekly Event takes place once a week.
INDA IntraDay Event takes place several times a day.
3.4.4.2.1.14.2  CommunicationMethod <ComMtd>
Presence: [1..1]
Definition: Specifies the communication method for statements.
CommunicationMethod <ComMtd> contains one of the following CommunicationMethod2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 84
Or}   Proprietary <Prtry> [1..1] Text 85
3.4.4.2.1.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication method using a code list.
Datatype: "CommunicationMethod2Code" on page 174
CodeName Name Definition
EMAL Email Transmission by e-mail.
FAXI Fax Transmission by fax.
FILE File Transmission by file transfer.
ONLI Online Transmission on line, for example, in a
web portal.
POST PostalService Transmission by postal service.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 84 August 2026
```

