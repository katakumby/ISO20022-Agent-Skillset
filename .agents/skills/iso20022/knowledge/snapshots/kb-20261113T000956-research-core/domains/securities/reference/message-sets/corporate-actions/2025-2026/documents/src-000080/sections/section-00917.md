---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.25 Settlement Chain", "16.1.25.1 SettlementParties129", "16.1.25.1.1 Depository <Dpstry>", "16.1.25.1.1.1 Identification <Id>"]
file_pages: [1135]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.25.1.1.1 Identification <Id>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1135 to 1135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1135

```text
Depository <Dpstry> contains the following PartyIdentification316 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1135
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1135
Or     NameAndAddress <NmAndAdr> [1..1] ± 1136
Or     Country <Ctry> [1..1] CodeSet C3 1136
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1136
   ProcessingIdentification <PrcgId> [0..1] Text 1136
   AlternateIdentification <AltrnId> [0..*] ± 1136
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
16.1.25.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Identification <Id> contains one of the following PartyIdentification257Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1135
Or   NameAndAddress <NmAndAdr> [1..1] ± 1136
Or   Country <Ctry> [1..1] CodeSet C3 1136
Or}   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1136
16.1.25.1.1.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1244
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1135 February 2026
```

