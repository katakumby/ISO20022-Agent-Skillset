---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>"]
file_pages: [596, 597]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1 BusinessReport <BizRpt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 596 to 597.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 596

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
                 SchemeName <SchmeNm> [0..1] Text 609
                 Balance <Bal> [1..1] Quantity 609
Or}               QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
                 Quantity <Qty> [1..1] ± 610
                 AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
           ValuationPrice <ValtnPric> [1..1]  610
             AmountPriceType <AmtPricTp> [1..1] ± 611
             PriceValue <PricVal> [1..1] ± 611
             FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 611
             PriceFixingDate <PricFxgDt> [1..1] Date 612
           CollateralValue <CollVal> [1..1] Amount C1, C6 612
Or}   OperationalError <OprlErr> [1..*]  612
     Error <Err> [1..1]  612
{Or       Code <Cd> [1..1] CodeSet 613
Or}       Proprietary <Prtry> [1..1] Text 613
     Description <Desc> [0..1] Text 613
25.4.2.1  BusinessReport <BizRpt>
Presence: [1..*]
Definition: Provides information specific to the collateral value reports included in the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 596 August 2026
```

## File page 597

```text
BusinessReport <BizRpt> contains the following CollateralValueReport4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccount <CshAcct> [1..1] ± C11,
C10
598
   CashAccountOwner <CshAcctOwnr> [0..1]  599
     Name <Nm> [0..1] Text 599
     Identification <Id> [1..1] ± 599
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 599
   CashAccountServicer <CshAcctSvcr> [0..1] ± 599
   SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 600
   SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 600
   CollateralValueReport <CollValRpt> [0..*]  601
{Or     BusinessError <BizErr> [1..1]  603
       Error <Err> [1..1]  603
{Or         Code <Cd> [1..1] CodeSet 603
Or}         Proprietary <Prtry> [1..1] Text 603
       Description <Desc> [0..1] Text 603
Or}     CollateralValue <CollVal> [1..1]  603
       DataAccessTime <DataAccsTm> [1..1] DateTime 604
       TotalCollateralValuation <TtlCollValtn> [0..1] Amount C1, C6 604
       SecuritiesAccount <SctiesAcct> [0..1] ± 605
       Securities <Scties> [0..*]  605
         Identification <Id> [0..*] ± C7, C8,
C12,
C13,
C14
606
         Position <Pos> [0..*]  607
           Type <Tp> [1..1] Text 608
           Quantity <Qty> [1..1]  608
{Or             Quantity <Qty> [1..1] ± 609
Or             Proprietary <Prtry> [1..1]  609
               Identification <Id> [1..1] Text 609
               Issuer <Issr> [1..1] Text 609
               SchemeName <SchmeNm> [0..1] Text 609
               Balance <Bal> [1..1] Quantity 609
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 597 August 2026
```

