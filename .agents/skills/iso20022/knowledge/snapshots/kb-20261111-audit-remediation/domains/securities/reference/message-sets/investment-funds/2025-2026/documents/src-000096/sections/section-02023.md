---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.26 TransactionOverhead <TxOvrhd>", "49.4.5.9.26.7 DigitalNetworkFee <DgtlNtwkFee>", "49.4.5.9.26.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [2846, 2847]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.26.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2846 to 2847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2846

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
2846
     ISIN <ISIN> [0..1] IdentifierSet 2848
     OtherIdentification <OthrId> [0..*]  2848
       Identification <Id> [1..1] Text 2848
       Suffix <Sfx> [0..1] Text 2848
       Type <Tp> [1..1]  2848
{Or         Code <Cd> [1..1] CodeSet 2849
Or}         Proprietary <Prtry> [1..1] Text 2850
     Description <Desc> [0..1] Text 2850
   Quantity <Qty> [1..1]  2851
{Or     Quantity <Qty> [1..1] ± C16 2851
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2851
       Quantity <Qty> [1..1] Quantity 2852
       QuantityType <QtyTp> [1..1] Text 2852
       Issuer <Issr> [1..1] Text 2852
       SchemeName <SchmeNm> [0..1] Text 2852
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2852
49.4.5.9.26.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C14 "DescriptionPresenceRule", C15 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C28 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2846 May 2026
```

## File page 2847

```text
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2848
   OtherIdentification <OthrId> [0..*]  2848
     Identification <Id> [1..1] Text 2848
     Suffix <Sfx> [0..1] Text 2848
     Type <Tp> [1..1]  2848
{Or       Code <Cd> [1..1] CodeSet 2849
Or}       Proprietary <Prtry> [1..1] Text 2850
   Description <Desc> [0..1] Text 2850
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
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2847 May 2026
```

