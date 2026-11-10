---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.21 Restriction <Rstrctn>", "2.4.5.21.1 RestrictionType <RstrctnTp>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.21.1 RestrictionType <RstrctnTp>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
2.4.5.21.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction.
RestrictionType <RstrctnTp> contains one of the following CodeOrProprietary1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 35
Or}   Proprietary <Prtry> [1..1] ± 35
2.4.5.21.1.1  Code <Cd>
Presence: [1..1]
Definition: Element expressed as an ISO 20022 code from an external list.
Datatype: "Max4Text" on page 184
2.4.5.21.1.2  Proprietary <Prtry>
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
2.4.5.21.2  ValidFrom <VldFr>
Presence: [1..1]
Definition: Date from when the restriction is valid.
Datatype: "ISODateTime" on page 180
2.4.5.21.3  ValidUntil <VldUntil>
Presence: [0..1]
Definition: Date until when the restriction is valid.
Datatype: "ISODateTime" on page 180
2.4.5.22  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Date when the account will be or was closed.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 35 August 2026
```

