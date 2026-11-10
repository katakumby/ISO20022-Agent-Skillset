---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.1 References <Refs>"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.1 References <Refs>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       FromDateTime <FrDtTm> [1..1] DateTime 65
Or       ToDateTime <ToDtTm> [1..1] DateTime 65
Or       FromToDateTime <FrToDtTm> [1..1] ± 66
Or       EqualDateTime <EQDtTm> [1..1] DateTime 66
Or}       NotEqualDateTime <NEQDtTm> [1..1] DateTime 66
   SettlementCurrency <SttlmCcy> [0..*] CodeSet C2 66
   SafekeepingAccountOwner <SfkpgAcctOwnr> [0..*] ± 66
   MessageOriginator <MsgOrgtr> [0..*] ± 67
   CounterpartSettlementParties <CntrptSttlmPties> [0..*] ± C12,
C13,
C14,
C15
67
   DeliveringSettlementParties <DlvrgSttlmPties> [0..*] ± C12,
C13,
C14,
C15
68
   ReceivingSettlementParties <RcvgSttlmPties> [0..*] ± C12,
C13,
C14,
C15
69
   TradeTransactionCondition <TradTxCond> [0..*] CodeSet 70
   SecuritiesTransactionCondition <SctiesTxCond> [0..*] ± 73
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 74
   ConditionalSecuritiesDelivery <CondlSctiesDlvry> [0..1] Indicator 74
   CountryOfIssue <CtryOfIsse> [0..*] CodeSet C5 74
   IssuerCSD <IssrCSD> [0..*] ± 74
   HoldIndicator <HldInd> [0..*]  75
{Or     Code <Cd> [1..1] CodeSet 75
Or}     Proprietary <Prtry> [1..1] ± 75
3.4.1.2.1  References <Refs>
Presence: [0..*]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 31 March 2026
```

