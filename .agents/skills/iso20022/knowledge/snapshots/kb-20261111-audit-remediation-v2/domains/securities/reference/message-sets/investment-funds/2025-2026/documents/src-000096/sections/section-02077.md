---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.3 DirectDebitDetails <DrctDbtDtls>", "49.4.5.9.34.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>"]
file_pages: [2913]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2913 to 2913.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2913

```text
Datatype: "Max35Text" on page 5403
49.4.5.9.34.1.3.4  DebtorNationalRegistrationNumber <DbtrNtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to an entity.
Datatype: "Max35Text" on page 5403
49.4.5.9.34.1.3.5  Creditor <Cdtr>
Presence: [0..1]
Definition: Party that receives an amount of money from the debtor. In the context of the payment
model, the creditor is also the credit account owner.
Creditor <Cdtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.9.34.1.3.6  DebtorAgent <DbtrAgt>
Presence: [1..1]
Definition: Financial institution that receives the direct debit instruction from the creditor or other
authorised party.
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  2913
{Or     NameAndAddress <NmAndAdr> [1..1] ± 2914
Or     BICFI <BICFI> [1..1] IdentifierSet C7 2914
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 2914
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 2915
   LEI <LEI> [0..1] IdentifierSet 2915
49.4.5.9.34.1.3.6.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2913 May 2026
```

