---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.18 TransactionOverhead <TxOvrhd>", "55.4.5.19.18.7 DigitalNetworkFee <DgtlNtwkFee>", "55.4.5.19.18.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [3890, 3891]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.18.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3890 to 3891.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3890

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C27
3890
     ISIN <ISIN> [0..1] IdentifierSet 3892
     OtherIdentification <OthrId> [0..*]  3892
       Identification <Id> [1..1] Text 3892
       Suffix <Sfx> [0..1] Text 3892
       Type <Tp> [1..1]  3892
{Or         Code <Cd> [1..1] CodeSet 3893
Or}         Proprietary <Prtry> [1..1] Text 3894
     Description <Desc> [0..1] Text 3894
   Quantity <Qty> [1..1]  3895
{Or     Quantity <Qty> [1..1] ± C14 3895
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3895
       Quantity <Qty> [1..1] Quantity 3896
       QuantityType <QtyTp> [1..1] Text 3896
       Issuer <Issr> [1..1] Text 3896
       SchemeName <SchmeNm> [0..1] Text 3896
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3896
55.4.5.19.18.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3890 May 2026
```

## File page 3891

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3892
   OtherIdentification <OthrId> [0..*]  3892
     Identification <Id> [1..1] Text 3892
     Suffix <Sfx> [0..1] Text 3892
     Type <Tp> [1..1]  3892
{Or       Code <Cd> [1..1] CodeSet 3893
Or}       Proprietary <Prtry> [1..1] Text 3894
   Description <Desc> [0..1] Text 3894
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
Investment Funds - Maintenance 2025 - 2026 3891 May 2026
```

