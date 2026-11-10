---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.26 TransactionOverhead <TxOvrhd>", "52.4.5.10.26.7 DigitalNetworkFee <DgtlNtwkFee>", "52.4.5.10.26.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [3331, 3332]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.26.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3331 to 3332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3331

```text
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C16,
C17,
C24,
C25,
C31
3331
     ISIN <ISIN> [0..1] IdentifierSet 3333
     OtherIdentification <OthrId> [0..*]  3333
       Identification <Id> [1..1] Text 3333
       Suffix <Sfx> [0..1] Text 3333
       Type <Tp> [1..1]  3333
{Or         Code <Cd> [1..1] CodeSet 3334
Or}         Proprietary <Prtry> [1..1] Text 3335
     Description <Desc> [0..1] Text 3335
   Quantity <Qty> [1..1]  3336
{Or     Quantity <Qty> [1..1] ± C18 3336
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3336
       Quantity <Qty> [1..1] Quantity 3337
       QuantityType <QtyTp> [1..1] Text 3337
       Issuer <Issr> [1..1] Text 3337
       SchemeName <SchmeNm> [0..1] Text 3337
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3337
52.4.5.10.26.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C16 "DescriptionPresenceRule", C17 "DescriptionUsageRule", C24 "ISINGuideline", C25
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3331 May 2026
```

## File page 3332

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3333
   OtherIdentification <OthrId> [0..*]  3333
     Identification <Id> [1..1] Text 3333
     Suffix <Sfx> [0..1] Text 3333
     Type <Tp> [1..1]  3333
{Or       Code <Cd> [1..1] CodeSet 3334
Or}       Proprietary <Prtry> [1..1] Text 3335
   Description <Desc> [0..1] Text 3335
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
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3332 May 2026
```

