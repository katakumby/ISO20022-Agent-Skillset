---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.1 References <Refs>"]
file_pages: [2427]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.1 References <Refs>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2427 to 2427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2427

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       FromDateTime <FrDtTm> [1..1] DateTime 2461
Or       ToDateTime <ToDtTm> [1..1] DateTime 2461
Or       FromToDateTime <FrToDtTm> [1..1] ± 2462
Or       EqualDateTime <EQDtTm> [1..1] DateTime 2462
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 2462
   SettlementCurrency <SttlmCcy> [0..*] CodeSet C2 2462
   SafekeepingAccountOwner <SfkpgAcctOwnr> [0..*] ± 2462
   MessageOriginator <MsgOrgtr> [0..*] ± 2463
   CounterpartSettlementParties <CntrptSttlmPties> [0..*] ± C12,
C13,
C14,
C15
2463
   DeliveringSettlementParties <DlvrgSttlmPties> [0..*] ± C12,
C13,
C14,
C15
2464
   ReceivingSettlementParties <RcvgSttlmPties> [0..*] ± C12,
C13,
C14,
C15
2465
   TradeTransactionCondition <TradTxCond> [0..*] CodeSet 2466
   SecuritiesTransactionCondition <SctiesTxCond> [0..*] ± 2469
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 2470
   ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 2470
   CountryOfIssue <CtryOfIsse> [0..*] CodeSet C5 2470
   IssuerCSD <IssrCSD> [0..*] ± 2470
   HoldIndicator <HldInd> [0..*]  2471
{Or     Code <Cd> [1..1] CodeSet 2471
Or}     Proprietary <Prtry> [1..1] ± 2471
71.4.1.2.1  References <Refs>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2427 August 2026
```

