---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.16 Restriction <Rstrctn>", "3.4.4.2.1.16.1 RestrictionType <RstrctnTp>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.16.1 RestrictionType <RstrctnTp>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
Restriction <Rstrctn> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  86
{Or     Code <Cd> [1..1] Text 86
Or}     Proprietary <Prtry> [1..1] ± 86
   ValidFrom <VldFr> [1..1] DateTime 86
   ValidUntil <VldUntil> [0..1] DateTime 87
3.4.4.2.1.16.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction.
RestrictionType <RstrctnTp> contains one of the following CodeOrProprietary1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 86
Or}   Proprietary <Prtry> [1..1] ± 86
3.4.4.2.1.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Element expressed as an ISO 20022 code from an external list.
Datatype: "Max4Text" on page 184
3.4.4.2.1.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Element expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 144 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   SchemeName <SchmeNm> [0..1] Text 145
   Issuer <Issr> [1..1] Text 145
3.4.4.2.1.16.2  ValidFrom <VldFr>
Presence: [1..1]
Definition: Date from when the restriction is valid.
Datatype: "ISODateTime" on page 180
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 86 August 2026
```

