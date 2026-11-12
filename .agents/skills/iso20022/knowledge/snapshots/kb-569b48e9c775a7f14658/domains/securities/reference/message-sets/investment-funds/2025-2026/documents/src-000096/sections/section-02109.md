---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.2 CreditTransferDetails <CdtTrfDtls>", "49.4.5.13.1.2.1 Reference <Ref>"]
file_pages: [2956]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.2.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2956 to 2956.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2956

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CreditorAccount <CdtrAcct> [1..1]  2978
     Identification <Id> [1..1]  2978
{Or       IBAN <IBAN> [1..1] IdentifierSet C19 2978
Or       BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2979
Or}       Other <Othr> [1..1] ± 2979
     Name <Nm> [0..1] Text 2979
49.4.5.13.1.2.1  Reference <Ref>
Presence: [0..1]
Definition: Information supplied to enable the matching of an entry with the items that the transfer is
intended to settle, such as commercial invoices in an accounts' receivable system.
Datatype: "Max35Text" on page 5403
49.4.5.13.1.2.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor. In the context of the payment
model, the debtor is also the debit account owner.
Debtor <Dbtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.13.1.2.3  DebtorAccount <DbtrAcct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made
as a result of the transaction.
DebtorAccount <DbtrAcct> contains the following AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2956
{Or     IBAN <IBAN> [1..1] IdentifierSet C19 2957
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2957
Or}     Other <Othr> [1..1] ± 2957
   Name <Nm> [0..1] Text 2958
49.4.5.13.1.2.3.1  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2956 May 2026
```

