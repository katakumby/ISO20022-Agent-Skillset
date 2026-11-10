---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.15 TransactionOverhead <TxOvrhd>", "41.4.4.8.15.4 DigitalNetworkFee <DgtlNtwkFee>"]
file_pages: [1764, 1765]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.15.4 DigitalNetworkFee <DgtlNtwkFee>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1764 to 1765.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1764

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
41.4.4.8.15.4  DigitalNetworkFee <DgtlNtwkFee>
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
1764
     ISIN <ISIN> [0..1] IdentifierSet 1766
     OtherIdentification <OthrId> [0..*]  1766
       Identification <Id> [1..1] Text 1766
       Suffix <Sfx> [0..1] Text 1766
       Type <Tp> [1..1]  1766
{Or         Code <Cd> [1..1] CodeSet 1767
Or}         Proprietary <Prtry> [1..1] Text 1768
     Description <Desc> [0..1] Text 1768
   Quantity <Qty> [1..1]  1769
{Or     Quantity <Qty> [1..1] ± C15 1769
Or}     ProprietaryQuantity <PrtryQty> [1..1]  1769
       Quantity <Qty> [1..1] Quantity 1770
       QuantityType <QtyTp> [1..1] Text 1770
       Issuer <Issr> [1..1] Text 1770
       SchemeName <SchmeNm> [0..1] Text 1770
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1770
41.4.4.8.15.4.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1764 May 2026
```

## File page 1765

```text
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1766
   OtherIdentification <OthrId> [0..*]  1766
     Identification <Id> [1..1] Text 1766
     Suffix <Sfx> [0..1] Text 1766
     Type <Tp> [1..1]  1766
{Or       Code <Cd> [1..1] CodeSet 1767
Or}       Proprietary <Prtry> [1..1] Text 1768
   Description <Desc> [0..1] Text 1768
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
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1765 May 2026
```

