---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.16 TransactionOverhead <TxOvrhd>", "47.4.4.8.16.4 DigitalNetworkFee <DgtlNtwkFee>"]
file_pages: [2609, 2610]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.16.4 DigitalNetworkFee <DgtlNtwkFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2609 to 2610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2609

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
47.4.4.8.16.4  DigitalNetworkFee <DgtlNtwkFee>
Presence: [0..*]
Definition: Digital payment settlement information or digital network fee assigned to a transaction.
DigitalNetworkFee <DgtlNtwkFee> contains the following DigitalPaymentSettlement3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2609
     ISIN <ISIN> [0..1] IdentifierSet 2611
     OtherIdentification <OthrId> [0..*]  2611
       Identification <Id> [1..1] Text 2611
       Suffix <Sfx> [0..1] Text 2611
       Type <Tp> [1..1]  2611
{Or         Code <Cd> [1..1] CodeSet 2612
Or}         Proprietary <Prtry> [1..1] Text 2613
     Description <Desc> [0..1] Text 2613
   Quantity <Qty> [1..1]  2614
{Or     Quantity <Qty> [1..1] ± C15 2614
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2614
       Quantity <Qty> [1..1] Quantity 2615
       QuantityType <QtyTp> [1..1] Text 2615
       Issuer <Issr> [1..1] Text 2615
       SchemeName <SchmeNm> [0..1] Text 2615
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2615
47.4.4.8.16.4.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2609 May 2026
```

## File page 2610

```text
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2611
   OtherIdentification <OthrId> [0..*]  2611
     Identification <Id> [1..1] Text 2611
     Suffix <Sfx> [0..1] Text 2611
     Type <Tp> [1..1]  2611
{Or       Code <Cd> [1..1] CodeSet 2612
Or}       Proprietary <Prtry> [1..1] Text 2613
   Description <Desc> [0..1] Text 2613
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
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2610 May 2026
```

