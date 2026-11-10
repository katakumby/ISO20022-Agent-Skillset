---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.20 StatementFrequencyAndFormat <StmtFrqcyAndFrmt>", "2.4.5.20.2 CommunicationMethod <ComMtd>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.20.2 CommunicationMethod <ComMtd>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
CodeName Name Definition
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
2.4.5.20.2  CommunicationMethod <ComMtd>
Presence: [1..1]
Definition: Specifies the communication method for statements.
CommunicationMethod <ComMtd> contains one of the following CommunicationMethod2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 33
Or}   Proprietary <Prtry> [1..1] Text 33
2.4.5.20.2.1  Code <Cd>
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
2.4.5.20.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication method using a bilaterally or
multilaterally agreed description.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 33 August 2026
```

