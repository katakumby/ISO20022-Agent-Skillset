---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.24 CashParties41", "35.1.18.24.5 Intermediary <Intrmy>"]
file_pages: [1700]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.24.5 Intermediary <Intrmy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1700 to 1700.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1700

```text
CreditorAgent <CdtrAgt> contains the following elements (see "PartyIdentificationAndAccount224" on
page 1692 for details)
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
35.1.18.24.5  Intermediary <Intrmy>
Presence: [0..1]
Definition: Financial institution through which the transaction must pass to reach the account with
institution.
Intermediary <Intrmy> contains the following elements (see "PartyIdentificationAndAccount224" on
page 1692 for details)
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1700 March 2026
```

