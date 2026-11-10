---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.2 CreditTransferDetails <CdtTrfDtls>", "49.4.5.13.1.2.13 CreditorAccount <CdtrAcct>"]
file_pages: [2978]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.2.13 CreditorAccount <CdtrAcct>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2978 to 2978.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2978

```text
Creditor <Cdtr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
49.4.5.13.1.2.13  CreditorAccount <CdtrAcct>
Presence: [1..1]
Definition: Unambiguous identification of the account of the creditor to which a credit entry will be
posted as a result of the payment transaction.
CreditorAccount <CdtrAcct> contains the following AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2978
{Or     IBAN <IBAN> [1..1] IdentifierSet C19 2978
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2979
Or}     Other <Othr> [1..1] ± 2979
   Name <Nm> [0..1] Text 2979
49.4.5.13.1.2.13.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C19 2978
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2979
Or}   Other <Othr> [1..1] ± 2979
49.4.5.13.1.2.13.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C19 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2978 May 2026
```

