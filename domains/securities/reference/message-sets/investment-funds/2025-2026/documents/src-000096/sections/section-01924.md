---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.20 CashSettlementDetails <CshSttlmDtls>", "47.4.4.8.20.1 PaymentInstrument <PmtInstrm>", "47.4.4.8.20.1.7 BlockChainCashWallet <BlckChainCshWllt>", "47.4.4.8.20.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [2690, 2691]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.20.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2690 to 2691.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2690

```text
47.4.4.8.20.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
47.4.4.8.21  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
2690
     ISIN <ISIN> [0..1] IdentifierSet 2692
     OtherIdentification <OthrId> [0..*]  2692
       Identification <Id> [1..1] Text 2692
       Suffix <Sfx> [0..1] Text 2692
       Type <Tp> [1..1]  2692
{Or         Code <Cd> [1..1] CodeSet 2693
Or}         Proprietary <Prtry> [1..1] Text 2694
     Description <Desc> [0..1] Text 2694
   Quantity <Qty> [1..1]  2695
{Or     Quantity <Qty> [1..1] ± C15 2695
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2695
       Quantity <Qty> [1..1] Quantity 2696
       QuantityType <QtyTp> [1..1] Text 2696
       Issuer <Issr> [1..1] Text 2696
       SchemeName <SchmeNm> [0..1] Text 2696
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2696
47.4.4.8.21.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2690 May 2026
```

## File page 2691

```text
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C22 "ISINGuideline", C23
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2692
   OtherIdentification <OthrId> [0..*]  2692
     Identification <Id> [1..1] Text 2692
     Suffix <Sfx> [0..1] Text 2692
     Type <Tp> [1..1]  2692
{Or       Code <Cd> [1..1] CodeSet 2693
Or}       Proprietary <Prtry> [1..1] Text 2694
   Description <Desc> [0..1] Text 2694
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
Investment Funds - Maintenance 2025 - 2026 2691 May 2026
```

