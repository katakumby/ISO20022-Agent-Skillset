---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.6 RequestDetails <ReqDtls>", "76.4.3.4.6.1 Reference <Ref>"]
file_pages: [2671]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.6.1 Reference <Ref>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2671 to 2671.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2671

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 2678
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 2678
Or       PoolIdentification <PoolId> [1..1] Text 2679
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 2679
     ReferenceOwner <RefOwnr> [0..1] ± 2679
Constraints
• ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and receiver.
• SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
76.4.3.4.6.1  Reference <Ref>
Presence: [1..1]
Definition: References of the transaction for which the securities settlement condition modification is
requested.
Impacted by: C23 "ReferencePresenceRule"
Reference <Ref> contains the following References32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[0..1] Text 2672
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 2672
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 2672
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 2672
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 2672
   PoolIdentification <PoolId> [0..1] Text 2672
   CommonIdentification <CmonId> [0..1] Text 2673
   TradeIdentification <TradId> [0..1] Text 2673
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2671 August 2026
```

