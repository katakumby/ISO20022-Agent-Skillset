---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.2 CreditTransferDetails <CdtTrfDtls>", "47.4.4.8.20.1.2.7 IntermediaryAgent1Account <IntrmyAgt1Acct>"]
file_pages: [2656]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.2.7 IntermediaryAgent1Account <IntrmyAgt1Acct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2656 to 2656.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2656

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
47.4.4.8.20.1.2.7  IntermediaryAgent1Account <IntrmyAgt1Acct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the intermediary agent 1 at its servicing agent in
the payment chain.
IntermediaryAgent1Account <IntrmyAgt1Acct> contains the following
AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  2656
{Or     IBAN <IBAN> [1..1] IdentifierSet C20 2656
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2657
Or}     Other <Othr> [1..1] ± 2657
   Name <Nm> [0..1] Text 2657
47.4.4.8.20.1.2.7.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C20 2656
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 2657
Or}   Other <Othr> [1..1] ± 2657
47.4.4.8.20.1.2.7.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C20 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2656 May 2026
```

