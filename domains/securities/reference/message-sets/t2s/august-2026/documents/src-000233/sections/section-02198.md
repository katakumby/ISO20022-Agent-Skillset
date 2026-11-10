---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.17 Identification Information"]
file_pages: [2961]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.17 Identification Information

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2961 to 2961.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2961

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.17 Identification Information
82.1.17.1  TransactionIdentifications55
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeIdentification <TradId> [0..*] Text 2961
   UniqueTransactionIdentifier <UnqTxIdr> [0..1] IdentifierSet 2962
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 2962
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 2962
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2962
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2962
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2962
   CommonIdentification <CmonId> [0..1] Text 2962
   NettingServiceProviderIdentification <NetgSvcPrvdrId> [0..1] Text 2962
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 2963
   RelatedTransactionIdentification <RltdTxId> [0..1] Text 2963
Constraints
• NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be NONREF.
82.1.17.1.1  TradeIdentification <TradId>
Presence: [0..*]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2961 August 2026
```

