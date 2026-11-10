---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.12 DigitalAssetSettlement <DgtlAsstSttlm>", "53.4.5.17.12.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [3674, 3675]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.12.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3674 to 3675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3674

```text
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3674
     ISIN <ISIN> [0..1] IdentifierSet 3676
     OtherIdentification <OthrId> [0..*]  3676
       Identification <Id> [1..1] Text 3676
       Suffix <Sfx> [0..1] Text 3676
       Type <Tp> [1..1]  3676
{Or         Code <Cd> [1..1] CodeSet 3677
Or}         Proprietary <Prtry> [1..1] Text 3678
     Description <Desc> [0..1] Text 3678
   Quantity <Qty> [1..1]  3679
{Or     Quantity <Qty> [1..1] ± C13 3679
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3679
       Quantity <Qty> [1..1] Quantity 3680
       QuantityType <QtyTp> [1..1] Text 3680
       Issuer <Issr> [1..1] Text 3680
       SchemeName <SchmeNm> [0..1] Text 3680
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3680
53.4.5.17.12.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C11 "DescriptionPresenceRule", C12 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C28 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3674 May 2026
```

## File page 3675

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3676
   OtherIdentification <OthrId> [0..*]  3676
     Identification <Id> [1..1] Text 3676
     Suffix <Sfx> [0..1] Text 3676
     Type <Tp> [1..1]  3676
{Or       Code <Cd> [1..1] CodeSet 3677
Or}       Proprietary <Prtry> [1..1] Text 3678
   Description <Desc> [0..1] Text 3678
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
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3675 May 2026
```

