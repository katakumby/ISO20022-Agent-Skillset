---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.25 Settlement Chain", "16.1.25.1 SettlementParties129", "16.1.25.1.1 Depository <Dpstry>"]
file_pages: [1134]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.25.1.1 Depository <Dpstry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1134 to 1134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1134

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1]  C3 1134
     Identification <Id> [1..1]  1135
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1135
Or       NameAndAddress <NmAndAdr> [1..1] ± 1136
Or       Country <Ctry> [1..1] CodeSet C3 1136
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1136
     ProcessingIdentification <PrcgId> [0..1] Text 1136
     AlternateIdentification <AltrnId> [0..*] ± 1136
   Party1 <Pty1> [0..1] ± C4, C54,
C56,
C58
1137
   Party2 <Pty2> [0..1] ± C4, C54,
C56,
C58
1138
   Party3 <Pty3> [0..1] ± C4, C54,
C56,
C58
1139
Constraints
• Party2PresenceRule
If Party 2 is present, then Party 1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party 3 is present, then Party 2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
16.1.25.1.1  Depository <Dpstry>
Presence: [0..1]
Definition: First receiving party in the settlement chain. In a plain vanilla settlement, it is the central
securities depository where the receiving side of the transaction requests to receive the financial
instrument.
Impacted by: C3 "AdditionalInforrmationRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1134 February 2026
```

