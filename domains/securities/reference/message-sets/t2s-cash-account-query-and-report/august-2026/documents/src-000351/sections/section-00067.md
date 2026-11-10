---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.1 Identification <Id>"]
file_pages: [81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.1 Identification <Id>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 81 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 81

```text
3.4.4.2.1.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the account.
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 134 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C11 134
Or}   Other <Othr> [1..1] ± 135
3.4.4.2.1.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max70Text" on page 185
3.4.4.2.1.3  Status <Sts>
Presence: [0..1]
Definition: Specifies the current state of an account, eg, enabled or deleted.
Datatype: "AccountStatus3Code" on page 172
CodeName Name Definition
ENAB Enabled Account can be used for its intended
purpose.
DISA Disabled Account cannot be used for its intended
purpose, either temporarily or
permanently.
DELE Deleted Account cannot be used any longer.
FORM ProForma Account is temporary and can be
partially used for its intended purpose.
The account will be fully available for use
when the account servicer has received
all relevant documents.
3.4.4.2.1.4  Type <Tp>
Presence: [0..1]
Definition: Type of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 133 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 133
Or}   Proprietary <Prtry> [1..1] Text 133
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 81 August 2026
```

