---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.10 Pledgee3", "35.1.18.10.1 PledgeeTypeAndIdentification <PldgeeTpAndId>", "35.1.18.10.1.1 TypeAndIdentification <TpAndId>"]
file_pages: [1676]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.10.1.1 TypeAndIdentification <TpAndId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1676 to 1676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1676

```text
PledgeeTypeAndIdentification <PldgeeTpAndId> contains one of the following
PledgeeFormat5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TypeAndIdentification <TpAndId> [1..1]  1676
     Identification <Id> [1..1] IdentifierSet C5 1676
     PledgeeType <PldgeeTp> [1..1] CodeSet 1676
Or   Identification <Id> [1..1]  1677
     Identification <Id> [0..1] Text 1677
     PledgeeType <PldgeeTp> [1..1] CodeSet 1677
Or}   Proprietary <Prtry> [1..1] ± 1677
35.1.18.10.1.1  TypeAndIdentification <TpAndId>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged expressed as a code
and a BIC.
TypeAndIdentification <TpAndId> contains the following PledgeeTypeAndAnyBICIdentifier2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet C5 1676
   PledgeeType <PldgeeTp> [1..1] CodeSet 1676
35.1.18.10.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity to which the financial instruments are pledged, expressed as a BIC.
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.18.10.1.1.2  PledgeeType <PldgeeTp>
Presence: [1..1]
Definition: Entity to which the financial instruments are pledged expressed as a code.
Datatype: "PledgeeType1Code" on page 2111
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1676 March 2026
```

