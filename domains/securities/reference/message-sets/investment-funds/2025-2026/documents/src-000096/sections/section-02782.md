---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.23 DigitalAssetSettlement <DgtlAsstSttlm>", "55.4.5.19.23.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [3915, 3916]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.23.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3915 to 3916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3915

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
3915
     ISIN <ISIN> [0..1] IdentifierSet 3917
     OtherIdentification <OthrId> [0..*]  3917
       Identification <Id> [1..1] Text 3917
       Suffix <Sfx> [0..1] Text 3917
       Type <Tp> [1..1]  3917
{Or         Code <Cd> [1..1] CodeSet 3918
Or}         Proprietary <Prtry> [1..1] Text 3919
     Description <Desc> [0..1] Text 3919
   Quantity <Qty> [1..1]  3920
{Or     Quantity <Qty> [1..1] ± C14 3920
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3920
       Quantity <Qty> [1..1] Quantity 3921
       QuantityType <QtyTp> [1..1] Text 3921
       Issuer <Issr> [1..1] Text 3921
       SchemeName <SchmeNm> [0..1] Text 3921
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3921
55.4.5.19.23.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3915 May 2026
```

## File page 3916

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3917
   OtherIdentification <OthrId> [0..*]  3917
     Identification <Id> [1..1] Text 3917
     Suffix <Sfx> [0..1] Text 3917
     Type <Tp> [1..1]  3917
{Or       Code <Cd> [1..1] CodeSet 3918
Or}       Proprietary <Prtry> [1..1] Text 3919
   Description <Desc> [0..1] Text 3919
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
Investment Funds - Maintenance 2025 - 2026 3916 May 2026
```

