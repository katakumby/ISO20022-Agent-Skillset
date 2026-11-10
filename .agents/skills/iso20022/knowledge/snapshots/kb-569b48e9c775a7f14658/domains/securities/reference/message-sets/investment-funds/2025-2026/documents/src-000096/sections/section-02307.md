---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.10 BulkCashSettlementDetails <BlkCshSttlmDtls>", "50.4.4.10.1 PaymentInstrument <PmtInstrm>", "50.4.4.10.1.3 DirectDebitDetails <DrctDbtDtls>", "50.4.4.10.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>"]
file_pages: [3224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.10.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3224 to 3224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3224

```text
Datatype: "Max35Text" on page 5403
50.4.4.10.1.3.4  DebtorNationalRegistrationNumber <DbtrNtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to an entity.
Datatype: "Max35Text" on page 5403
50.4.4.10.1.3.5  Creditor <Cdtr>
Presence: [0..1]
Definition: Party that receives an amount of money from the debtor. In the context of the payment
model, the creditor is also the credit account owner.
Creditor <Cdtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.10.1.3.6  DebtorAgent <DbtrAgt>
Presence: [1..1]
Definition: Financial institution that receives the direct debit instruction from the creditor or other
authorised party.
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  3224
{Or     NameAndAddress <NmAndAdr> [1..1] ± 3225
Or     BICFI <BICFI> [1..1] IdentifierSet C6 3225
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 3225
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 3226
   LEI <LEI> [0..1] IdentifierSet 3226
50.4.4.10.1.3.6.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3224 May 2026
```

