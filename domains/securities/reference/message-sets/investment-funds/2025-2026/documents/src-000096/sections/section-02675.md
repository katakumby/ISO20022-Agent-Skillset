---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.2 CashOutPaymentInstrument <CshOutPmtInstrm>", "53.4.5.18.1.2.1 CreditTransferDetails <CdtTrfDtls>", "53.4.5.18.1.2.1.1 Reference <Ref>"]
file_pages: [3758]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.2.1.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3758 to 3758.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3758

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditorAccount <CdtrAcct> [1..1]  3780
     Identification <Id> [1..1]  3780
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 3780
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3781
Or}       Other <Othr> [1..1] ± 3781
     Name <Nm> [0..1] Text 3781
53.4.5.18.1.2.1.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
53.4.5.18.1.2.1.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor. In the context of the payment
model, the debtor is also the debit account owner.
Debtor <Dbtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.18.1.2.1.3  DebtorAccount <DbtrAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made
as a result of the transaction.
DebtorAccount <DbtrAcct> contains the following AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3758
{Or     IBAN <IBAN> [1..1] IdentifierSet C19 3759
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3759
Or}     Other <Othr> [1..1] ± 3759
   Name <Nm> [0..1] Text 3760
53.4.5.18.1.2.1.3.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3758 May 2026
```

