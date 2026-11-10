---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.6 RequestDetails <ReqDtls>", "5.4.3.4.6.1 Reference <Ref>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.6.1 Reference <Ref>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 123
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 123
Or       PoolIdentification <PoolId> [1..1] Text 124
Or}       OtherTransactionIdentification <OthrTxId> [1..1] Text 124
     ReferenceOwner <RefOwnr> [0..1] ± 124
Constraints
• ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
• OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and receiver.
• SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
5.4.3.4.6.1  Reference <Ref>
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
[0..1] Text 117
   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[0..1] Text 117
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 117
   CounterpartyMarketInfrastructureTransactionIdentific
ation <CtrPtyMktInfrstrctrTxId>
[0..1] Text 117
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 117
   PoolIdentification <PoolId> [0..1] Text 117
   CommonIdentification <CmonId> [0..1] Text 118
   TradeIdentification <TradId> [0..1] Text 118
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 116 September 2025
```

