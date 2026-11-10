---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "44.4.4.9.15 TransactionOverhead <TxOvrhd>", "44.4.4.9.15.4 DigitalNetworkFee <DgtlNtwkFee>"]
file_pages: [2181, 2182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.9.15.4 DigitalNetworkFee <DgtlNtwkFee>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2181 to 2182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2181

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
44.4.4.9.15.4  DigitalNetworkFee <DgtlNtwkFee>
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
2181
     ISIN <ISIN> [0..1] IdentifierSet 2183
     OtherIdentification <OthrId> [0..*]  2183
       Identification <Id> [1..1] Text 2183
       Suffix <Sfx> [0..1] Text 2183
       Type <Tp> [1..1]  2183
{Or         Code <Cd> [1..1] CodeSet 2184
Or}         Proprietary <Prtry> [1..1] Text 2185
     Description <Desc> [0..1] Text 2185
   Quantity <Qty> [1..1]  2186
{Or     Quantity <Qty> [1..1] ± C15 2186
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2186
       Quantity <Qty> [1..1] Quantity 2187
       QuantityType <QtyTp> [1..1] Text 2187
       Issuer <Issr> [1..1] Text 2187
       SchemeName <SchmeNm> [0..1] Text 2187
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2187
44.4.4.9.15.4.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2181 May 2026
```

## File page 2182

```text
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2183
   OtherIdentification <OthrId> [0..*]  2183
     Identification <Id> [1..1] Text 2183
     Suffix <Sfx> [0..1] Text 2183
     Type <Tp> [1..1]  2183
{Or       Code <Cd> [1..1] CodeSet 2184
Or}       Proprietary <Prtry> [1..1] Text 2185
   Description <Desc> [0..1] Text 2185
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
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2182 May 2026
```

