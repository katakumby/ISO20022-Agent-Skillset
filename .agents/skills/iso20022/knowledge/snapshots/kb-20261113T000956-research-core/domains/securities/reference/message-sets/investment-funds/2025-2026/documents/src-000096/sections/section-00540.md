---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.8 TransactionOverhead <TxOvrhd>", "30.4.7.16.8.7 DigitalNetworkFee <DgtlNtwkFee>", "30.4.7.16.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [738, 739]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 738 to 739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 738

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
738
     ISIN <ISIN> [0..1] IdentifierSet 740
     OtherIdentification <OthrId> [0..*]  740
       Identification <Id> [1..1] Text 740
       Suffix <Sfx> [0..1] Text 740
       Type <Tp> [1..1]  740
{Or         Code <Cd> [1..1] CodeSet 741
Or}         Proprietary <Prtry> [1..1] Text 742
     Description <Desc> [0..1] Text 742
   Quantity <Qty> [1..1]  743
{Or     Quantity <Qty> [1..1] ± C14 743
Or}     ProprietaryQuantity <PrtryQty> [1..1]  743
       Quantity <Qty> [1..1] Quantity 744
       QuantityType <QtyTp> [1..1] Text 744
       Issuer <Issr> [1..1] Text 744
       SchemeName <SchmeNm> [0..1] Text 744
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 744
30.4.7.16.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C25 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 738 May 2026
```

## File page 739

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 740
   OtherIdentification <OthrId> [0..*]  740
     Identification <Id> [1..1] Text 740
     Suffix <Sfx> [0..1] Text 740
     Type <Tp> [1..1]  740
{Or       Code <Cd> [1..1] CodeSet 741
Or}       Proprietary <Prtry> [1..1] Text 742
   Description <Desc> [0..1] Text 742
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
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 739 May 2026
```

