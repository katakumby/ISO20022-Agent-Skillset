---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.34 CashSettlementDetails <CshSttlmDtls>", "49.4.5.9.34.1 PaymentInstrument <PmtInstrm>", "49.4.5.9.34.1.7 BlockChainCashWallet <BlckChainCshWllt>", "49.4.5.9.34.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [2930, 2931]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.34.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2930 to 2931.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2930

```text
49.4.5.9.34.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
49.4.5.9.35  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2930
     ISIN <ISIN> [0..1] IdentifierSet 2932
     OtherIdentification <OthrId> [0..*]  2932
       Identification <Id> [1..1] Text 2932
       Suffix <Sfx> [0..1] Text 2932
       Type <Tp> [1..1]  2932
{Or         Code <Cd> [1..1] CodeSet 2933
Or}         Proprietary <Prtry> [1..1] Text 2934
     Description <Desc> [0..1] Text 2934
   Quantity <Qty> [1..1]  2935
{Or     Quantity <Qty> [1..1] ± C16 2935
Or}     ProprietaryQuantity <PrtryQty> [1..1]  2935
       Quantity <Qty> [1..1] Quantity 2936
       QuantityType <QtyTp> [1..1] Text 2936
       Issuer <Issr> [1..1] Text 2936
       SchemeName <SchmeNm> [0..1] Text 2936
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2936
49.4.5.9.35.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2930 May 2026
```

## File page 2931

```text
Impacted by: C14 "DescriptionPresenceRule", C15 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C28 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2932
   OtherIdentification <OthrId> [0..*]  2932
     Identification <Id> [1..1] Text 2932
     Suffix <Sfx> [0..1] Text 2932
     Type <Tp> [1..1]  2932
{Or       Code <Cd> [1..1] CodeSet 2933
Or}       Proprietary <Prtry> [1..1] Text 2934
   Description <Desc> [0..1] Text 2934
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
Investment Funds - Maintenance 2025 - 2026 2931 May 2026
```

