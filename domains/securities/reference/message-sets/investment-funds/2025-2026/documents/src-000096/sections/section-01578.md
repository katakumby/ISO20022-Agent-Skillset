---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.21 CashSettlementDetails <CshSttlmDtls>", "44.4.4.9.21.1 PaymentInstrument <PmtInstrm>", "44.4.4.9.21.1.1 CreditTransferDetails <CdtTrfDtls>", "44.4.4.9.21.1.1.1 Reference <Ref>"]
file_pages: [2215]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.21.1.1.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2215 to 2215.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2215

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditorAccount <CdtrAcct> [1..1]  2237
     Identification <Id> [1..1]  2237
{Or       IBAN <IBAN> [1..1] IdentifierSet C20 2237
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2238
Or}       Other <Othr> [1..1] ± 2238
     Name <Nm> [0..1] Text 2238
44.4.4.9.21.1.1.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
44.4.4.9.21.1.1.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor. In the context of the payment
model, the debtor is also the debit account owner.
Debtor <Dbtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
44.4.4.9.21.1.1.3  DebtorAccount <DbtrAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made
as a result of the transaction.
DebtorAccount <DbtrAcct> contains the following AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2215
{Or     IBAN <IBAN> [1..1] IdentifierSet C20 2216
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2216
Or}     Other <Othr> [1..1] ± 2216
   Name <Nm> [0..1] Text 2217
44.4.4.9.21.1.1.3.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2215 May 2026
```

