---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.9 Identification Information", "12.1.9.5 GenericIdentification36", "12.1.9.5.2 Issuer <Issr>"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.9.5.2 Issuer <Issr>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: Max35Text on page 493
12.1.9.5.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
12.1.9.5.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: Max35Text on page 493
12.1.9.6  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 400
Or}   Proprietary <Prtry> [1..1] Text 400
12.1.9.6.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification source, as assigned via a pre-determined code list.
Datatype: ExternalFinancialInstrumentIdentificationType1Code on page 477
12.1.9.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification source using a proprietary identification scheme.
Datatype: Max35Text on page 493
12.1.9.7  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
12.1.9.7.1  Identification <Id>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 400
```

