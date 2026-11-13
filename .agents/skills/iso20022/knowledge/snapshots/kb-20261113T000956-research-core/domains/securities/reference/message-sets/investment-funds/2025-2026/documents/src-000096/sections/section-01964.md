---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "47.4.4.12.1 PaymentInstrument <PmtInstrm>", "47.4.4.12.1.3 DirectDebitDetails <DrctDbtDtls>", "47.4.4.12.1.3.1 DebtorAccount <DbtrAcct>", "47.4.4.12.1.3.1.1 Identification <Id>"]
file_pages: [2741]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.12.1.3.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2741 to 2741.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2741

```text
Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made
as a result of the transaction.
DebtorAccount <DbtrAcct> contains the following AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2741
{Or     IBAN <IBAN> [1..1] IdentifierSet C20 2741
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2741
Or}     Other <Othr> [1..1] ± 2742
   Name <Nm> [0..1] Text 2742
47.4.4.12.1.3.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C20 2741
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2741
Or}   Other <Othr> [1..1] ± 2742
47.4.4.12.1.3.1.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C20 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
47.4.4.12.1.3.1.1.2  BlockChainCashWallet <BlckChainCshWllt>
Presence: [1..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2741 May 2026
```

