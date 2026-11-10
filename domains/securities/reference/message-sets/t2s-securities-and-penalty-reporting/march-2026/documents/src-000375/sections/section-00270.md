---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.16 Identification Information"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.16 Identification Information

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
7.1.16 Identification Information
7.1.16.1  TransactionIdentifications55
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 347
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 347
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 347
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 348
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 348
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 348
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 348
   CommonIdentification <CmonId> [0..1] Text 348
   NettingServiceProviderIdentification <NetgSvcPrvdrId> [0..1] Text 348
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 348
   RelatedTransactionIdentification <RltdTxId> [0..1] Text 349
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
7.1.16.1.1  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 557
7.1.16.1.2  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [0..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 553
7.1.16.1.3  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account owner (or the
instructing party managing the account).
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 347 March 2026
```

