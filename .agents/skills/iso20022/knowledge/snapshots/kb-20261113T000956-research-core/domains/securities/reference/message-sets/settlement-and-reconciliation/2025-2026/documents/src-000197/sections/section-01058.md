---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.14 Identification Information", "35.1.14.12 References41Choice", "35.1.14.12.6 PoolIdentification <PoolId>"]
file_pages: [1497]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.14.12.6 PoolIdentification <PoolId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1497 to 1497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1497

```text
35.1.14.12.6  PoolIdentification <PoolId>
Presence: [1..1]
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 2192
35.1.14.12.7  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 2192
35.1.14.13  GenericIdentification36
Definition: Identification using a proprietary scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1497
   Issuer <Issr> [1..1] Text 1497
   SchemeName <SchmeNm> [0..1] Text 1497
35.1.14.13.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 2192
35.1.14.13.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 2192
35.1.14.13.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 2192
35.1.14.14  IdentificationSource3Choice
Definition: Choice between source of identification of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1498
Or}   Proprietary <Prtry> [1..1] Text 1498
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1497 March 2026
```

