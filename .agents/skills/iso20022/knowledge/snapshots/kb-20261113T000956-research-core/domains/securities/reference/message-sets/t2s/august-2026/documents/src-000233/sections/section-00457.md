---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.2 Structure"]
file_pages: [579]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 579 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 579

```text
24.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollValQry> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 580
   CollateralValueQueryDefinition <CollValQryDef> [0..1]  581
{Or     QueryName <QryNm> [1..1] Text 582
Or}     NewCriteria <NewCrit> [1..1]  582
       QueryName <QryNm> [0..1] Text 583
       SearchCriteria <SchCrit> [0..1]  C4 583
         CashAccountIdentification <CshAcctId> [0..1] ± 584
         Currency <Ccy> [0..*] CodeSet C1 584
         CashAccountOwner <CshAcctOwnr> [0..1] ± 585
         CashAccountServicer <CshAcctSvcr> [0..1] ± 585
         FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
585
         SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 586
         SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 587
       ReturnCriteria <RtrCrit> [0..1]  587
         CashAccountOwnerIndicator <CshAcctOwnrInd> [0..1] Indicator 587
         CashAccountServicerIndicator <CshAcctSvcrInd> [0..1] Indicator 588
         SecuritiesAccountOwnerIndicator <SctiesAcctOwnrInd> [0..1] Indicator 588
         SecuritiesAccountServicerIndicator <SctiesAcctSvcrInd> [0..1] Indicator 588
         TotalCollateralValuationIndicator <TtlCollValtnInd> [0..1] Indicator 588
         SecuritiesAccountIndicator <SctiesAcctInd> [0..1] Indicator 588
         Securities <Scties> [0..1] Indicator 588
   SupplementaryData <SplmtryData> [0..*] ± C12 589
24.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 579 August 2026
```

