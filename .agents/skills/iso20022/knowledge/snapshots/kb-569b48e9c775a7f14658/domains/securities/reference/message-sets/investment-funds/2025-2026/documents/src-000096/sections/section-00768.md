---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.8 TransactionOverhead <TxOvrhd>", "35.4.14.10.9.8.7 DigitalNetworkFee <DgtlNtwkFee>", "35.4.14.10.9.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1051, 1052]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1051 to 1052.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1051

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C20,
C21,
C31,
C32,
C35
1051
     ISIN <ISIN> [0..1] IdentifierSet 1053
     OtherIdentification <OthrId> [0..*]  1053
       Identification <Id> [1..1] Text 1053
       Suffix <Sfx> [0..1] Text 1053
       Type <Tp> [1..1]  1053
{Or         Code <Cd> [1..1] CodeSet 1054
Or}         Proprietary <Prtry> [1..1] Text 1055
     Description <Desc> [0..1] Text 1055
   Quantity <Qty> [1..1]  1056
{Or     Quantity <Qty> [1..1] ± C22 1056
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1056
       Quantity <Qty> [1..1] Quantity 1057
       QuantityType <QtyTp> [1..1] Text 1057
       Issuer <Issr> [1..1] Text 1057
       SchemeName <SchmeNm> [0..1] Text 1057
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1057
35.4.14.10.9.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C20 "DescriptionPresenceRule", C21 "DescriptionUsageRule", C31 "ISINGuideline", C32
"ISINPresenceRule", C35 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1051 May 2026
```

## File page 1052

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1053
   OtherIdentification <OthrId> [0..*]  1053
     Identification <Id> [1..1] Text 1053
     Suffix <Sfx> [0..1] Text 1053
     Type <Tp> [1..1]  1053
{Or       Code <Cd> [1..1] CodeSet 1054
Or}       Proprietary <Prtry> [1..1] Text 1055
   Description <Desc> [0..1] Text 1055
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
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1052 May 2026
```

