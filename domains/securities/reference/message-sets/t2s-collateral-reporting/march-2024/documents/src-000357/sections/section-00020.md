---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>"]
file_pages: [22, 23]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1 BusinessReport <BizRpt>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 22 to 23.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                 SchemeName <SchmeNm> [0..1] Text 35
                 Balance <Bal> [1..1] Quantity 35
Or}               QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
                 Quantity <Qty> [1..1] ± 36
                 AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
           ValuationPrice <ValtnPric> [1..1]  36
             AmountPriceType <AmtPricTp> [1..1] ± 37
             PriceValue <PricVal> [1..1] ± 37
             FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 37
             PriceFixingDate <PricFxgDt> [1..1] Date 38
           CollateralValue <CollVal> [1..1] Amount C1, C6 38
Or}   OperationalError <OprlErr> [1..*]  38
     Error <Err> [1..1]  38
{Or       Code <Cd> [1..1] CodeSet 39
Or}       Proprietary <Prtry> [1..1] Text 39
     Description <Desc> [0..1] Text 39
3.4.2.1  BusinessReport <BizRpt>
Presence: [1..*]
Definition: Provides information specific to the collateral value reports included in the message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
22 March 2024
```

## File page 23

```text
BusinessReport <BizRpt> contains the following CollateralValueReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [1..1] ± C11,
C10
24
   CashAccountOwner <CshAcctOwnr> [0..1]  25
     Name <Nm> [0..1] Text 25
     Identification <Id> [1..1] ± 25
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 25
   CashAccountServicer <CshAcctSvcr> [0..1] ± 25
   SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 26
   SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 26
   CollateralValueReport <CollValRpt> [0..*]  27
{Or     BusinessError <BizErr> [1..1]  29
       Error <Err> [1..1]  29
{Or         Code <Cd> [1..1] CodeSet 29
Or}         Proprietary <Prtry> [1..1] Text 29
       Description <Desc> [0..1] Text 29
Or}     CollateralValue <CollVal> [1..1]  29
       DataAccessTime <DataAccsTm> [1..1] DateTime 30
       TotalCollateralValuation <TtlCollValtn> [0..1] Amount C1, C6 30
       SecuritiesAccount <SctiesAcct> [0..1] ± 31
       Securities <Scties> [0..*]  31
         Identification <Id> [0..*] ± C7, C8,
C12,
C13,
C14
32
         Position <Pos> [0..*]  33
           Type <Tp> [1..1] Text 34
           Quantity <Qty> [1..1]  34
{Or             Quantity <Qty> [1..1] ± 35
Or             Proprietary <Prtry> [1..1]  35
               Identification <Id> [1..1] Text 35
               Issuer <Issr> [1..1] Text 35
               SchemeName <SchmeNm> [0..1] Text 35
               Balance <Bal> [1..1] Quantity 35
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
23 March 2024
```

