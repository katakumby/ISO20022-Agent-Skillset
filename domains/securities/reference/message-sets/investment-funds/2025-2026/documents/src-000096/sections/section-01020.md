---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.8 TransactionOverhead <TxOvrhd>", "38.4.15.8.4.8.7 DigitalNetworkFee <DgtlNtwkFee>", "38.4.15.8.4.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1412, 1413]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1412 to 1413.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1412

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C18,
C19,
C27,
C28,
C31
1412
     ISIN <ISIN> [0..1] IdentifierSet 1414
     OtherIdentification <OthrId> [0..*]  1414
       Identification <Id> [1..1] Text 1414
       Suffix <Sfx> [0..1] Text 1414
       Type <Tp> [1..1]  1414
{Or         Code <Cd> [1..1] CodeSet 1415
Or}         Proprietary <Prtry> [1..1] Text 1416
     Description <Desc> [0..1] Text 1416
   Quantity <Qty> [1..1]  1417
{Or     Quantity <Qty> [1..1] ± C20 1417
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1417
       Quantity <Qty> [1..1] Quantity 1418
       QuantityType <QtyTp> [1..1] Text 1418
       Issuer <Issr> [1..1] Text 1418
       SchemeName <SchmeNm> [0..1] Text 1418
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1418
38.4.15.8.4.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C18 "DescriptionPresenceRule", C19 "DescriptionUsageRule", C27 "ISINGuideline", C28
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1412 May 2026
```

## File page 1413

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1414
   OtherIdentification <OthrId> [0..*]  1414
     Identification <Id> [1..1] Text 1414
     Suffix <Sfx> [0..1] Text 1414
     Type <Tp> [1..1]  1414
{Or       Code <Cd> [1..1] CodeSet 1415
Or}       Proprietary <Prtry> [1..1] Text 1416
   Description <Desc> [0..1] Text 1416
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1413 May 2026
```

