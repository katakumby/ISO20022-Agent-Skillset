---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.4 Mandate <Mndt>", "3.4.4.2.4.7 StartDate <StartDt>"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.4.7 StartDate <StartDt>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
BankOperation <BkOpr> contains the following elements (see "BankTransactionCodeStructure4" on
page 135 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Domain <Domn> [0..1] ± 136
   Proprietary <Prtry> [0..1]  136
     Code <Cd> [1..1] Text 136
     Issuer <Issr> [0..1] Text 136
Constraints
• DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
3.4.4.2.4.7  StartDate <StartDt>
Presence: [0..1]
Definition: Specifies the date when the mandate becomes valid.
Datatype: "ISODate" on page 179
3.4.4.2.4.8  EndDate <EndDt>
Presence: [0..1]
Definition: Specifies the date when the mandate stops to be valid.
Datatype: "ISODate" on page 179
3.4.4.2.5  ReferenceAccount <RefAcct>
Presence: [0..1]
Definition: Unique and unambiguous identification of the account used as a reference for the opening of
another account.
Impacted by: C13 "IdentificationOrProxyPresenceRule", C12 "IdentificationAndProxyGuideline"
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 98 August 2026
```

