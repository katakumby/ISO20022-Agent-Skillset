---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.12 ReceivingSettlementParties <RcvgSttlmPties>", "22.4.13.4 CreditorAgent <CdtrAgt>"]
file_pages: [759]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.13.4 CreditorAgent <CdtrAgt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 759 to 759.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 759

```text
Creditor <Cdtr> contains the following elements (see "PartyIdentificationAndAccount223" on
page 1695 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1696
   LEI <LEI> [0..1] IdentifierSet 1696
   AlternateIdentification <AltrnId> [0..1] ± 1696
   CashAccount <CshAcct> [0..1] ± 1696
   ChargesAccount <ChrgsAcct> [0..1] ± 1696
   CommissionAccount <ComssnAcct> [0..1] ± 1697
   TaxAccount <TaxAcct> [0..1] ± 1697
   AdditionalInformation <AddtlInf> [0..1] ± C5 1697
22.4.13.4  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
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
22.4.14 SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 759 March 2026
```

