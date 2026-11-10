---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.1 Reference <Ref>"]
file_pages: [2812]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.1 Reference <Ref>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2812 to 2812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2812

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       EndTime <EndTm> [0..1] DateTime 2825
   NetMovementDetails <NetMvmntDtls> [0..1]  2825
     SafekeepingAccount <SfkpgAcct> [0..1] ± 2826
     SecuritiesShortfall <SctiesShrtfll> [0..1] ± 2826
     ShortfallValuation <ShrtfllValtn> [0..1] ± 2826
     TradeTransactionCondition <TradTxCond> [0..*] ± 2827
     NumberOfEntries <NbOfNtries> [0..1] Quantity 2827
81.4.6.11.4.9.1  Reference <Ref>
Presence: [1..1]
Definition: Reference of the transaction for which penalties are provided.
Impacted by: C12 "NoAccountOwnerTransactionIdentificationRule"
Reference <Ref> contains the following elements (see "TransactionIdentifications55" on page 2961 for
details)
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
81.4.6.11.4.9.2  ReferenceOwner <RefOwnr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2812 August 2026
```

