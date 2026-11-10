---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["8 reda.041.001.02 PartyActivityAdviceV02", "8.4 Message Building Blocks", "8.4.2 PartyActivity <PtyActvty>", "8.4.2.2 Change <Chng>", "8.4.2.2.2 Record <Rcrd>", "8.4.2.2.2.4 ClosingDate <ClsgDt>"]
file_pages: [97]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 8.4.2.2.2.4 ClosingDate <ClsgDt>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 97 to 97.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 97

```text
Definition: New value after the update.
Datatype: "ISODate" on page 184
8.4.2.2.2.4  ClosingDate <ClsgDt>
Presence: [1..1]
Definition: Specifies the closing date of the party.
ClosingDate <ClsgDt> contains the following UpdateLogDate1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] Date 97
   New <New> [1..1] Date 97
8.4.2.2.2.4.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Datatype: "ISODate" on page 184
8.4.2.2.2.4.2  New <New>
Presence: [1..1]
Definition: New value after the update.
Datatype: "ISODate" on page 184
8.4.2.2.2.5  Type <Tp>
Presence: [1..1]
Definition: Specifies the type classification of the party.
Type <Tp> contains the following UpdateLogSystemPartyType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1]  97
{Or     Code <Cd> [1..1] CodeSet 98
Or}     Proprietary <Prtry> [1..1] Text 98
   New <New> [1..1]  98
{Or     Code <Cd> [1..1] CodeSet 98
Or}     Proprietary <Prtry> [1..1] Text 98
8.4.2.2.2.5.1  Old <Od>
Presence: [1..1]
Definition: Old value before the update.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
97 March 2024
```

