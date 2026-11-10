---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.35 CashSettlementDetails <CshSttlmDtls>", "52.4.5.10.35.1 PaymentInstrument <PmtInstrm>", "52.4.5.10.35.1.7 BlockChainCashWallet <BlckChainCshWllt>", "52.4.5.10.35.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>"]
file_pages: [3416, 3417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.35.1.7.4 DigitalLedgerIdentification <DgtlLdgrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3416 to 3417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3416

```text
52.4.5.10.35.1.7.4  DigitalLedgerIdentification <DgtlLdgrId>
Presence: [1..1]
Definition: Place of safekeeping expressed with a Digital Ledger Identifier. It identifies a digital ledger or
distributed ledger system (for example, blockchain or similar platforms).
Datatype: "DTI2024Identifier" on page 5392
52.4.5.10.36  DigitalAssetSettlement <DgtlAsstSttlm>
Presence: [0..1]
Definition: Total quantity of digital asset to be paid or received in exchange for the securities token.
DigitalAssetSettlement <DgtlAsstSttlm> contains the following DigitalPaymentSettlement3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1]  C16,
C17,
C24,
C25,
C31
3416
     ISIN <ISIN> [0..1] IdentifierSet 3418
     OtherIdentification <OthrId> [0..*]  3418
       Identification <Id> [1..1] Text 3418
       Suffix <Sfx> [0..1] Text 3418
       Type <Tp> [1..1]  3418
{Or         Code <Cd> [1..1] CodeSet 3419
Or}         Proprietary <Prtry> [1..1] Text 3420
     Description <Desc> [0..1] Text 3420
   Quantity <Qty> [1..1]  3421
{Or     Quantity <Qty> [1..1] ± C18 3421
Or}     ProprietaryQuantity <PrtryQty> [1..1]  3421
       Quantity <Qty> [1..1] Quantity 3422
       QuantityType <QtyTp> [1..1] Text 3422
       Issuer <Issr> [1..1] Text 3422
       SchemeName <SchmeNm> [0..1] Text 3422
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3422
52.4.5.10.36.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3416 May 2026
```

## File page 3417

```text
Impacted by: C16 "DescriptionPresenceRule", C17 "DescriptionUsageRule", C24 "ISINGuideline", C25
"ISINPresenceRule", C31 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following SecurityIdentification50
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 3418
   OtherIdentification <OthrId> [0..*]  3418
     Identification <Id> [1..1] Text 3418
     Suffix <Sfx> [0..1] Text 3418
     Type <Tp> [1..1]  3418
{Or       Code <Cd> [1..1] CodeSet 3419
Or}       Proprietary <Prtry> [1..1] Text 3420
   Description <Desc> [0..1] Text 3420
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
Investment Funds - Maintenance 2025 - 2026 3417 May 2026
```

