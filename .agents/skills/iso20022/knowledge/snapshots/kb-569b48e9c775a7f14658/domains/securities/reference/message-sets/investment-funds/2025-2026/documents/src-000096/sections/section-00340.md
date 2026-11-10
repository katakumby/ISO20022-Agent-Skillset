---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.12 UnitsDetails <UnitsDtls>", "24.4.6.12.8 TransactionOverhead <TxOvrhd>", "24.4.6.12.8.7 DigitalNetworkFee <DgtlNtwkFee>", "24.4.6.12.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [474, 475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.12.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 474 to 475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 474

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
474
     ISIN <ISIN> [0..1] IdentifierSet 476
     OtherIdentification <OthrId> [0..*]  476
       Identification <Id> [1..1] Text 476
       Suffix <Sfx> [0..1] Text 476
       Type <Tp> [1..1]  476
{Or         Code <Cd> [1..1] CodeSet 477
Or}         Proprietary <Prtry> [1..1] Text 478
     Description <Desc> [0..1] Text 478
   Quantity <Qty> [1..1]  479
{Or     Quantity <Qty> [1..1] ± C14 479
Or}     ProprietaryQuantity <PrtryQty> [1..1]  479
       Quantity <Qty> [1..1] Quantity 480
       QuantityType <QtyTp> [1..1] Text 480
       Issuer <Issr> [1..1] Text 480
       SchemeName <SchmeNm> [0..1] Text 480
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 480
24.4.6.12.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C24 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 474 May 2026
```

## File page 475

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 476
   OtherIdentification <OthrId> [0..*]  476
     Identification <Id> [1..1] Text 476
     Suffix <Sfx> [0..1] Text 476
     Type <Tp> [1..1]  476
{Or       Code <Cd> [1..1] CodeSet 477
Or}       Proprietary <Prtry> [1..1] Text 478
   Description <Desc> [0..1] Text 478
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
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 475 May 2026
```

