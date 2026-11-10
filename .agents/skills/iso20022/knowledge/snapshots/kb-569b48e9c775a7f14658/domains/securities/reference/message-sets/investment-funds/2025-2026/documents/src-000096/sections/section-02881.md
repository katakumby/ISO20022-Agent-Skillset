---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.1 CashInPaymentInstrument <CshInPmtInstrm>", "55.4.5.21.1.1.3 DirectDebitDetails <DrctDbtDtls>", "55.4.5.21.1.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>"]
file_pages: [4047]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.1.3.4 DebtorNationalRegistrationNumber <DbtrNtlRegnNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4047 to 4047.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4047

```text
Datatype: "Max35Text" on page 5403
55.4.5.21.1.1.3.4  DebtorNationalRegistrationNumber <DbtrNtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to an entity.
Datatype: "Max35Text" on page 5403
55.4.5.21.1.1.3.5  Creditor <Cdtr>
Presence: [0..1]
Definition: Party that receives an amount of money from the debtor. In the context of the payment
model, the creditor is also the credit account owner.
Creditor <Cdtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
55.4.5.21.1.1.3.6  DebtorAgent <DbtrAgt>
Presence: [1..1]
Definition: Financial institution that receives the direct debit instruction from the creditor or other
authorised party.
DebtorAgent <DbtrAgt> contains the following FinancialInstitutionIdentification17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  4047
{Or     NameAndAddress <NmAndAdr> [1..1] ± 4048
Or     BICFI <BICFI> [1..1] IdentifierSet C6 4048
Or     ClearingSystemMemberIdentification
<ClrSysMmbId>
[1..1] ± 4048
Or}     ProprietaryIdentification <PrtryId> [1..1] Text 4049
   LEI <LEI> [0..1] IdentifierSet 4049
55.4.5.21.1.1.3.6.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the financial institution.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4047 May 2026
```

