---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.2 Name <Nm>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.2 Name <Nm>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 134 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C11 134
Or}   Other <Othr> [1..1] ± 135
2.4.5.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max70Text" on page 185
2.4.5.3  Status <Sts>
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
2.4.5.4  Type <Tp>
Presence: [0..1]
Definition: Type of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 133 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 133
Or}   Proprietary <Prtry> [1..1] Text 133
2.4.5.5  Currency <Ccy>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 29 August 2026
```

