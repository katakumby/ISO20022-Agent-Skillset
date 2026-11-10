---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.21 DigitalAssetSettlement <DgtlAsstSttlm>", "55.4.5.20.21.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [3987, 3988]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.21.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3987 to 3988.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3987

```text
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3987
     ISIN <ISIN> [0..1] IdentifierSet 3989
     OtherIdentification <OthrId> [0..*]  3989
       Identification <Id> [1..1] Text 3989
       Suffix <Sfx> [0..1] Text 3989
       Type <Tp> [1..1]  3989
{Or         Code <Cd> [1..1] CodeSet 3990
Or}         Proprietary <Prtry> [1..1] Text 3991
     Description <Desc> [0..1] Text 3991
   Quantity <Qty> [1..1]  3992
{Or     Quantity <Qty> [1..1] ± C14 3992
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3992
       Quantity <Qty> [1..1] Quantity 3993
       QuantityType <QtyTp> [1..1] Text 3993
       Issuer <Issr> [1..1] Text 3993
       SchemeName <SchmeNm> [0..1] Text 3993
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3993
55.4.5.20.21.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3987 May 2026
```

## File page 3988

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3989
   OtherIdentification <OthrId> [0..*]  3989
     Identification <Id> [1..1] Text 3989
     Suffix <Sfx> [0..1] Text 3989
     Type <Tp> [1..1]  3989
{Or       Code <Cd> [1..1] CodeSet 3990
Or}       Proprietary <Prtry> [1..1] Text 3991
   Description <Desc> [0..1] Text 3991
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
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3988 May 2026
```

