---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.10 UnitsDetails <UnitsDtls>", "36.4.15.11.10.8 TransactionOverhead <TxOvrhd>", "36.4.15.11.10.8.7 DigitalNetworkFee <DgtlNtwkFee>", "36.4.15.11.10.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1246, 1247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.10.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1246 to 1247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1246

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
1246
     ISIN <ISIN> [0..1] IdentifierSet 1248
     OtherIdentification <OthrId> [0..*]  1248
       Identification <Id> [1..1] Text 1248
       Suffix <Sfx> [0..1] Text 1248
       Type <Tp> [1..1]  1248
{Or         Code <Cd> [1..1] CodeSet 1249
Or}         Proprietary <Prtry> [1..1] Text 1250
     Description <Desc> [0..1] Text 1250
   Quantity <Qty> [1..1]  1251
{Or     Quantity <Qty> [1..1] ± C23 1251
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1251
       Quantity <Qty> [1..1] Quantity 1252
       QuantityType <QtyTp> [1..1] Text 1252
       Issuer <Issr> [1..1] Text 1252
       SchemeName <SchmeNm> [0..1] Text 1252
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1252
36.4.15.11.10.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C21 "DescriptionPresenceRule", C22 "DescriptionUsageRule", C33 "ISINGuideline", C34
"ISINPresenceRule", C37 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1246 May 2026
```

## File page 1247

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1248
   OtherIdentification <OthrId> [0..*]  1248
     Identification <Id> [1..1] Text 1248
     Suffix <Sfx> [0..1] Text 1248
     Type <Tp> [1..1]  1248
{Or       Code <Cd> [1..1] CodeSet 1249
Or}       Proprietary <Prtry> [1..1] Text 1250
   Description <Desc> [0..1] Text 1250
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
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1247 May 2026
```

