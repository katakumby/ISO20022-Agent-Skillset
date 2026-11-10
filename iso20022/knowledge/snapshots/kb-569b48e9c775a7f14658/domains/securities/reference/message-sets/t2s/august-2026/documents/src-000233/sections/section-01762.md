---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.1 QueryType <QryTp>"]
file_pages: [2421]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.1 QueryType <QryTp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2421 to 2421.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2421

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         NotEqualDate <NEQDt> [1..1] Date 2461
Or}       DateTime <DtTm> [1..1]  2461
{Or         FromDateTime <FrDtTm> [1..1] DateTime 2461
Or         ToDateTime <ToDtTm> [1..1] DateTime 2461
Or         FromToDateTime <FrToDtTm> [1..1] ± 2462
Or         EqualDateTime <EQDtTm> [1..1] DateTime 2462
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 2462
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
{Or       Code <Cd> [1..1] CodeSet 2471
Or}       Proprietary <Prtry> [1..1] ± 2471
71.4.1.1  QueryType <QryTp>
Presence: [1..1]
Definition: Defines the type of query.
Datatype: "SettlementQueryType1Code" on page 3300
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2421 August 2026
```

