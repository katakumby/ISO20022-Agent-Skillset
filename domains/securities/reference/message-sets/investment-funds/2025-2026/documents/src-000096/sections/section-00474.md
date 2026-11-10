---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.12 UnitsDetails <UnitsDtls>", "28.4.7.12.8 TransactionOverhead <TxOvrhd>", "28.4.7.12.8.7 DigitalNetworkFee <DgtlNtwkFee>", "28.4.7.12.8.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [650, 651]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.12.8.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 650 to 651.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 650

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
650
     ISIN <ISIN> [0..1] IdentifierSet 652
     OtherIdentification <OthrId> [0..*]  652
       Identification <Id> [1..1] Text 652
       Suffix <Sfx> [0..1] Text 652
       Type <Tp> [1..1]  652
{Or         Code <Cd> [1..1] CodeSet 653
Or}         Proprietary <Prtry> [1..1] Text 654
     Description <Desc> [0..1] Text 654
   Quantity <Qty> [1..1]  655
{Or     Quantity <Qty> [1..1] ± C14 655
Or}     ProprietaryQuantity <PrtryQty> [1..1]  655
       Quantity <Qty> [1..1] Quantity 656
       QuantityType <QtyTp> [1..1] Text 656
       Issuer <Issr> [1..1] Text 656
       SchemeName <SchmeNm> [0..1] Text 656
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 656
28.4.7.12.8.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C20 "ISINGuideline", C21
"ISINPresenceRule", C24 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 650 May 2026
```

## File page 651

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 652
   OtherIdentification <OthrId> [0..*]  652
     Identification <Id> [1..1] Text 652
     Suffix <Sfx> [0..1] Text 652
     Type <Tp> [1..1]  652
{Or       Code <Cd> [1..1] CodeSet 653
Or}       Proprietary <Prtry> [1..1] Text 654
   Description <Desc> [0..1] Text 654
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
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 651 May 2026
```

