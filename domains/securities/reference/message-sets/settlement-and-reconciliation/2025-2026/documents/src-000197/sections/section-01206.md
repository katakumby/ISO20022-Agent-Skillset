---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.1 PartyIdentification314", "35.1.18.1.3 ProcessingIdentification <PrcgId>"]
file_pages: [1663]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.1.3 ProcessingIdentification <PrcgId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1663 to 1663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1663

```text
Datatype: "LEIIdentifier" on page 2187
35.1.18.1.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction for the party identified.
Datatype: "Max35Text" on page 2192
35.1.18.2  PartyIdentification125Choice
Definition: Choice of formats for the identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1663
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1663
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1663
35.1.18.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Identification of the party expressed as a BIC.
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.18.2.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to the party using a proprietary identification
scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 1500 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1500
   SchemeName <SchmeNm> [0..1] Text 1501
   Issuer <Issr> [0..1] Text 1501
35.1.18.2.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1663 March 2026
```

