---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.17 Organisation Identification", "35.1.17.1 OrganisationIdentification31", "35.1.17.1.2 Other <Othr>", "35.1.17.1.2.2 SchemeName <SchmeNm>", "35.1.17.1.2.2.2 Proprietary <Prtry>"]
file_pages: [1661]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.17.1.2.2.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1661 to 1661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1661

```text
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalOrganisationIdentification1Code" on page 2065
35.1.17.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 2192
35.1.17.1.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 2192
35.1.18 Party Identification
35.1.18.1  PartyIdentification314
Definition: Identification of a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1661
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1662
Or     NameAndAddress <NmAndAdr> [1..1] ± 1662
Or     Country <Ctry> [1..1] CodeSet C7 1662
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1662
   LEI <LEI> [0..1] IdentifierSet 1662
   ProcessingIdentification <PrcgId> [0..1] Text 1663
35.1.18.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following PartyIdentification257Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1662
Or   NameAndAddress <NmAndAdr> [1..1] ± 1662
Or   Country <Ctry> [1..1] CodeSet C7 1662
Or}   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1662
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1661 March 2026
```

