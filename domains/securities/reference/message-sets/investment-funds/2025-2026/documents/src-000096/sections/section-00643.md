---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.16 UnitsDetails <UnitsDtls>", "34.4.4.16.8 TransactionOverhead <TxOvrhd>", "34.4.4.16.8.7 DigitalNetworkFee <DgtlNtwkFee>", "34.4.4.16.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [876, 877]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.16.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 876 to 877.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 876

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C20,
C21,
C23
876
     ISIN <ISIN> [0..1] IdentifierSet 878
     OtherIdentification <OthrId> [0..*]  878
       Identification <Id> [1..1] Text 878
       Suffix <Sfx> [0..1] Text 878
       Type <Tp> [1..1]  878
{Or         Code <Cd> [1..1] CodeSet 879
Or}         Proprietary <Prtry> [1..1] Text 880
     Description <Desc> [0..1] Text 880
   Quantity <Qty> [1..1]  881
{Or     Quantity <Qty> [1..1] ± C13 881
Or}     ProprietaryQuantity <PrtryQty> [1..1]  881
       Quantity <Qty> [1..1] Quantity 882
       QuantityType <QtyTp> [1..1] Text 882
       Issuer <Issr> [1..1] Text 882
       SchemeName <SchmeNm> [0..1] Text 882
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 882
34.4.4.16.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C23 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 876 May 2026
```

## File page 877

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 878
   OtherIdentification <OthrId> [0..*]  878
     Identification <Id> [1..1] Text 878
     Suffix <Sfx> [0..1] Text 878
     Type <Tp> [1..1]  878
{Or       Code <Cd> [1..1] CodeSet 879
Or}       Proprietary <Prtry> [1..1] Text 880
   Description <Desc> [0..1] Text 880
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
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 877 May 2026
```

