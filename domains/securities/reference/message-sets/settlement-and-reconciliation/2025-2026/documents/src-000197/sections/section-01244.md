---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.25 PartyIdentification315"]
file_pages: [1701]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.25 PartyIdentification315

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1701 to 1701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1701

```text
35.1.18.25  PartyIdentification315
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1701
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1701
Or     NameAndAddress <NmAndAdr> [1..1] ± 1702
Or     Country <Ctry> [1..1] CodeSet C7 1702
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1702
   LEI <LEI> [0..1] IdentifierSet 1702
   AlternateIdentification <AltrnId> [0..1] ± 1702
   ProcessingDate <PrcgDt> [0..1] ± 1703
   ProcessingIdentification <PrcgId> [0..1] Text 1703
   AdditionalInformation <AddtlInf> [0..1] ± C5 1703
35.1.18.25.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Identification <Id> contains one of the following PartyIdentification257Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1701
Or   NameAndAddress <NmAndAdr> [1..1] ± 1702
Or   Country <Ctry> [1..1] CodeSet C7 1702
Or}   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1702
35.1.18.25.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Unique and unambiguous way to identify an organisation.
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1701 March 2026
```

