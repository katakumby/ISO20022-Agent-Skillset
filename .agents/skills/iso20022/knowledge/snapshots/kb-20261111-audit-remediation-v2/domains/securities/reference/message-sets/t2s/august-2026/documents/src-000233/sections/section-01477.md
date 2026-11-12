---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.4 Message Building Blocks", "37.4.2 ReportOrError <RptOrErr>", "37.4.2.1 PartyReport <PtyRpt>", "37.4.2.1.2 PartyOrError <PtyOrErr>", "37.4.2.1.2.1 SystemParty <SysPty>", "37.4.2.1.2.1.12 Restriction <Rstrctn>"]
file_pages: [2095]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.4.2.1.2.1.12 Restriction <Rstrctn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2095 to 2095.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2095

```text
37.4.2.1.2.1.12  Restriction <Rstrctn>
Presence: [0..*]
Definition: Defines the specific processing characteristics for a party to ensure configurability of specific
requirements, as prescribed by national legal and regulatory requirements and practices.
Restriction <Rstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 2095
   ValidTo <VldTo> [0..1] DateTime 2095
   Type <Tp> [1..1] Text 2095
37.4.2.1.2.1.12.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 3320
37.4.2.1.2.1.12.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 3320
37.4.2.1.2.1.12.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 3328
37.4.2.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2095
{Or     Code <Cd> [1..1] CodeSet 2096
Or}     Proprietary <Prtry> [1..1] Text 2096
   Description <Desc> [0..1] Text 2096
37.4.2.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2095 August 2026
```

