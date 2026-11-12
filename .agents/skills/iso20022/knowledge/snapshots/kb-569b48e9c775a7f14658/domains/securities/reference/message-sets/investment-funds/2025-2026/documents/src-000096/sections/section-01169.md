---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.10 UnitsDetails <UnitsDtls>", "40.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "40.4.15.11.10.8.7 DigitalNetworkFee <DgtlNtwkFee>", "40.4.15.11.10.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1629, 1630]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.10.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1629 to 1630.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1629

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1629
     ISIN <ISIN> [0..1] IdentifierSet 1631
     OtherIdentification <OthrId> [0..*]  1631
       Identification <Id> [1..1] Text 1631
       Suffix <Sfx> [0..1] Text 1631
       Type <Tp> [1..1]  1631
{Or         Code <Cd> [1..1] CodeSet 1632
Or}         Proprietary <Prtry> [1..1] Text 1633
     Description <Desc> [0..1] Text 1633
   Quantity <Qty> [1..1]  1634
{Or     Quantity <Qty> [1..1] ± C23 1634
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1634
       Quantity <Qty> [1..1] Quantity 1635
       QuantityType <QtyTp> [1..1] Text 1635
       Issuer <Issr> [1..1] Text 1635
       SchemeName <SchmeNm> [0..1] Text 1635
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1635
40.4.15.11.10.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C21 "DescriptionPresenceRule", C22 "DescriptionUsageRule", C33 "ISINGuideline", C34
"ISINPresenceRule", C37 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1629 May 2026
```

## File page 1630

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1631
   OtherIdentification <OthrId> [0..*]  1631
     Identification <Id> [1..1] Text 1631
     Suffix <Sfx> [0..1] Text 1631
     Type <Tp> [1..1]  1631
{Or       Code <Cd> [1..1] CodeSet 1632
Or}       Proprietary <Prtry> [1..1] Text 1633
   Description <Desc> [0..1] Text 1633
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
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1630 May 2026
```

