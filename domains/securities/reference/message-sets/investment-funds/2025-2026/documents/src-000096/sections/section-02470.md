---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "52.4.5.12.1 PaymentInstrument <PmtInstrm>", "52.4.5.12.1.2 CreditTransferDetails <CdtTrfDtls>", "52.4.5.12.1.2.9 IntermediaryAgent2Account <IntrmyAgt2Acct>"]
file_pages: [3457]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.12.1.2.9 IntermediaryAgent2Account <IntrmyAgt2Acct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3457 to 3457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3457

```text
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
52.4.5.12.1.2.9  IntermediaryAgent2Account <IntrmyAgt2Acct>
Presence: [0..1]
Definition: Unambiguous identification of the account of the intermediary agent 2 at its servicing agent in
the payment chain.
IntermediaryAgent2Account <IntrmyAgt2Acct> contains the following
AccountIdentificationAndName8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3457
{Or     IBAN <IBAN> [1..1] IdentifierSet C22 3457
Or     BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3458
Or}     Other <Othr> [1..1] ± 3458
   Name <Nm> [0..1] Text 3458
52.4.5.12.1.2.9.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following AccountIdentification82Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C22 3457
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 3458
Or}   Other <Othr> [1..1] ± 3458
52.4.5.12.1.2.9.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C22 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3457 May 2026
```

