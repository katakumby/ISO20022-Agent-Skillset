---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.22 PartyIdentificationAndAccount224"]
file_pages: [1692]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.22 PartyIdentificationAndAccount224

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1692 to 1692.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1692

```text
Definition: Alternate identification for a party.
Datatype: "Max35Text" on page 2192
35.1.18.22  PartyIdentificationAndAccount224
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1692
{Or     BICFI <BICFI> [1..1] IdentifierSet C8 1692
Or     NameAndAddress <NmAndAdr> [1..1] ± 1693
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1693
   LEI <LEI> [0..1] IdentifierSet 1693
   AlternateIdentification <AltrnId> [0..1] ± 1693
   CashAccount <CshAcct> [0..1] ± 1694
   ChargesAccount <ChrgsAcct> [0..1] ± 1694
   CommissionAccount <ComssnAcct> [0..1] ± 1694
   TaxAccount <TaxAcct> [0..1] ± 1695
   AdditionalInformation <AddtlInf> [0..1] ± C5 1695
35.1.18.22.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following PartyIdentification133Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICFI <BICFI> [1..1] IdentifierSet C8 1692
Or   NameAndAddress <NmAndAdr> [1..1] ± 1693
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1693
35.1.18.22.1.1  BICFI <BICFI>
Presence: [1..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority, as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C8 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 2186
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1692 March 2026
```

