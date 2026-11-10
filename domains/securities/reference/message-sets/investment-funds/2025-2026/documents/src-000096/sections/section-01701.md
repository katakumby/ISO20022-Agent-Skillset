---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.26 TransactionOverhead <TxOvrhd>", "46.4.5.10.26.7 DigitalNetworkFee <DgtlNtwkFee>", "46.4.5.10.26.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2388, 2389]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.26.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2388 to 2389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2388

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2388
     ISIN <ISIN> [0..1] IdentifierSet 2390
     OtherIdentification <OthrId> [0..*]  2390
       Identification <Id> [1..1] Text 2390
       Suffix <Sfx> [0..1] Text 2390
       Type <Tp> [1..1]  2390
{Or         Code <Cd> [1..1] CodeSet 2391
Or}         Proprietary <Prtry> [1..1] Text 2392
     Description <Desc> [0..1] Text 2392
   Quantity <Qty> [1..1]  2393
{Or     Quantity <Qty> [1..1] ± C16 2393
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2393
       Quantity <Qty> [1..1] Quantity 2394
       QuantityType <QtyTp> [1..1] Text 2394
       Issuer <Issr> [1..1] Text 2394
       SchemeName <SchmeNm> [0..1] Text 2394
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2394
46.4.5.10.26.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C14 "DescriptionPresenceRule", C15 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C28 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2388 May 2026
```

## File page 2389

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2390
   OtherIdentification <OthrId> [0..*]  2390
     Identification <Id> [1..1] Text 2390
     Suffix <Sfx> [0..1] Text 2390
     Type <Tp> [1..1]  2390
{Or       Code <Cd> [1..1] CodeSet 2391
Or}       Proprietary <Prtry> [1..1] Text 2392
   Description <Desc> [0..1] Text 2392
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
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2389 May 2026
```

