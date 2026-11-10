---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.12 Identification Information", "9.1.12.2 GenericIdentification36", "9.1.12.2.1 Identification <Id>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.12.2.1 Identification <Id>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 225
   Issuer <Issr> [1..1] Text 225
   SchemeName <SchmeNm> [0..1] Text 225
9.1.12.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 345
9.1.12.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 345
9.1.12.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 345
9.1.12.3  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 225
Or}   Proprietary <Prtry> [1..1] Text 225
9.1.12.3.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: "ExternalFinancialInstrumentIdentificationType1Code" on page 326
9.1.12.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: "Max35Text" on page 345
9.1.12.4  GenericIdentification37
Definition: Identification expressed as a proprietary type and narrative description.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 225 September 2025
```

