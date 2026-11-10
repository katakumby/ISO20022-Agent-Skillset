---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.8 AccountOwner <AcctOwnr>", "3.4.4.2.8.1 AnyBIC <AnyBIC>"]
file_pages: [101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.8.1 AnyBIC <AnyBIC>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 101 to 101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 101

```text
AccountOwner <AcctOwnr> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C3 101
   LEI <LEI> [0..1] IdentifierSet 101
   Other <Othr> [0..*]  101
     Identification <Id> [1..1] Text 102
     SchemeName <SchmeNm> [0..1]  102
{Or       Code <Cd> [1..1] CodeSet 102
Or}       Proprietary <Prtry> [1..1] Text 102
     Issuer <Issr> [0..1] Text 102
3.4.4.2.8.1  AnyBIC <AnyBIC>
Presence: [0..1]
Definition: Business identification code of the organisation.
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 180
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
3.4.4.2.8.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 181
3.4.4.2.8.3  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 101 August 2026
```

