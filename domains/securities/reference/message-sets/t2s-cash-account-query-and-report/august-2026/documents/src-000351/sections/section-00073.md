---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.16 Restriction <Rstrctn>", "3.4.4.2.1.16.3 ValidUntil <VldUntil>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.16.3 ValidUntil <VldUntil>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
3.4.4.2.1.16.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 180
3.4.4.2.1.17  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Date when the account was opened.
Datatype: "ISODate" on page 179
3.4.4.2.2  UnderlyingMasterAgreement <UndrlygMstrAgrmt>
Presence: [0..1]
Definition: Account contract established between the organisation or the group to which the
organisation belongs, and the account servicer. This contract has to be applied for the new account to
be opened and maintained.
UnderlyingMasterAgreement <UndrlygMstrAgrmt> contains the following ContractDocument1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 87
   SignOffDate <SgnOffDt> [0..1] Date 87
   Version <Vrsn> [0..1] Text 87
3.4.4.2.2.1  Reference <Ref>
Presence: [1..1]
Definition: Account contract established between the organisation or the group to which the
organisation belongs, and the account servicer. This contract has to be applied for the new account to
be opened and maintained.
Datatype: "Max35Text" on page 183
3.4.4.2.2.2  SignOffDate <SgnOffDt>
Presence: [0..1]
Definition: Signoff date of the document.
Datatype: "ISODate" on page 179
3.4.4.2.2.3  Version <Vrsn>
Presence: [0..1]
Definition: Identification of the version of the contract.
Datatype: "Max6Text" on page 184
3.4.4.2.3  ContractDates <CtrctDts>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 87 August 2026
```

